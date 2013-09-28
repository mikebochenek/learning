// +build coding_kata_01

package main

import (
	"fmt"
	"math"
	"testing"
)

func TestCheck(t *testing.T) {

	if x := check(17); x != 1 {
		t.Errorf("check(17) = %v, want 1", x)
	}

	/*
		check(17)         //1
		check(1073741824) //30
		check(25)         //2
	*/
}
func check(input int) int {
	for y := 1; y <= int(math.Sqrt(float64(input))); y++ {
		for p := 32; p > 0; p-- {
			x := math.Pow(float64(y), float64(p))
			if int(x) == input {
				fmt.Printf("%d^%d = %d\n", y, p, int(x))
				return p
			}
		}
	}
	return 1 // if not found, then x**1=x
}
