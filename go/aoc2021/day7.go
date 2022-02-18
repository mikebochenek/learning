package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/day7-1.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	max := 0
	if scanner.Scan() {
		word := scanner.Text()
		numbers := strings.Split(word, ",") //https://yourbasic.org/golang/string-functions-reference-cheat-sheet/
		//var pos[len(numbers)]int // https://stackoverflow.com/questions/38362631/go-error-non-constant-array-bound
		pos := make([]int, len(numbers))
		for i, number := range numbers {
			pos[i] = safeParse(number)
			if pos[i] > max {
				max = pos[i]
			}
		}
		fmt.Println(pos, "len:", len(pos), "max:", max)
		findPos(pos, max)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("short test to check fuel cost between 16 and 5:", calcCost(16, 5))
	fmt.Println("short test to check fuel cost between 14 and 5:", calcCost(14, 5))
}

func findPos(p []int, max int) {
	lowestCost := 1000000000
	bestPos := p[0]
	//for _, pos := range p { // oh wow- this was an actual bug, because 4 vs. 5 (I assumed pos must be in array)
	for pos := 0; pos <= max; pos++ {
		cost := 0

		for _, x := range p {
			cost = cost + calcCost(x, pos)
		}
		//fmt.Println("pos", pos, "cost", cost)

		if cost < lowestCost {
			lowestCost = cost
			bestPos = pos
		}
	}
	fmt.Println("lowestCost:", lowestCost, "best:", bestPos)
}

func calcCost(x int, y int) int {
	limit := Abs(x - y)
	cost := 0
	for i := 0; i < limit; i++ {
		cost = cost + i + 1
	}
	return cost
}

func oldCalcCost(x int, y int) int {
	return Abs(x - y)
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println(err)
		return -1
	} else {
		return i
	}
}

// There is no built-in abs function for integers, but it’s simple to write your own.
// https://yourbasic.org/golang/absolute-value-int-float/
// Abs returns the absolute value of x.
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

/*That's not the right answer; your answer is too high. If you're stuck, make sure
you're using the full input data; there are also some general tips on the about page,
or you can ask for hints on the subreddit. Please wait one minute before trying again.
(You guessed 92338199.) [Return to Day 7] */

/*Fri Feb 18 22:36:43 CET 2022
lowestCost: 92335207 best: 476
short test to check fuel cost between 16 and 5: 66
short test to check fuel cost between 14 and 5: 45

real	0m2.344s
user	0m2.420s
sys	0m0.206s */
