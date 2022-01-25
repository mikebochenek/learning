package main

import (
  "fmt"
  "log"
  "net/http"
  "strconv"
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
      println("invalid input") // funny that this check is "forced" onto the developer
    }
    println("request input", param1)
    fmt.Fprintln(w, x, "is prime?", prime(x))
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
