package main

import (
	"fmt"
	"math/rand"
	"testing"
)

func TestNothingInParticular(t *testing.T) { /** from https://tour.golang.org/basics/1 */
	fmt.Println("My favorite number is", rand.Intn(10))
}
