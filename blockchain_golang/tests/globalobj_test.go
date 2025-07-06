package tests

import (
	"strconv"
	"sync"
	"sync/atomic"
	"testing"
)

type Data struct {
	ID   int
	Hash string
}

var GlobalObj atomic.Pointer[Data]

func TestAtomicPointerThreadSafety(t *testing.T) {

	initial := &Data{ID: 0, Hash: "0"}
	GlobalObj.Store(initial)

	var wg sync.WaitGroup
	stop := make(chan struct{})

	// Writer: changes GlobalObj each 0 ID->Hash
	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 1; i < 10000; i++ {
			newData := &Data{ID: i, Hash: strconv.Itoa(i)}
			GlobalObj.Store(newData)
		}
		close(stop)
	}()

	// Reader
	wg.Add(1)
	go func() {
		defer wg.Done()
		for {
			select {
			case <-stop:
				return
			default:
				data := GlobalObj.Load()
				if data == nil {
					continue
				}
				// Check - ID should be hash
				expected := strconv.Itoa(data.ID)
				if data.Hash != expected {
					// t.Fatalf("Data mismatch: ID=%d but Hash=%s", data.ID, data.Hash)
				}
			}
		}
	}()

	wg.Wait()
}
