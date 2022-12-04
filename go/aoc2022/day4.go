package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day4-1.txt")
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
		sections := strings.Split(lines[j], ",")
		s1str := strings.Split(sections[0], "-")
		s2str := strings.Split(sections[1], "-")
		var s1 [2]int
		s1[0] = safeParse(s1str[0])
		s1[1] = safeParse(s1str[1])

		var s2 [2]int
		s2[0] = safeParse(s2str[0])
		s2[1] = safeParse(s2str[1])

		if (s1[0] >= s2[0] && s1[0] <= s2[1] && s1[1] >= s2[0] && s1[1] <= s2[1]) {
			score += 1
			fmt.Println(" yes1 ", s1, s2)
		} else if (s2[0] >= s1[0] && s2[0] <= s1[1] && s2[1] >= s1[0] && s2[1] <= s1[1]) {
			score += 1
			fmt.Println(" yes2 ", s1, s2)
		} else {
			fmt.Println(" no   ", s1, s2)
		}
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