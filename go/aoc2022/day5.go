package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day5-0.txt")
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

	fmt.Println("\n---> score: ", score)

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

type stack []rune // https://stackoverflow.com/questions/28541609/looking-for-reasonable-stack-implementation-in-golang

func (s stack) Push(v rune) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, rune) {
	if len(s) == 0 { //What do we do if the stack is empty, though?
		fmt.Println("empty stack!", s)
	}

	l := len(s)
	return s[:l-1], s[l-1]
}
