package tests

import (
	"fmt"
	"strconv"
	"testing"

	"github.com/syndtr/goleveldb/leveldb"
)

func TestLevelDB(t *testing.T) {

	db, _ := leveldb.OpenFile("TEST", nil)

	defer db.Close()

	// Test batch write

	batch := new(leveldb.Batch)

	commonValue := []byte("llkfsdjlfsdjfjgoejjfgoigjdpfjdgjdfjgdfgdgd6fg4df5g4df5g4d5g4df5g4dgfsdf4sd4fs3df4sf4sf4sdf354we3r54we3f54e3rg4df3g4df34f3r4w3erw4e3r5w4e35r4235433544grg3h4y35h435yth434354d35qw43qw4e3qwe43qw5e4q35w43g5f4g3d5f4g3re54g3re5g43erg4")

	for i := 0; i < 100_000; i++ {

		key := []byte("Hellofksdfklsdjfksdjfowhui2hiroisjuihiuwbkfsd2fs4d2f4s2fsdfknjsnf" + strconv.Itoa(i))

		batch.Put(key, commonValue)

	}

	err := db.Write(batch, nil)

	if err != nil {

		fmt.Println("Error occured")

	}

}

func TestLevelDBRead(t *testing.T) {

	db, _ := leveldb.OpenFile("TEST", nil)

	defer db.Close()

	for i := 0; i < 100_000; i++ {

		key := []byte("Hellofksdfklsdjfksdjfowhui2hiroisjuihiuwbkfsd2fs4d2f4s2fsdfknjsnf" + strconv.Itoa(i))

		_, err := db.Get([]byte(key), nil)

		if err != nil {

			fmt.Println("Error when reading => ", string(key))

		}

	}

}
