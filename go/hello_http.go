package main

import (
  "fmt"
  "log"
  "net/http"
)

/*
 * https://blog.devgenius.io/golangs-most-important-feature-is-invisible-6be9c1e7249b
 * % ab -c 160 -n 100000 -s 2 -k  "http://127.0.0.1:9100/"
*/
func main() {
  http.HandleFunc("/", func(w http.ResponseWriter, req *http.Request) {
    fmt.Fprintln(w, "Goodbye, World!")
  })
  log.Fatal(http.ListenAndServe(":8080", nil))
}
