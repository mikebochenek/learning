/* circle_intersect_test
 *
 * http://math.stackexchange.com/questions/256100/how-can-i-find-the-points-at-which-two-circles-intersect
 * http://mathworld.wolfram.com/Circle-CircleIntersection.html
 */
package main

import (
	"log"
	"testing"
)

/**
 * According to the internets:
 * Two circles intersect only iff |r1-r2|<=|C1-C2|<=|r1+r2|, where |C1-C2| is the distance
 * between the two centers. If equality holds, the circles touch and there
 * is one solution. For strict inequalities, they intersect and they have two solutions.
 */
func intersect(x1 int, y1 int, r1 int, x2 int, y2 int, r2 int) string {
	log.Printf("Input: c1=(%v,%v) r1=%v c2=(%v,%v) r2=%v", x1, y1, r1, x2, y2, r2)
	ret := "0"

	// instead of calculating actual distance, distance ^ 2 is good enough for us
	distance_squared := square(x2-x1) + square(y2-y1)

	if x1 == x2 && y1 == y2 && r1 == r2 {
		ret = "Equal" // they are equal only if x,y and radius are exactly equal
	} else if distance_squared == square(r1-r2) || distance_squared == square(r1+r2) {
		ret = "1"
	} else if square(r1-r2) <= distance_squared && distance_squared <= square(r1+r2) {
		ret = "2"
	}

	log.Printf("Output: %v", ret)
	return ret
}

func square(x int) int {
	return x * x
}

func TestIntersect(t *testing.T) {
	if x := intersect(0, 0, 2, 3, 0, 2); x != "2" {
		t.Errorf("should return 2, but got %v", x)
	}
	if x := intersect(0, 0, 1, 0, 2, 1); x != "1" {
		t.Errorf("should return 1, but got %v", x)
	}
	if x := intersect(0, 0, 5, 5, 5, 2); x != "0" {
		t.Errorf("should return 0, but got %v", x)
	}
	if x := intersect(0, 0, 1, 0, 0, 1); x != "Equal" {
		t.Errorf("should return Equal, but got %v", x)
	}
	if x := intersect(0, 0, 5, 2, 2, 1); x != "0" {
		t.Errorf("should return 0, but got %v", x)
	}
	if x := intersect(0, 0, 2, 0, 1, 2); x != "2" {
		t.Errorf("should return 2, but got %v", x)
	}
}
