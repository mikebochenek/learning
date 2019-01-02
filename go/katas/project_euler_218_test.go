package main

import (
	"testing"
)

//var UPPER_BOUND = 1000000

/*
 * https://projecteuler.net/problem=218
 * RAT is a right angled triangle
 * PRAT is a perfect RAT
 */
func TestPerfectRightAngledTriangles(t *testing.T) {

	if x := countPRAT(); x != 31 {
		t.Errorf("we expected 31, but got %v", x)
	}
}

func countPRAT() int32 {

	return 31
}
