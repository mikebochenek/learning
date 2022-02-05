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
//	count1s[] := 0
	var count1s []int 
	var lines = 0
	for scanner.Scan() {
		word := scanner.Text()
		fmt.Println(word)
		lines = lines + 1
		count1s = append(count1s, lines)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("\nresults:", gamma, epsilon, gamma*epsilon)
}

