package routes

import (
	"encoding/json"

	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
	"github.com/valyala/fasthttp"
)

func GetBlockById(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	blockIdRaw := ctx.UserValue("id")
	blockId, ok := blockIdRaw.(string)

	if !ok {
		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.SetContentType("application/json")
		ctx.Write([]byte(`{"err": "Invalid value"}`))
		return
	}

	block, err := globals.BLOCKS.Get([]byte(blockId), nil)

	if err == nil && block != nil {
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.SetContentType("application/json")
		ctx.Write(block)
		return
	}

	ctx.SetStatusCode(fasthttp.StatusNotFound)
	ctx.SetContentType("application/json")
	ctx.Write([]byte(`{"err": "Not found"}`))
}

func GetAggregatedFinalizationProof(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	blockIdRaw := ctx.UserValue("blockId")
	blockId, ok := blockIdRaw.(string)

	if !ok {
		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.SetContentType("application/json")
		ctx.Write([]byte(`{"err": "Invalid value"}`))
		return
	}

	afp, err := globals.EPOCH_DATA.Get([]byte("AFP:"+blockId), nil)

	if err == nil && afp != nil {
		ctx.SetStatusCode(fasthttp.StatusOK)
		ctx.SetContentType("application/json")
		ctx.Write(afp)
		return
	}

	ctx.SetStatusCode(fasthttp.StatusNotFound)
	ctx.SetContentType("application/json")
	ctx.Write([]byte(`{"err": "Not found"}`))
}

func AcceptTransaction(ctx *fasthttp.RequestCtx) {

	ctx.Response.Header.Set("Access-Control-Allow-Origin", "*")

	var transaction structures.Transaction

	if err := json.Unmarshal(ctx.PostBody(), &transaction); err != nil {

		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.Write([]byte(`{"err":"Invalid JSON"}`))
		return

	}

	if transaction.Creator == "" || transaction.Nonce == 0 || transaction.Sig == "" {

		ctx.SetStatusCode(fasthttp.StatusBadRequest)
		ctx.Write([]byte(`{"err":"Event structure is wrong"}`))
		return

	}

	currentLeader := utils.GetCurrentLeader()

	if !currentLeader.IsMeLeader {

		// Redirect tx to leader

		req := fasthttp.AcquireRequest()
		defer fasthttp.ReleaseRequest(req)
		resp := fasthttp.AcquireResponse()
		defer fasthttp.ReleaseResponse(resp)

		req.SetRequestURI(currentLeader.Url + "/transaction")
		req.Header.SetMethod(fasthttp.MethodPost)
		req.SetBody(ctx.PostBody())

		if err := fasthttp.Do(req, resp); err != nil {
			ctx.SetStatusCode(fasthttp.StatusInternalServerError)
			ctx.Write([]byte(`{"err":"Impossible to redirect to current leader"}`))
			return
		}

		ctx.Write([]byte(`{"status":"Ok, tx redirected to current leader"}`))
		return

	}

	// Check mempool size

	globals.MEMPOOL.Mutex.Lock()
	defer globals.MEMPOOL.Mutex.Unlock()

	if len(globals.MEMPOOL.Slice) >= globals.CONFIGURATION.TxMemPoolSize {
		ctx.SetStatusCode(fasthttp.StatusTooManyRequests)
		ctx.Write([]byte(`{"err":"Mempool is fullfilled"}`))
		return
	}

	// Add to mempool
	globals.MEMPOOL.Slice = append(globals.MEMPOOL.Slice, transaction)

	ctx.Write([]byte(`{"status":"OK"}`))

}
