// timer
package main

import (
	"fmt"
	"time"
)

func main() {
	// (A)
	time.AfterFunc(5*time.Second, func() {
		fmt.Printf("expired")
	})

	// (B) create a Timer object
	timer := time.NewTimer(5 * time.Second)
	<-timer.C
	fmt.Printf("expired")

	// (C) time.After() returns timer.C internally
	<-time.After(5 * time.Second)
	fmt.Printf("expired")

	fmt.Println("Hello World!")
}
