package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day9-0.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	const W = 5  //100
	const H = 10 //100
	lines := 0
	var m [W][H]int
	var lp [W][H]int
	for scanner.Scan() {
		line := scanner.Text()
		fmt.Println(line, len(line))
		for j := 0; j < len(line); j++ {
			x := safeParse(string(line[j]))
			m[lines][j] = x
		}
		lines = lines + 1
	}

	var totalRisk = 0
	for i := 0; i < W; i++ {
		for j := 0; j < H; j++ {
			val := m[i][j]
			if (i == 0 || m[i-1][j] > val) && // top adjacent
				(j == 0 || m[i][j-1] > val) && // left adjacent
				(j == (H-1) || m[i][j+1] > val) && // right adjacent
				(i == (W-1) || m[i+1][j] > val) { // bottom adjacent
				lp[i][j] = val + 1
				totalRisk = totalRisk + val + 1
			}
		}
	}

	// part II hints: 9 is the breaker, consider largest 3 basins (only)
	//fmt.Println(m)
	//fmt.Println(lp)
	fmt.Println("\n\tlines:", lines, "totalRisk:", totalRisk)

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
