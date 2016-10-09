package main

import (
	"fmt"
	"math/rand"
	"testing"
)

func TestFib(t *testing.T) { /** from https://tour.golang.org/basics/1 */
	fmt.Println("My favorite number is", rand.Intn(10))
}
