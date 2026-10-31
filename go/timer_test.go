package main

import (
	"fmt"
	"testing"
	"time"
)

/**
 * Three ways to use a Timer from http://golang-examples.tumblr.com/
 * maybe it would be more fun to add some randomness? ..
 */
func TestTimer(t *testing.T) {
	for p := 8; p > 0; p-- {
		time.AfterFunc(200*time.Millisecond, func() {
			fmt.Printf(".") // but this is not what I had ordered at all...
		})
	}

	// (option A)
	time.AfterFunc(1*time.Second, func() {
		fmt.Printf("(A) expired \n")
	})

	// (option B) create a Timer object
	timer := time.NewTimer(1 * time.Second)
	<-timer.C
	fmt.Printf("(B) expired \n")

	// (option C) time.After() returns timer.C internally
	<-time.After(1 * time.Second)
	fmt.Printf("(C) expired \n")

	fmt.Println("Hello World!")
}
