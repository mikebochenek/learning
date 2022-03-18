package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const SIZE = 10
const FILENAME = "day11-1"

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
		//fmt.Println(line, len(line))
		for j := 0; j < len(line); j++ {
			x := safeParse(string(line[j]))
			m[lines][j] = x
		}
		lines = lines + 1
	}

	var flash = 0

	for i := 0; i <= 100; i++ {
		fmt.Println("\nafter step", i, "flashes:", flash)
		//printNicely(m)

		for j := 0; j < SIZE; j++ {
			for k := 0; k < SIZE; k++ {
				m[j][k]++
			}
		}

		for n := 0; n < 40; n++ {
			for j := 0; j < SIZE; j++ {
				for k := 0; k < SIZE; k++ {
					if m[j][k] > 9 {

						flash += 1
						m[j][k] = -100

						if j > 0 && k > 0 && m[j-1][k-1] != 0 {
							m[j-1][k-1]++
						}
						if j > 0 && m[j-1][k] != 0 {
							m[j-1][k]++
						}
						if j > 0 && (k+1) < SIZE && m[j-1][k+1] != 0 {
							m[j-1][k+1]++
						}

						if k > 0 && m[j][k-1] != 0 {
							m[j][k-1]++
						}
						if (k+1) < SIZE && m[j][k+1] != 0 {
							m[j][k+1]++
						}

						if (j+1) < SIZE && k > 0 && m[j+1][k-1] != 0 {
							m[j+1][k-1]++
						}
						if (j+1) < SIZE && m[j+1][k] != 0 {
							m[j+1][k]++
						}
						if (j+1) < SIZE && (k+1) < SIZE && m[j+1][k+1] != 0 {
							m[j+1][k+1]++
						}

					}
				}
			}
		}

		for j := 0; j < SIZE; j++ {
			for k := 0; k < SIZE; k++ {
				if m[j][k] < 0 {
					m[j][k] = 0
				}
			}
		}
	}

	//this was causing me pain!! fmt.Println("\n\tflashes", flash)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func printNicely(m [SIZE][SIZE]int) {
	for i := 0; i < SIZE; i++ {
		fmt.Println(m[i])
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
