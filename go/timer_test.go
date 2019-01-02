package main

import (
	"fmt"
	"testing"
	"time"
)

/**
 * Three ways to use a Timer from http://golang-examples.tumblr.com/
 */
func TestTimer(t *testing.T) {
	for p := 32; p > 0; p-- {
		time.AfterFunc(500*time.Millisecond, func() {
			fmt.Printf(".") // but this is not what I had ordered at all...
		})
	}

	// (A)
	time.AfterFunc(1*time.Second, func() {
		fmt.Printf("(A) expired \n")
	})

	// (B) create a Timer object
	timer := time.NewTimer(1 * time.Second)
	<-timer.C
	fmt.Printf("(B) expired \n")

	// (C) time.After() returns timer.C internally
	<-time.After(1 * time.Second)
	fmt.Printf("(C) expired \n")

	fmt.Println("Hello World!")
}
