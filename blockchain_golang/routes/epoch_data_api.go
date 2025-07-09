package routes

import (
	"encoding/json"
	"strconv"

	"github.com/KlyntarNetwork/Web1337Golang/crypto_primitives/ed25519"
	"github.com/VladChernenko/UndchainCore/block"
	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
	"github.com/valyala/fasthttp"
)

type ErrMsg struct {
	Err string `json:"err"`
}

type AlignmentData struct {
	ProposedIndexOfLeader            int                                    `json:"proposedIndexOfLeader"`
	FirstBlockByCurrentLeader        block.Block                            `json:"firstBlockByCurrentLeader"`
	AfpForSecondBlockByCurrentLeader structures.AggregatedFinalizationProof `json:"afpForSecondBlockByCurrentLeader"`
}

func sendJson(ctx *fasthttp.RequestCtx, payload any) {
	ctx.SetContentType("application/json")
	ctx.SetStatusCode(fasthttp.StatusOK)
	jsonBytes, _ := json.Marshal(payload)
	ctx.SetBody(jsonBytes)
}

func GetFirstBlockAssumption(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	epochIndexVal := ctx.UserValue("epochIndex")
	epochIndex, ok := epochIndexVal.(string)

	if !ok {
		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.SetContentType("application/json")
		ctx.Write([]byte(`{"err": "Invalid epoch index"}`))
		return
	}

	value, err := globals.EPOCH_DATA.Get([]byte("FIRST_BLOCK_ASSUMPTION:"+epochIndex), nil)

	if err == nil && value != nil {
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.SetContentType("application/json")
		ctx.Write(value)
		return
	}

	ctx.SetStatusCode(fasthttp.StatusNotFound)
	ctx.SetContentType("application/json")
	ctx.Write([]byte(`{"err": "No assumptions found"}`))
}

func GetAggregatedEpochFinalizationProof(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	epochIndexVal := ctx.UserValue("epochIndex")
	epochIndex, ok := epochIndexVal.(string)

	if !ok {
		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.SetContentType("application/json")
		ctx.Write([]byte(`{"err": "Invalid epoch index"}`))
		return
	}

	value, err := globals.EPOCH_DATA.Get([]byte("AEFP:"+epochIndex), nil)

	if err == nil && value != nil {
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.SetContentType("application/json")
		ctx.Write(value)
		return
	}

	ctx.SetStatusCode(fasthttp.StatusNotFound)
	ctx.SetContentType("application/json")
	ctx.Write([]byte(`{"err": "No assumptions found"}`))
}

func GetSequenceAlignmentData(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	epochHandler := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	epochIndex := epochHandler.Id

	localIndexOfLeader := epochHandler.CurrentLeaderIndex

	pubKeyOfCurrentLeader := epochHandler.LeadersSequence[localIndexOfLeader]

	firstBlockIdByThisLeader := strconv.Itoa(epochIndex) + ":" + pubKeyOfCurrentLeader + ":0"

	firstBlockAsBytes, dbErr := globals.BLOCKS.Get([]byte(firstBlockIdByThisLeader), nil)

	if dbErr == nil {

		var firstBlockParsed block.Block

		parseErr := json.Unmarshal(firstBlockAsBytes, &firstBlockParsed)

		if parseErr == nil {

			secondBlockID := strconv.Itoa(epochIndex) + ":" + pubKeyOfCurrentLeader + ":1"

			afpForSecondBlockByCurrentLeader := common_functions.GetVerifiedAggregatedFinalizationProofByBlockId(secondBlockID, epochHandler)

			if afpForSecondBlockByCurrentLeader != nil {

				alignmentDataResponse := AlignmentData{
					ProposedIndexOfLeader:            localIndexOfLeader,
					FirstBlockByCurrentLeader:        firstBlockParsed,
					AfpForSecondBlockByCurrentLeader: *afpForSecondBlockByCurrentLeader,
				}

				sendJson(ctx, alignmentDataResponse)

			} else {

				sendJson(ctx, ErrMsg{Err: "No AFP for second block"})

			}

		} else {

			sendJson(ctx, ErrMsg{Err: "No first block"})

		}

	} else {

		sendJson(ctx, ErrMsg{Err: "No first block"})

	}

}

func EpochProposition(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	if string(ctx.Method()) != fasthttp.MethodPost {
		ctx.SetStatusCode(fasthttp.StatusMethodNotAllowed)
		return
	}

	var proposition structures.EpochFinishRequest

	if err := json.Unmarshal(ctx.PostBody(), &proposition); err != nil {
		sendJson(ctx, ErrMsg{Err: "Wrong format"})
		return
	}

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RLock()

	defer globals.APPROVEMENT_THREAD_METADATA_HANDLER.RWMutex.RUnlock()

	epochHandler := &globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler

	epochIndex := epochHandler.Id

	epochFullID := epochHandler.Hash + "#" + strconv.Itoa(int(epochHandler.Id))

	localIndexOfLeader := epochHandler.CurrentLeaderIndex

	pubKeyOfCurrentLeader := epochHandler.LeadersSequence[localIndexOfLeader]

	if utils.SignalAboutEpochRotationExists(epochIndex) {

		votingMetadataForPool := strconv.Itoa(epochIndex) + ":" + pubKeyOfCurrentLeader

		votingRaw, err := globals.FINALIZATION_VOTING_STATS.Get([]byte(votingMetadataForPool), nil)

		var votingData structures.PoolVotingStat

		if err != nil || votingRaw == nil {

			votingData = structures.NewPoolVotingStatTemplate()

		} else {
			_ = json.Unmarshal(votingRaw, &votingData)
		}

		blockID := strconv.Itoa(epochIndex) + ":" + pubKeyOfCurrentLeader + ":0"

		var hashOfFirstBlock string

		if proposition.AfpForFirstBlock.BlockId == blockID && proposition.LastBlockProposition.Index >= 0 {

			if common_functions.VerifyAggregatedFinalizationProof(&proposition.AfpForFirstBlock, epochHandler) {

				hashOfFirstBlock = proposition.AfpForFirstBlock.BlockHash

			}

		}

		if hashOfFirstBlock == "" {

			sendJson(ctx, ErrMsg{Err: "Can't verify hash"})

			return

		}

		if proposition.CurrentLeader == localIndexOfLeader {

			if votingData.Index == proposition.LastBlockProposition.Index && votingData.Hash == proposition.LastBlockProposition.Hash {

				dataToSign := "EPOCH_DONE:" +
					strconv.Itoa(proposition.CurrentLeader) + ":" +
					strconv.Itoa(proposition.LastBlockProposition.Index) + ":" +
					proposition.LastBlockProposition.Hash + ":" +
					hashOfFirstBlock + ":" +
					epochFullID

				response := structures.EpochFinishResponseOk{
					Status: "OK",
					Sig:    ed25519.GenerateSignature(globals.CONFIGURATION.PrivateKey, dataToSign),
				}

				sendJson(ctx, response)

			} else if votingData.Index > proposition.LastBlockProposition.Index {

				response := structures.EpochFinishResponseUpgrade{
					Status:               "UPGRADE",
					CurrentLeader:        localIndexOfLeader,
					LastBlockProposition: votingData,
				}

				sendJson(ctx, response)

			}

		} else if proposition.CurrentLeader < localIndexOfLeader {

			response := structures.EpochFinishResponseUpgrade{
				Status:               "UPGRADE",
				CurrentLeader:        localIndexOfLeader,
				LastBlockProposition: votingData,
			}

			sendJson(ctx, response)

		}

	} else {

		sendJson(ctx, ErrMsg{Err: "Too early"})

	}

}
