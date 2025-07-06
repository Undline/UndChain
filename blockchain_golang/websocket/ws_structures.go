package websocket

import (
	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/structures"
)

type WsLeaderRotationProofRequest struct {
	Route               string                                 `json:"route"`
	IndexOfPoolToRotate int                                    `json:"indexOfPoolToRotate"`
	AfpForFirstBlock    structures.AggregatedFinalizationProof `json:"afpForFirstBlock"`
	SkipData            structures.PoolVotingStat              `json:"skipData"`
}

type WsLeaderRotationProofResponseOk struct {
	Voter         string `json:"voter"`
	ForPoolPubkey string `json:"forPoolPubkey"`
	Status        string `json:"status"`
	Sig           string `json:"sig"`
}

type WsLeaderRotationProofResponseUpgrade struct {
	Voter            string                                 `json:"voter"`
	ForPoolPubkey    string                                 `json:"forPoolPubkey"`
	Status           string                                 `json:"status"`
	AfpForFirstBlock structures.AggregatedFinalizationProof `json:"afpForFirstBlock"`
	SkipData         structures.PoolVotingStat              `json:"skipData"`
}

type WsFinalizationProofRequest struct {
	Route            string                                 `json:"route"`
	Block            block.Block                            `json:"block"`
	PreviousBlockAfp structures.AggregatedFinalizationProof `json:"previousBlockAfp"`
}

type WsFinalizationProofResponse struct {
	Voter             string `json:"voter"`
	FinalizationProof string `json:"finalizationProof"`
	VotedForHash      string `json:"votedForHash"`
}
