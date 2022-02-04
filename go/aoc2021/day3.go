package main

import (
	"bufio"
	"fmt"
	"os"
//	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/input.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	gamma := 0
	epsilon := 0
	for scanner.Scan() {
		word := scanner.Text()
		fmt.Println(word)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("\nresults:", gamma, epsilon, gamma*epsilon)
}

