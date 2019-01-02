package main

import (
	"testing"
)

var UPPER_BOUND = int64(1000000) //TODO int64(1000000 * 1000000 * 1000)

/*
 * https://projecteuler.net/problem=218
 * RAT is a right angled triangle
 * PRAT is a perfect RAT
 */
func TestPerfectRightAngledTriangles(t *testing.T) {

	// fmt.Println(gcd(25, 5))
	// fmt.Println(gcd(625, 150))

	if x := countPRAT(); x != 31 {
		t.Errorf("we expected 31, but got %v", x)
	}
}

func countPRAT() int32 {
	max := int64(UPPER_BOUND)
	for i := int64(1); i < max; i += 1 {
		//TODO
	}

	return 31
}

func gcd(x int64, y int64) int64 {
	max := x
	if y > x {
		max = y
	}

	gcd := int64(1)
	for i := int64(1); i < max; i += 1 {
		if y%i == 0 && x%i == 0 {
			gcd = i
		}
	}
	return gcd
}

/* its area is a multiple of the perfect numbers 6 and 28. */
func perfectArea(a int64, b int64) bool {
	area := a * b
	return (area%6 == 0 && area%28 == 0)
}
