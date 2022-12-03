package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day2-1.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	score := 0
	for scanner.Scan() {
		line := scanner.Text()
		// A for Rock, B for Paper, and C for Scissors
		// X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
		if (       line == "A Y") {
			score += (1 + 3)
		} else if (line == "B X") {
			score += (1 + 0)
		} else if (line == "C Z") {
			score += (1 + 6)
		} else if (line == "A X") {
			score += (3 + 0)
		} else if (line == "A Z") {
			score += (2 + 6)
		} else if (line == "B Y") {
			score += (2 + 3)
		} else if (line == "B Z") {
			score += (3 + 6)
		} else if (line == "C X") {
			score += (2 + 0) 
		} else if (line == "C Y") {
			score += (3 + 3)
		}
	}

	fmt.Println(score)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}
