package utils

import (
	"context"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"math/rand"
	"os"
	"strconv"
	"sync"
	"time"

	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/gorilla/websocket"
	"github.com/syndtr/goleveldb/leveldb"
	"lukechampine.com/blake3"
)

// ANSI escape codes for text colors
const (
	RESET_COLOR      = "\033[0m"
	RED_COLOR        = "\033[31;1m"
	DEEP_GREEN_COLOR = "\u001b[38;5;23m"
	GREEN_COLOR      = "\033[32;1m"
	YELLOW_COLOR     = "\033[33m"
	MAGENTA_COLOR    = "\033[38;5;99m"
	CYAN_COLOR       = "\033[36;1m"
	WHITE_COLOR      = "\033[37;1m"
)

var shutdownOnce sync.Once

var rng = rand.New(rand.NewSource(time.Now().UnixNano()))

type QuorumWaiter struct {
	responseCh chan QuorumResponse
	done       chan struct{}
	answered   map[string]bool
	responses  map[string][]byte
	timer      *time.Timer
	mu         sync.Mutex
	buf        []string
}

type QuorumResponse struct {
	id  string
	msg []byte
}

func SignalAboutEpochRotationExists(epochIndex int) bool {

	keyValue := []byte("EPOCH_FINISH:" + strconv.Itoa(epochIndex))

	if readyToChangeEpochRaw, err := globals.FINALIZATION_VOTING_STATS.Get(keyValue, nil); err == nil && string(readyToChangeEpochRaw) == "TRUE" {

		return true

	}

	return false

}

func OpenDb(dbName string) *leveldb.DB {

	db, err := leveldb.OpenFile(globals.CHAINDATA_PATH+"/DATABASES/"+dbName, nil)
	if err != nil {
		panic("Impossible to open db : " + dbName + " =>" + err.Error())
	}
	return db
}

func OpenWebsocketConnectionsWithQuorum(quorum []string, wsConnMap map[string]*websocket.Conn) {

	// Close and remove any existing connections

	// For safety reasons - close connections even in case websocket handler exists for quorum member in NEW quorum

	for id, conn := range wsConnMap {
		if conn != nil {
			_ = conn.Close()
		}
		delete(wsConnMap, id)
	}

	// Establish new connections for each validator in the quorum
	for _, validatorPubkey := range quorum {
		// Fetch validator metadata from LevelDB
		raw, err := globals.APPROVEMENT_THREAD_METADATA.Get([]byte(validatorPubkey+"(POOL)_STORAGE_POOL"), nil)

		if err != nil {
			continue
		}

		// Parse JSON metadata
		var pool structures.PoolStorage
		if err := json.Unmarshal(raw, &pool); err != nil {
			continue
		}

		// Skip inactive validators or those without WebSocket URL
		if pool.WssPoolUrl == "" {
			continue
		}

		// Open WebSocket connection
		conn, _, err := websocket.DefaultDialer.Dial(pool.WssPoolUrl, nil)

		if err != nil {
			continue
		}

		// Store the new connection in the map
		wsConnMap[validatorPubkey] = conn
	}
}

func NewQuorumWaiter(maxQuorumSize int) *QuorumWaiter {
	return &QuorumWaiter{
		responseCh: make(chan QuorumResponse, maxQuorumSize),
		done:       make(chan struct{}),
		answered:   make(map[string]bool, maxQuorumSize),
		responses:  make(map[string][]byte, maxQuorumSize),
		timer:      time.NewTimer(0),
		buf:        make([]string, 0, maxQuorumSize),
	}
}

func (qw *QuorumWaiter) sendMessages(targets []string, msg []byte, wsConnMap map[string]*websocket.Conn) {

	for _, id := range targets {

		conn, ok := wsConnMap[id]

		if !ok {
			continue
		}

		go func(id string, c *websocket.Conn) {

			if err := c.WriteMessage(websocket.TextMessage, msg); err != nil {
				return
			}

			_ = c.SetReadDeadline(time.Now().Add(time.Second))
			_, raw, err := c.ReadMessage()

			if err == nil {

				select {

				case qw.responseCh <- QuorumResponse{id: id, msg: raw}:
				case <-qw.done:

				}

			}

		}(id, conn)

	}

}

func (qw *QuorumWaiter) SendAndWait(
	ctx context.Context,
	message []byte,
	quorum []string,
	wsConnMap map[string]*websocket.Conn,
	majority int,
) (map[string][]byte, bool) {

	// Reset state
	qw.mu.Lock()
	for k := range qw.answered {
		delete(qw.answered, k)
	}
	for k := range qw.responses {
		delete(qw.responses, k)
	}
	qw.buf = qw.buf[:0]
	qw.mu.Unlock()

	if !qw.timer.Stop() {
		select {
		case <-qw.timer.C:
		default:
		}
	}
	qw.timer.Reset(time.Second)
	qw.done = make(chan struct{})

	qw.sendMessages(quorum, message, wsConnMap)

	for {
		select {
		case r := <-qw.responseCh:
			qw.mu.Lock()
			if !qw.answered[r.id] {
				qw.answered[r.id] = true
				qw.responses[r.id] = r.msg
			}
			count := len(qw.answered)
			qw.mu.Unlock()

			if count >= majority {
				close(qw.done)
				// Return copy of responses
				qw.mu.Lock()
				out := make(map[string][]byte, len(qw.responses))
				for k, v := range qw.responses {
					out[k] = v
				}
				qw.mu.Unlock()
				return out, true
			}

		case <-qw.timer.C:
			qw.mu.Lock()
			qw.buf = qw.buf[:0]
			for _, id := range quorum {
				if !qw.answered[id] {
					qw.buf = append(qw.buf, id)
				}
			}
			qw.mu.Unlock()

			if len(qw.buf) == 0 {
				return nil, false
			}
			qw.timer.Reset(time.Second)
			qw.sendMessages(qw.buf, message, wsConnMap)

		case <-ctx.Done():
			return nil, false
		}
	}
}

func GracefulShutdown() {

	shutdownOnce.Do(func() {

		LogWithTime("Stop signal has been initiated.Keep waiting...", CYAN_COLOR)

		LogWithTime("Closing server connections...", CYAN_COLOR)

		LogWithTime("Node was gracefully stopped", GREEN_COLOR)

		os.Exit(0)

	})

}

func LogWithTime(msg, msgColor string) {

	formattedDate := time.Now().Format("02 January 2006 at 03:04:05 PM")

	var prefixColor = DEEP_GREEN_COLOR

	fmt.Printf(prefixColor+"[%s]"+MAGENTA_COLOR+"(pid:%d)"+msgColor+"  %s\n"+RESET_COLOR, formattedDate, os.Getpid(), msg)

}

func Blake3(data string) string {

	blake3Hash := blake3.Sum256([]byte(data))

	return hex.EncodeToString(blake3Hash[:])

}

func GetUTCTimestampInMilliSeconds() int64 {

	return time.Now().UTC().UnixMilli()

}

type CurrentLeaderData struct {
	IsMeLeader bool
	Url        string
}

func IsMyCoreVersionOld(thread structures.LogicalThread) bool {

	return thread.GetCoreMajorVersion() > globals.CORE_MAJOR_VERSION

}

func GetRandomFromSlice(arr []structures.QuorumMemberData) structures.QuorumMemberData {

	return arr[rng.Intn(len(arr))]

}

func EpochStillFresh(thread structures.LogicalThread) bool {

	return (thread.GetEpochHandler().StartTimestamp + uint64(thread.GetNetworkParams().EpochTime)) > uint64(GetUTCTimestampInMilliSeconds())

}

func GetCurrentLeader() CurrentLeaderData {

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	currentLeaderIndex := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.CurrentLeaderIndex

	currentLeaderPubKey := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.LeadersSequence[currentLeaderIndex]

	if currentLeaderPubKey == globals.CONFIGURATION.PublicKey {

		return CurrentLeaderData{IsMeLeader: true, Url: ""}

	}

	return CurrentLeaderData{IsMeLeader: false, Url: ""}
}
