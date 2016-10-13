package main

import (
	"fmt"
	"time"
)

func saySomething(s string, j int) {
	for i := 0; i < 100; i++ {
		go fmt.Println(s, j, i)
	} // weird that it's so random...
}

func main() {
	for i := 0; i < 50; i++ {
		go saySomething("what?", i)
	}
	time.Sleep(500 * time.Millisecond)
	fmt.Println("all done")
}
