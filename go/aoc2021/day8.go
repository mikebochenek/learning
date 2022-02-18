package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/day8-0.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	for scanner.Scan() {
		word := scanner.Text()
		numbers := strings.Split(word, " ")
		fmt.Println(numbers)
	}
	// Because the digits 1, 4, 7, and 8 each use a unique number of segments

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
