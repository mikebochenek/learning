package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day12-0.txt")
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

	for j := 0; j < len(lines); j+=1 {
		fmt.Println(lines[j])
	}

	//This path reaches the goal in 31 steps, the fewest possible.
	score = search(0, 0, 0, lines)

	fmt.Println("\n---> score: ", score)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func search(x int, y int, steps int, lines []string) int {
	fmt.Println(lines[y][x])
	return steps+1 
}