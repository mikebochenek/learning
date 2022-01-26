package main

import (
	"fmt"
	"log"
	"net/http"
	"strconv"
	"time"
)

/*
 * https://blog.devgenius.io/golangs-most-important-feature-is-invisible-6be9c1e7249b
 * % ab -c 160 -n 100000 -s 2 -k  "http://127.0.0.1:9100/"
 * test with: http://localhost:8080/?param1=2
 */
func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
		param1 := req.URL.Query().Get("param1")
		x, err := strconv.Atoi(param1)
		if err != nil {
			//println("invalid input") // funny that this check is "forced" onto the developer
		} else {
			start := time.Now()
			println(start.Format(time.StampMilli), "processing input", param1, "gives", prime(x), fib(x), time.Now().Sub(start))
			fmt.Fprintln(w, x, "is prime?", prime(x), "Fibonacci", fib(x))
		}
	})
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func prime(x int) bool {
	for i := 2; i < x; i += 2 {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func fib(a int) int {
	if a < 2 {
		return a
	}
	return fib(a-1) + fib(a-2)
}
