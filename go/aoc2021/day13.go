package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

const SIZE = 16

func solve(filename string, size int) int {
	f, err := os.Open("/home/mike/Documents/aoc/" + filename + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	lines := 0
	var m [SIZE][SIZE]int //TODO resize
	var folds []string
	for scanner.Scan() {
		line := scanner.Text()
		//fmt.Println(line, len(line))
		if strings.HasPrefix(line, "fold along") {
			folds = append(folds, line)
		} else if len(line) > 1 {
			x := safeParse(strings.Split(line, ",")[0])
			y := safeParse(strings.Split(line, ",")[1])
			m[y][x] = 1
		}
		lines = lines + 1
	}

	for i := 0; i < len(folds); i++ {
		printNicely(m)
		fmt.Println(count(m), "after", folds[i])
	}

	fmt.Println("\n\tlines:", lines, "folds:", folds)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
	return count(m)
}

func main() {
	fmt.Println("solve gives", solve("day13-0", 12))
	//fmt.Println("solve gives", solve("day13-1", 2000))
}

func printNicely(m [SIZE][SIZE]int) {
	for i := 0; i < SIZE; i++ {
		fmt.Println(m[i])
	}
}

func count(m [SIZE][SIZE]int) int {
	count := 0
	for i := 0; i < SIZE; i++ {
		for j := 0; j < SIZE; j++ {
			if m[i][j] == 1 {
				count++
			}
		}
	}
	return count
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}
