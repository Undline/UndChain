package structures

type LogicalThread interface {
	GetCoreMajorVersion() int
	GetNetworkParams() NetworkParameters
	GetEpochHandler() EpochDataHandler
}

type ApprovementThreadMetadataHandler struct {
	CoreMajorVersion  int                     `json:"coreMajorVersion"`
	NetworkParameters NetworkParameters       `json:"networkParameters"`
	EpochDataHandler  EpochDataHandler        `json:"epoch"`
	Cache             map[string]*PoolStorage `json:"-"`
}

type ExecutionThreadMetadataHandler struct {
	CoreMajorVersion  int               `json:"coreMajorVersion"`
	NetworkParameters NetworkParameters `json:"networkParameters"`
	EpochDataHandler  EpochDataHandler  `json:"epoch"`

	LastHeight    int64  `json:"lastHeight"`
	LastBlockHash string `json:"lastBlockHash"`

	ExecutionData map[string]ExecutionStatsPerPool `json:"executionData"` // PUBKEY => {index:int, hash:""}
	AlignmentData AlignmentDataHandler             `json:"alignmentData"`

	Cache map[string]string `json:"-"`
}

func (handler *ApprovementThreadMetadataHandler) GetCoreMajorVersion() int {
	return handler.CoreMajorVersion
}

func (handler *ExecutionThreadMetadataHandler) GetCoreMajorVersion() int {
	return handler.CoreMajorVersion
}

func (handler *ApprovementThreadMetadataHandler) GetNetworkParams() NetworkParameters {
	return handler.NetworkParameters
}

func (handler *ApprovementThreadMetadataHandler) GetEpochHandler() EpochDataHandler {
	return handler.EpochDataHandler
}

func (handler *ExecutionThreadMetadataHandler) GetNetworkParams() NetworkParameters {
	return handler.NetworkParameters
}

func (handler *ExecutionThreadMetadataHandler) GetEpochHandler() EpochDataHandler {
	return handler.EpochDataHandler
}

type GenerationThreadMetadataHandler struct {
	EpochFullId string `json:"epochFullId"`
	PrevHash    string `json:"prevHash"`
	NextIndex   int    `json:"nextIndex"`
}

type AlignmentDataHandler struct {
	CurrentLeader              int                              `json:"currentLeader"`
	CurrentToExecute           int                              `json:"currentToExecute"`
	InfoAboutLastBlocksInEpoch map[string]ExecutionStatsPerPool `json:"infoAboutLastBlocksInEpoch"` // PUBKEY => {index:int, hash:""}
}
