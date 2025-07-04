package tests

import (
	"fmt"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

type MyStruct struct {
	id   int
	hash string
}

func TestPointer(t *testing.T) {

	var globalObj atomic.Pointer[MyStruct]

	initial := &MyStruct{id: 0, hash: "initial"}
	globalObj.Store(initial)

	var wg sync.WaitGroup

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 1; i <= 5; i++ {
			newObj := &MyStruct{
				id:   i,
				hash: fmt.Sprintf("hash%d", i),
			}
			globalObj.Store(newObj)
			fmt.Printf("Writer: Updated to id=%d, hash=%s\n", newObj.id, newObj.hash)
			time.Sleep(100 * time.Millisecond)
		}
	}()

	wg.Add(1)
	go func() {
		defer wg.Done()
		for i := 0; i < 10; i++ {
			obj := globalObj.Load()
			fmt.Printf("Reader: id=%d, hash=%s\n", obj.id, obj.hash)
			time.Sleep(50 * time.Millisecond)
		}
	}()

	wg.Wait()
	fmt.Println("Done")
}
