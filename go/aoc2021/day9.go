package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const W = 5  //100
const H = 10 //100
const FILENAME = "day9-0"

func main() {
	//	lines: 100 lowPoint: 221 totalRisk: 504
	f, err := os.Open("/home/mike/Documents/aoc/" + FILENAME + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

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

	var lowPoint = 0
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
				lowPoint++
			}
		}
	}
	//fmt.Println(m)
	//fmt.Println(lp)

	// part II hints: 9 is the breaker, consider largest 3 basins (only)
	var a, b, c = 0, 0, 0
	for i := 0; i < W; i++ {
		for j := 0; j < H; j++ {
			if lp[i][j] > 0 {
				newBasin := basin(lp, m, i, j)
				if newBasin > a {
					if newBasin > b && newBasin < c {

					} else if newBasin > c {

					} else {
						a = newBasin
					}
				}
			}
		}
	}

	fmt.Println("\n\tlines:", lines, "lowPoint:", lowPoint, "totalRisk:", totalRisk, "basins:", a, b, c)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func basin(lp [W][H]int, m [W][H]int, i int, j int) int {
	var tmp [W][H]int
	tmp[0][0] = 0
	fmt.Println("\t-> here", i, j)
	return 1
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}
