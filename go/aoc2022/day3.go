package main

import (
	"bufio"
	"fmt"
	"os"
	"bytes"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day3-1.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	score := 0
	var lines []string

	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	for j := 2; j < len(lines); j+=3 {
		first := lines[j-2]
		second := lines[j-1]
		third := lines[j]

		priority := first[0]
		for i := 0; i < len(first); i++ {
			if (bytes.Contains([]byte(second), []byte{first[i]}) && 
			    bytes.Contains([]byte(third), []byte{first[i]})) {
				priority = first[i]
				if (priority >= 97) {
					priority = priority - 96
				} else if (priority >= 65) {
					priority = priority - 64 + 26
				}
				fmt.Println("found ", first[i], priority)
			}
		}

		score = score + int(priority)

		fmt.Println(first, "  ", second)
	}

	fmt.Println("\n---> score: ", score)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
