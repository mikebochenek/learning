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
	for scanner.Scan() {
		line := scanner.Text()
		first := line[0:len(line)/2]
		second := line[len(first):len(line)]

		priority := first[0]
		for i := 0; i < len(first); i++ {
			if (bytes.Contains([]byte(second), []byte{first[i]})) {
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
