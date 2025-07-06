package websocket

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"

	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/utils"
	"github.com/lxzan/gws"
)

type Handler struct{}

type IncomingMsg struct {
	Route string `json:"route"`
}

func (h *Handler) OnOpen(conn *gws.Conn) {}

func (h *Handler) OnClose(conn *gws.Conn, err error) {}

func (h *Handler) OnPing(conn *gws.Conn, payload []byte) {}

func (h *Handler) OnPong(conn *gws.Conn, payload []byte) {}

func (h *Handler) OnMessage(connection *gws.Conn, message *gws.Message) {

	defer message.Close()

	var incoming IncomingMsg

	if err := json.Unmarshal(message.Bytes(), &incoming); err != nil {

		connection.WriteMessage(gws.OpcodeText, []byte(`{"error":"invalid_json"}`))

		return

	}

	switch incoming.Route {

	case "get_finalization_proof":

		var req WsFinalizationProofRequest

		if err := json.Unmarshal(message.Bytes(), &req); err != nil {
			connection.WriteMessage(gws.OpcodeText, []byte(`{"error":"invalid_finalization_proof_request"}`))
			return
		}

		GetFinalizationProof(req, connection)

	case "get_leader_rotation_proof":

		var req WsLeaderRotationProofRequest

		if err := json.Unmarshal(message.Bytes(), &req); err != nil {
			connection.WriteMessage(gws.OpcodeText, []byte(`{"error":"invalid_leader_rotation_proof_request"}`))
			return
		}

		GetLeaderRotationProof(req, connection)

	default:
		connection.WriteMessage(gws.OpcodeText, []byte(`{"error":"unknown_type"}`))

	}
}

func CreateWebsocketServer() {

	upgrader := gws.NewUpgrader(&Handler{}, &gws.ServerOption{
		ParallelEnabled:   true,
		Recovery:          gws.Recovery,
		PermessageDeflate: gws.PermessageDeflate{Enabled: true},
	})

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {

		conn, err := upgrader.Upgrade(w, r)

		if err != nil {

			return

		}

		go func() {

			conn.ReadLoop()

		}()

	})

	wsInterface := globals.CONFIGURATION.WebSocketInterface

	wsPort := globals.CONFIGURATION.WebSocketPort

	address := wsInterface + ":" + strconv.Itoa(wsPort)

	utils.LogWithTime(fmt.Sprintf("Websocket server is starting at ws://%s ...✅", address), utils.CYAN_COLOR)

	if err := http.ListenAndServe(address, nil); err != nil {

		utils.LogWithTime(fmt.Sprintf("Error in websocket server: %s", err), utils.RED_COLOR)

	}

}
