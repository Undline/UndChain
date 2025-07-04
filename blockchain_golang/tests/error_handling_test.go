package tests

import (
	"fmt"
	"testing"
)

func HandlePanic() {
	r := recover()

	if r != nil {
		fmt.Println("RECOVER => ", r)
	}
}

func divide(divisor int, divider int) {

	defer HandlePanic()

	if divisor < divider {
		panic("start is greater than end")
	} else {
		fmt.Println(divisor / divider)
	}
}

func TestErrorHandling(t *testing.T) {

	fmt.Println("Before call")

	divide(2, 4)

	fmt.Println("After call")

}
