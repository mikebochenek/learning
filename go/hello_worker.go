// hello_worker
package main

import (
	"fmt"
	"github.com/benmanns/goworker"
)

// go build hello_worker.go  worker.go
// go run worker.go -queues=hello
func init() {
	goworker.Register("Hello", helloWorker)
}

func helloWorker(queue string, args ...interface{}) error {
	fmt.Println("Hello, world!")
	return nil
}
