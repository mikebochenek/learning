package main

import (
	"testing"
)

func bcrypt(x string) string {
	return x
}

func TestBCrypt(t *testing.T) {
	bcrypt("xx")
	// now := time.Now()
	// fmt.Printf("\n  testing with fmt [ %v ]\n", now)
	// log.Printf("\n  testing with log [ %v ]\n", now)
}
