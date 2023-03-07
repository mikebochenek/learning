package main

import "fmt"
import "sync"
import "time"
import "math/rand"

func DoWork() int { 
	time.Sleep(time.Second)
	return rand.Intn(100) // not very random yet
}

func main() {
	dataChan := make(chan int)

	go func() {
		wg := sync.WaitGroup{}
		for i := 0; i< 10; i++ {
			wg.Add(1)
			go func() {
				defer wg.Done()
				result := DoWork()
				dataChan <- result
			}()
		}
		wg.Wait()
		close(dataChan)
	}()


	for n := range dataChan {
		fmt.Printf("n = %d\n", n)
	}
}