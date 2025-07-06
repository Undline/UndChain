package structures

type NodeLevelConfig struct {
	PublicKey                                           string              `json:"PUBLIC_KEY"`
	PrivateKey                                          string              `json:"PRIVATE_KEY"`
	StoreBlocksInLocalDatabase                          bool                `json:"STORE_BLOCKS_IN_LOCAL_DATABASE"`
	PointOfDistributionWS                               string              `json:"POINT_OF_DISTRIBUTION_WS"`
	PointOfDistributionHTTP                             string              `json:"POINT_OF_DISTRIBUTION_HTTP"`
	ExtraDataToBlock                                    map[string]string   `json:"EXTRA_DATA_TO_BLOCK"`
	WaitIfCantFindAeFp                                  int                 `json:"WAIT_IF_CANT_FIND_AEFP"`
	PollingTimeoutToFindAeFpForQuorumThread             int                 `json:"POLLING_TIMEOUT_TO_FIND_AEFP_FOR_QUORUM_THREAD"`
	TimeoutToFindTempInfoAboutLastBlocksByPreviousPools int                 `json:"TIMEOUT_TO_FIND_TEMP_INFO_ABOUT_LAST_BLOCKS_BY_PREVIOUS_POOLS"`
	TxMemPoolSize                                       int                 `json:"TXS_MEMPOOL_SIZE"`
	BootstrapNodes                                      []string            `json:"BOOTSTRAP_NODES"`
	MyHostname                                          string              `json:"MY_HOSTNAME"`
	RouteTTL                                            RouteTTLConfig      `json:"ROUTE_TTL"`
	RouteTriggers                                       RouteTriggersConfig `json:"ROUTE_TRIGGERS"`
	Interface                                           string              `json:"INTERFACE"`
	Port                                                int                 `json:"PORT"`
	WebSocketInterface                                  string              `json:"WEBSOCKET_INTERFACE"`
	WebSocketPort                                       int                 `json:"WEBSOCKET_PORT"`
	PayloadSize                                         int                 `json:"PAYLOAD_SIZE"`
	MaxPayloadSize                                      int                 `json:"MAX_PAYLOAD_SIZE"`
}

type RouteTTLConfig struct {
	API RouteAPIConfig `json:"API"`
}

type RouteAPIConfig struct {
	FromState              int `json:"FROM_STATE"`
	Block                  int `json:"BLOCK"`
	PoolStats              int `json:"POOL_STATS"`
	LatestNBlocks          int `json:"LATEST_N_BLOCKS"`
	BlockBySid             int `json:"BLOCK_BY_SID"`
	SyncStats              int `json:"SYNC_STATS"`
	ChainInfo              int `json:"CHAIN_INFO"`
	TxReceipt              int `json:"TX_RECEIPT"`
	DataAboutEpochOnThread int `json:"DATA_ABOUT_EPOCH_ON_THREAD"`
	GetEpochByIndex        int `json:"GET_EPOCH_BY_INDEX"`
	QuorumUrlsAndPubkeys   int `json:"QUORUM_URLS_AND_PUBKEYS"`
	VtTotalStats           int `json:"VT_TOTAL_STATS"`
	VtStatsPerEpoch        int `json:"VT_STATS_PER_EPOCH"`
}

type RouteTriggersConfig struct {
	Main RouteMainConfig       `json:"MAIN"`
	Api  RouteAPITriggerConfig `json:"API"`
}

type RouteMainConfig struct {
	AcceptBlocksAndReturnFinalizationProofs int `json:"ACCEPT_BLOCKS_AND_RETURN_FINALIZATION_PROOFS"`
	AcceptTxs                               int `json:"ACCEPT_TXS"`
	GetAggregatedFinalizationProofs         int `json:"GET_AGGREGATED_FINALIZATION_PROOFS"`
	GetAggregatedEpochFinalizationProof     int `json:"GET_AGGREGATED_EPOCH_FINALIZATION_PROOF"`
	NewNodes                                int `json:"NEW_NODES"`
}

type RouteAPITriggerConfig struct {
	FromState              int `json:"FROM_STATE"`
	PoolStats              int `json:"POOL_STATS"`
	Block                  int `json:"BLOCK"`
	BlockBySid             int `json:"BLOCK_BY_SID"`
	LatestNBlocks          int `json:"LATEST_N_BLOCKS"`
	VtTotalStats           int `json:"VT_TOTAL_STATS"`
	VtStatsPerEpoch        int `json:"VT_STATS_PER_EPOCH"`
	SyncStats              int `json:"SYNC_STATS"`
	ChainInfo              int `json:"CHAIN_INFO"`
	TxReceipt              int `json:"TX_RECEIPT"`
	DataAboutEpochOnThread int `json:"DATA_ABOUT_EPOCH_ON_THREAD"`
	GetEpochByIndex        int `json:"GET_EPOCH_BY_INDEX"`
}
