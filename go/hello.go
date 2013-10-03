/* +build hello */

package main

import (
	"fmt"
	"log"
	"time"
)

func main() {
	now := time.Now()
	fmt.Printf("\nhello, world with fmt [ %v ]\n", now)
	log.Printf("\nhello, world with log [ %v ]\n", now)
}
