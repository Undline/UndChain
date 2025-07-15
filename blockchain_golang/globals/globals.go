package globals

import (
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync"

	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/syndtr/goleveldb/leveldb"
)

var CORE_MAJOR_VERSION = func() int {

	data, err := os.ReadFile("version.txt")

	if err != nil {
		panic("Failed to read version.txt: " + err.Error())
	}

	version, err := strconv.Atoi(string(data))

	if err != nil {
		panic("Invalid version format: " + err.Error())
	}

	return version

}()

var CHAINDATA_PATH = func() string {

	dirPath := os.Getenv("CHAINDATA_PATH")

	if dirPath == "" {

		panic("CHAINDATA_PATH environment variable is not set")

	}

	dirPath = strings.TrimRight(dirPath, "/")

	if !filepath.IsAbs(dirPath) {

		panic("CHAINDATA_PATH must be an absolute path")

	}

	// Check if exists
	if _, err := os.Stat(dirPath); os.IsNotExist(err) {

		// If no - create
		if err := os.MkdirAll(dirPath, os.ModePerm); err != nil {

			panic("Error with creating directory for chaindata: " + err.Error())

		}

	}

	return dirPath

}()

var CONFIGURATION structures.NodeLevelConfig

var GENESIS structures.Genesis

var MEMPOOL struct {
	Slice []structures.Transaction
	Mutex sync.Mutex
}

var GENERATION_THREAD_METADATA_HANDLER structures.GenerationThreadMetadataHandler

var APPROVEMENT_THREAD_METADATA_HANDLER = struct {
	RWMutex sync.RWMutex
	Handler structures.ApprovementThreadMetadataHandler
}{
	Handler: structures.ApprovementThreadMetadataHandler{
		CoreMajorVersion: -1,
		Cache:            make(map[string]*structures.PoolStorage),
	},
}

var EXECUTION_THREAD_METADATA_HANDLER = struct {
	RWMutex sync.RWMutex
	Handler structures.ExecutionThreadMetadataHandler
}{
	Handler: structures.ExecutionThreadMetadataHandler{
		CoreMajorVersion: -1,
		Cache:            make(map[string]string),
		LastHeight:       -1,
		ExecutionData:    make(map[string]structures.ExecutionStatsPerPool),
		CurrentEpochAlignmentData: structures.AlignmentDataHandler{
			Activated:                  true,
			InfoAboutLastBlocksInEpoch: make(map[string]structures.ExecutionStatsPerPool),
		},
		LegacyEpochAlignmentData: structures.AlignmentDataHandler{
			InfoAboutLastBlocksInEpoch: make(map[string]structures.ExecutionStatsPerPool),
		},
	},
}

var BLOCKS, STATE, EPOCH_DATA, APPROVEMENT_THREAD_METADATA, FINALIZATION_VOTING_STATS *leveldb.DB
