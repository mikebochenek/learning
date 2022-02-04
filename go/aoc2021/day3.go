package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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
	var total int64 = 0
	var lines int64 = 0
	for scanner.Scan() {
		word := scanner.Text()
		lines = lines + 1

		if i, err := strconv.ParseInt(word, 2, 64); err != nil {
			fmt.Println(err)
		} else {
			fmt.Println(lines, i, word)
			total = total + i
		}
		// is most common the average? what would be least common, then?
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println(total, lines, total * 1.0 / lines)

	fmt.Println("\nresults:", gamma, epsilon, gamma*epsilon)
}

