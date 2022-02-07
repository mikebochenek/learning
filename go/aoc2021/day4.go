package main

import (
	"bufio"
	"fmt"
	"os"
	//	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/input0.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	var lines = 0
	for scanner.Scan() {
		word := scanner.Text()
		lines = lines + 1
		fmt.Println(lines, word)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
