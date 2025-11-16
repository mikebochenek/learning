package main

import (
    "log"
)

// do nothing, but get rid of "no non-test Go files in ..."
func main() {
    log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile) 
    log.Println("my message includes date, time, and file information.")
}
