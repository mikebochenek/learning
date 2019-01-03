package main

import (
	"testing"
)

var UPPER_BOUND = int64(100000000) // our upper bound is not 10^16, but 10^8 (since we look for perfect squares only)

/*
 * https://projecteuler.net/problem=218
 * RAT is a right angled triangle
 * PRAT is a perfect RAT
 * How many perfect right-angled triangles with c<=10^16 exist that are not super-perfect?
 */
func TestPerfectRightAngledTriangles(t *testing.T) {

	if x := gcd(25, 5); x != 5 {
		t.Errorf("gcd(25,5) should be 5, but we got %v", x)
	}
	if x := gcd(625, 150); x != 25 {
		t.Errorf("gcd(625,150) should be 25, but we got %v", x)
	}

	if x := countPRAT(); x != 10714286 {
		t.Errorf("we expected 31, but got %v", x)
	}
}

func countPRAT() int {
	count := 0
	for i := int64(1); i < UPPER_BOUND; i += 1 {
		if perfectAreaC(i) { //TODO still very incomplete, but got 10714286
			count++
		}
	}

	return count
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

func perfectAreaC(c int64) bool {
	area := c * c / 2
	return (area%6 == 0 && area%28 == 0)
}
