package main

import (
	"testing"
)

func TestArraySum(t *testing.T) {
	ar := []int32{1, 2, 3, 4, 10, 11}

	if result := simpleArraySum(ar); result != 31 {
		t.Errorf("we expected 31, but got %v", result)
	}

	//fmt.Println(" ---            ", result)
}

func simpleArraySum(ar []int32) int32 {
	var sum int32 = 0
	for _, num := range ar {
		sum += num
	}

	return sum
}
