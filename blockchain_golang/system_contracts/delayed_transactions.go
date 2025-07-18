package system_contracts

import (
	"math/big"
	"strconv"

	"github.com/VladChernenko/UndchainCore/common_functions"
	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
)

type DelayedTxExecutorFunction = func(map[string]string) bool

var DELAYED_TRANSACTIONS_MAP = map[string]DelayedTxExecutorFunction{
	"createStakingPool": CreateStakingPool,
	"updateStakingPool": UpdateStakingPool,
	"stake":             Stake,
	"unstake":           Unstake,
}

func CreateStakingPool(delayedTransaction map[string]string) bool {

	creator := delayedTransaction["creator"]
	percentage, _ := strconv.Atoi(delayedTransaction["percentage"])
	poolURL := delayedTransaction["poolURL"]
	wssPoolURL := delayedTransaction["wssPoolURL"]

	if poolURL != "" && wssPoolURL != "" && percentage >= 0 && percentage <= 100 {

		storageKey := creator + "(POOL)_STORAGE_POOL"

		if _, exists := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache[storageKey]; exists {

			return false

		}

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache[storageKey] = &structures.PoolStorage{
			Percentage:  percentage,
			TotalStaked: structures.BigInt{Int: big.NewInt(0)},
			Stakers: map[string]structures.Staker{
				creator: {
					Stake: structures.BigInt{Int: big.NewInt(0)},
				},
			},
			PoolUrl:    poolURL,
			WssPoolUrl: wssPoolURL,
		}

		return true
	}

	return false
}

func UpdateStakingPool(delayedTransaction map[string]string) bool {

	creator := delayedTransaction["creator"]
	percentage, err1 := strconv.Atoi(delayedTransaction["percentage"])
	poolURL := delayedTransaction["poolURL"]
	wssPoolURL := delayedTransaction["wssPoolURL"]

	if err1 != nil || percentage < 0 || percentage > 100 || poolURL == "" || wssPoolURL == "" {

		return false

	}

	poolStorage := common_functions.GetFromApprovementThreadState(creator + "(POOL)_STORAGE_POOL")

	if poolStorage != nil {

		poolStorage.Percentage = percentage
		poolStorage.PoolUrl = poolURL
		poolStorage.WssPoolUrl = wssPoolURL

		requiredStake := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.ValidatorStake

		if poolStorage.TotalStaked.Int.Cmp(requiredStake.Int) >= 0 {
			globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.PoolsRegistry[creator] = struct{}{}
		} else {
			delete(globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.PoolsRegistry, creator)
		}

		globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache[creator+"(POOL)_STORAGE_POOL"] = poolStorage

		return true

	}

	return false

}

func Stake(delayedTransaction map[string]string) bool {

	staker := delayedTransaction["staker"]
	poolPubKey := delayedTransaction["poolPubKey"]
	amount, ok := new(big.Int).SetString(delayedTransaction["amount"], 10)

	if !ok {

		return false

	}

	poolStorage := common_functions.GetFromApprovementThreadState(poolPubKey + "(POOL)_STORAGE_POOL")

	if poolStorage != nil {

		minStake := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.MinimalStakePerEntity

		if amount.Cmp(minStake.Int) < 0 {

			return false

		}

		if _, exists := poolStorage.Stakers[staker]; !exists {

			poolStorage.Stakers[staker] = structures.Staker{

				Stake: structures.BigInt{Int: big.NewInt(0)},
			}

		}

		stakerData := poolStorage.Stakers[staker]
		stakerData.Stake = structures.BigInt{Int: new(big.Int).Add(stakerData.Stake.Int, amount)}
		poolStorage.TotalStaked = structures.BigInt{Int: new(big.Int).Add(poolStorage.TotalStaked.Int, amount)}
		poolStorage.Stakers[staker] = stakerData

		requiredStake := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.ValidatorStake

		if poolStorage.TotalStaked.Cmp(requiredStake.Int) >= 0 {

			if _, exists := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.PoolsRegistry[poolPubKey]; !exists {

				globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.PoolsRegistry[poolPubKey] = struct{}{}

			}

		}

		return true

	}

	return false

}

func Unstake(delayedTransaction map[string]string) bool {

	unstaker := delayedTransaction["unstaker"]
	poolPubKey := delayedTransaction["poolPubKey"]
	amount, ok := new(big.Int).SetString(delayedTransaction["amount"], 10)

	if !ok {

		return false

	}

	poolStorage := common_functions.GetFromApprovementThreadState(poolPubKey + "(POOL)_STORAGE_POOL")

	if poolStorage != nil {

		stakerData, exists := poolStorage.Stakers[unstaker]

		if !exists {

			return false

		}

		if stakerData.Stake.Cmp(amount) < 0 {

			return false

		}

		stakerData.Stake.Sub(stakerData.Stake.Int, amount)

		poolStorage.TotalStaked.Sub(poolStorage.TotalStaked.Int, amount)

		if stakerData.Stake.Cmp(big.NewInt(0)) == 0 {

			delete(poolStorage.Stakers, unstaker)

		} else {

			poolStorage.Stakers[unstaker] = stakerData

		}

		requiredStake := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.NetworkParameters.ValidatorStake

		if poolStorage.TotalStaked.Cmp(requiredStake.Int) < 0 {

			delete(globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.EpochDataHandler.PoolsRegistry, poolPubKey)

		}

		return true

	}

	return false

}
