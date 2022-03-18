package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const SIZE = 10
const FILENAME = "day11-0"

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/" + FILENAME + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	lines := 0
	var m [SIZE][SIZE]int
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line, len(line))
		for j := 0; j < len(line); j++ {
			x := safeParse(string(line[j]))
			m[lines][j] = x
		}
		lines = lines + 1
	}

	fmt.Println(m)

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
