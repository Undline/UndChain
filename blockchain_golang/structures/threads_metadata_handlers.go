package structures

type ApprovementThreadMetadataHandler struct {
	CoreMajorVersion  int                     `json:"coreMajorVersion"`
	NetworkParameters NetworkParameters       `json:"networkParameters"`
	EpochHandler      EpochHandler            `json:"epoch"`
	Cache             map[string]*PoolStorage `json:"-"`
}

type ExecutionThreadMetadataHandler struct {
	CoreMajorVersion  int               `json:"coreMajorVersion"`
	NetworkParameters NetworkParameters `json:"networkParameters"`
	EpochHandler      EpochHandler      `json:"epoch"`

	LastHeight    int64  `json:"lastHeight"`
	LastBlockHash string `json:"lastBlockHash"`

	ExecutionData map[string]ExecutionStatsPerPool `json:"executionData"` // PUBKEY => {index:int, hash:""}
	AlignmentData map[string]ExecutionStatsPerPool `json:"alignmentData"` // PUBKEY => {index:int, hash:""}

	Cache map[string]string `json:"-"` // not serialized
}

type GenerationThreadMetadataHandler struct {
	EpochFullId string `json:"epochFullId"`
	PrevHash    string `json:"prevHash"`
	NextIndex   int    `json:"nextIndex"`
}
