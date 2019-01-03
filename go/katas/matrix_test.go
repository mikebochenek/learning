package main

import (
	"fmt"
	"testing"
)

/* matrix multiplication page 152 */
func multiply(a [][]int, b [][]int) [][]int {
	for i := 0; i < len(a); i += 1 {
		for j := 0; j < len(a[i]); j += 1 {
			fmt.Println(a[i][j])
		}
	}
	return a
}

func TestMatrix(t *testing.T) {
	a := [4][3]int{{1, 0, 4}, {2, 1, 1}, {3, 1, 0}, {0, 2, 2}}
	b := [3][2]int{{2, 4}, {1, 1}, {3, 0}}
	c := [4][2]int{{14, 4}, {8, 9}, {7, 13}, {8, 2}}

	fmt.Println("input  A: ", a)
	fmt.Println("input  B: ", b)
	fmt.Println("output C: ", c)

	//fmt.Println("multiply AB", multiply(a, b)) // cannot use a (type [4][3]int) as type [][]int in argument to multiply
}
