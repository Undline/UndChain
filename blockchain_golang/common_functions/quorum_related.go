package common_functions

import (
	"encoding/json"
	"math/big"
	"strconv"

	"github.com/VladChernenko/UndchainCore/globals"
	"github.com/VladChernenko/UndchainCore/structures"
	"github.com/VladChernenko/UndchainCore/utils"
)

type ValidatorData struct {
	ValidatorPubKey string
	TotalStake      *big.Int
}

func GetFromApprovementThreadState(poolId string) *structures.PoolStorage {

	if val, ok := globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache[poolId]; ok {
		return val
	}

	data, err := globals.APPROVEMENT_THREAD_METADATA.Get([]byte(poolId), nil)

	if err != nil {
		return nil
	}

	var pool structures.PoolStorage

	err = json.Unmarshal(data, &pool)

	if err != nil {
		return nil
	}

	globals.APPROVEMENT_THREAD_METADATA_HANDLER.Handler.Cache[poolId] = &pool

	return &pool

}

func SetLeadersSequence(epochHandler *structures.EpochDataHandler, epochSeed string) {

	epochHandler.LeadersSequence = []string{} // [pool0, pool1,...poolN]

	// Hash of metadata from the old epoch

	hashOfMetadataFromOldEpoch := utils.Blake3(epochSeed)

	// Change order of validators pseudo-randomly

	validatorsExtendedData := make(map[string]ValidatorData)

	var totalStakeSum *big.Int = big.NewInt(0)

	// Populate validator data and calculate total stake sum

	for validatorPubKey := range epochHandler.PoolsRegistry {

		validatorData := GetFromApprovementThreadState(validatorPubKey + "(POOL)_STORAGE_POOL")

		// Calculate total stake

		totalStakeByThisValidator := new(big.Int)

		totalStakeByThisValidator.Add(totalStakeByThisValidator, validatorData.TotalStaked.Int)

		totalStakeSum.Add(totalStakeSum, totalStakeByThisValidator)

		validatorsExtendedData[validatorPubKey] = ValidatorData{validatorPubKey, totalStakeByThisValidator}

	}

	// Iterate over the poolsRegistry and pseudo-randomly choose leaders

	for i := range len(epochHandler.PoolsRegistry) {

		cumulativeSum := big.NewInt(0)

		// Generate deterministic random value using the hash of metadata
		hashInput := hashOfMetadataFromOldEpoch + "_" + strconv.Itoa(i)

		deterministicRandomValue := new(big.Int)

		deterministicRandomValue.SetString(utils.Blake3(hashInput), 16)

		deterministicRandomValue.Mod(deterministicRandomValue, totalStakeSum)

		// Find the validator based on the random value
		for validatorPubKey, validator := range validatorsExtendedData {

			cumulativeSum.Add(cumulativeSum, validator.TotalStake)

			if deterministicRandomValue.Cmp(cumulativeSum) <= 0 {

				// Add the chosen validator to the leaders sequence
				epochHandler.LeadersSequence = append(epochHandler.LeadersSequence, validatorPubKey)

				// Update totalStakeSum and remove the chosen validator from the map
				totalStakeSum.Sub(totalStakeSum, validator.TotalStake)

				delete(validatorsExtendedData, validatorPubKey)

				break

			}

		}

	}

}

func GetQuorumMajority(epochHandler *structures.EpochDataHandler) int {

	quorumSize := len(epochHandler.Quorum)

	majority := (2 * quorumSize) / 3

	majority += 1

	if majority > quorumSize {
		return quorumSize
	}

	return majority
}

func GetQuorumUrlsAndPubkeys(epochHandler *structures.EpochDataHandler) []structures.QuorumMemberData {

	var toReturn []structures.QuorumMemberData

	for _, pubKey := range epochHandler.Quorum {

		poolStorage := GetFromApprovementThreadState(pubKey + "(POOL)_STORAGE_POOL")

		toReturn = append(toReturn, structures.QuorumMemberData{PubKey: pubKey, Url: poolStorage.PoolUrl})

	}

	return toReturn

}

func GetCurrentEpochQuorum(epochHandler *structures.EpochDataHandler, quorumSize int, newEpochSeed string) []string {

	totalNumberOfValidators := len(epochHandler.PoolsRegistry)

	if totalNumberOfValidators <= quorumSize {

		futureQuorum := make([]string, 0, len(epochHandler.PoolsRegistry))

		for validatorPubkey := range epochHandler.PoolsRegistry {

			futureQuorum = append(futureQuorum, validatorPubkey)
		}

		return futureQuorum

	}

	quorum := []string{}

	hashOfMetadataFromEpoch := utils.Blake3(newEpochSeed)

	validatorsExtendedData := make(map[string]ValidatorData)

	totalStakeSum := big.NewInt(0)

	for validatorPubKey := range epochHandler.PoolsRegistry {

		validatorData := GetFromApprovementThreadState(validatorPubKey + "(POOL)_STORAGE_POOL")

		totalStakeByThisValidator := new(big.Int)

		totalStakeByThisValidator.Add(totalStakeByThisValidator, validatorData.TotalStaked.Int)

		validatorsExtendedData[validatorPubKey] = ValidatorData{
			ValidatorPubKey: validatorPubKey,
			TotalStake:      totalStakeByThisValidator,
		}

		totalStakeSum.Add(totalStakeSum, totalStakeByThisValidator)
	}

	for i := range quorumSize {

		cumulativeSum := big.NewInt(0)

		hashInput := hashOfMetadataFromEpoch + "_" + strconv.Itoa(i)

		deterministicRandomValue := new(big.Int)

		deterministicRandomValue.SetString(utils.Blake3(hashInput), 16)

		deterministicRandomValue.Mod(deterministicRandomValue, totalStakeSum)

		for validatorPubKey, validator := range validatorsExtendedData {

			cumulativeSum.Add(cumulativeSum, validator.TotalStake)

			if deterministicRandomValue.Cmp(cumulativeSum) <= 0 {

				quorum = append(quorum, validatorPubKey)

				totalStakeSum.Sub(totalStakeSum, validator.TotalStake)

				delete(validatorsExtendedData, validatorPubKey)

				break

			}

		}

	}

	return quorum

}
