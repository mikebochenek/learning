package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day8-1.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	lines := 0
	count := 0
	for scanner.Scan() {
		line := scanner.Text()
		words := strings.Split(line, " ")
		lines = lines + 1
		fmt.Println(len(words), words)
		for j := 10; j < len(words); j++ { //NB we start at 10!
			segments := len(words[j])
			if segments == 2 || segments == 4 || segments == 3 || segments == 7 {
				count = count + 1
			}
		}
	}
	// Because the digits 1, 4, 7, and 8 each use a unique number of segments
	//  namely            2, 4, 3, and 7 segements

	fmt.Println("\n\tlines:", lines, "count:", count)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
