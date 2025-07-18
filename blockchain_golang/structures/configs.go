package structures

type NodeLevelConfig struct {
	PublicKey                                           string            `json:"PUBLIC_KEY"`
	PrivateKey                                          string            `json:"PRIVATE_KEY"`
	StoreBlocksInLocalDatabase                          bool              `json:"STORE_BLOCKS_IN_LOCAL_DATABASE"`
	PointOfDistributionWS                               string            `json:"POINT_OF_DISTRIBUTION_WS"`
	PointOfDistributionHTTP                             string            `json:"POINT_OF_DISTRIBUTION_HTTP"`
	ExtraDataToBlock                                    map[string]string `json:"EXTRA_DATA_TO_BLOCK"`
	WaitIfCantFindAefp                                  int               `json:"WAIT_IF_CANT_FIND_AEFP"`
	PollingTimeoutToFindAefpForQuorumThread             int               `json:"POLLING_TIMEOUT_TO_FIND_AEFP_FOR_QUORUM_THREAD"`
	TimeoutToFindTempInfoAboutLastBlocksByPreviousPools int               `json:"TIMEOUT_TO_FIND_TEMP_INFO_ABOUT_LAST_BLOCKS_BY_PREVIOUS_POOLS"`
	TxMemPoolSize                                       int               `json:"TXS_MEMPOOL_SIZE"`
	BootstrapNodes                                      []string          `json:"BOOTSTRAP_NODES"`
	MyHostname                                          string            `json:"MY_HOSTNAME"`
	Interface                                           string            `json:"INTERFACE"`
	Port                                                int               `json:"PORT"`
	WebSocketInterface                                  string            `json:"WEBSOCKET_INTERFACE"`
	WebSocketPort                                       int               `json:"WEBSOCKET_PORT"`
	PayloadSize                                         int               `json:"PAYLOAD_SIZE"`
	MaxPayloadSize                                      int               `json:"MAX_PAYLOAD_SIZE"`
}
