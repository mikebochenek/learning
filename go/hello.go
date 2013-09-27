/* +build hello */

package main

import (
	"fmt"
	"log"
	"time"
)

func main() {
	now := time.Now()
	fmt.Printf("hello, world with fmt %d\n", now)
	log.Printf("hello, world with log %d\n", now)
}
