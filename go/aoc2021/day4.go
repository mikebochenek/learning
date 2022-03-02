package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day4-0.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var lines = 0
	for scanner.Scan() {
		line := scanner.Text()
		lines = lines + 1
		if len(line) > 0 && len(line) < 15 {
			words := strings.Split(line, " ")
			fmt.Println("at line:", lines, "parsed:", safeParse(words[0]))
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}
