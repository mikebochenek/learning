package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day15-0.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	const S = 10
	var nums [S][S]int
	count := 0
	if scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		for j := 0; j < len(line); j++ {
			nums[count][j] = safeParse(line[j])
		}
		count++
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
