// timer
package main

import (
	"fmt"
	"time"
)

/**
 * Three ways to use a Timer from http://golang-examples.tumblr.com/
 */
func main() {
	// (A)
	time.AfterFunc(5*time.Second, func() {
		fmt.Printf("(A) expired \n")
	})

	// (B) create a Timer object
	timer := time.NewTimer(5 * time.Second)
	<-timer.C
	fmt.Printf("(B) expired \n")

	// (C) time.After() returns timer.C internally
	<-time.After(5 * time.Second)
	fmt.Printf("(C) expired \n")

	fmt.Println("Hello World!")
}
