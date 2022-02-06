package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/input1.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	const size = 12
	var count1s [size]int
	var count0s [size]int
	var lines = 0
	for scanner.Scan() {
		word := scanner.Text()
		for i := 0; i < len(word); i++ {
			if word[i] == '0' {
				count0s[i] = count0s[i] + 1
			}
			if word[i] == '1' {
				count1s[i] = count1s[i] + 1
			}
		}
		lines = lines + 1
		//fmt.Println(count1s, count0s, lines)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	gamma := ""
	epsilon := ""
	for i := 0; i < size; i++ {
		if count1s[i] > count0s[i] {
			gamma = gamma + "1"
			epsilon = epsilon + "0"
		} else {
			gamma = gamma + "0"
			epsilon = epsilon + "1"
		}
	}

	var gammaVal int64
	if i, err := strconv.ParseInt(gamma, 2, 64); err != nil {
		fmt.Println(err)
	} else {
		gammaVal = i
	}

	var epsilonVal int64
	if i, err := strconv.ParseInt(epsilon, 2, 64); err != nil {
		fmt.Println(err)
	} else {
		epsilonVal = i
	}

	fmt.Println("\ngamma:", gammaVal, "epsilon:", epsilonVal, "product:", gammaVal*epsilonVal, lines)
}
