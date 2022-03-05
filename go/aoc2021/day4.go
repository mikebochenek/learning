package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day4-1.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var nums []int
	if scanner.Scan() {
		line := strings.Split(scanner.Text(), ",")
		nums = make([]int, len(line))
		for j := 0; j < len(line); j++ {
			nums[j] = safeParse(line[j])
		}
	}

	const size = 500 //15
	var box[size/5]int
	var b [size][5]int
	var lines = 0
	for scanner.Scan() {
		line := scanner.Text()
		if len(line) > 0 && len(line) < 15 {
			lines = lines + 1
			words := strings.Split(strings.TrimSpace(strings.Replace(line, "  ", " ", -1)), " ")
			var n [5]int
			for j := 0; j < 5; j++ {
				n[j] = safeParse(words[j])
			}
			b[lines-1] = n
			//fmt.Println("at line:", lines, "parsed:", n)
		}
	}

	for j := 0; j < len(nums); j++ {

		for i := 0; i < size; i++ {
			for k := 0; k < 5; k++ {
				if b[i][k] == nums[j] {
					b[i][k] = -1
				}
			}
		}

		//check for horizontal match
		for i := 0; i < size; i++ {
			var hc = 0
			for k := 0; k < 5; k++ {
				if b[i][k] == -1 {
					hc = hc + 1
				}
			}
			if hc == 5 && box[i/5] == 0 {
				var sum = 0
				for x := (i / 5) * 5; x < (i/5)*5+5; x++ {
					for y := 0; y < 5; y++ {
						if b[x][y] > 0 {
							sum = sum + b[x][y]
							//fmt.Println(b[x][y])
						}
					}
				}
				//fmt.Println(b)

				fmt.Println("lastnum:", nums[j], "sum:", sum, "box:", i/5, " -->", (nums[j] * sum))
				//os.Exit(0)
				box[i/5] = 1
			}
		}

		//check for vertical match (cut and paste from horizontal, and modify first 2 for loops)
		for i := 0; i < size; i++ { // i+=5
			var vc = 0
			for k := 0; k < 5; k++ {
				//if b[i][k] == -1 {
				// b[(i/5)*5+k][(i%(k+1))] == -1 {
				if b[(i/5)*5+k][(i%5)] == -1 {
					vc = vc + 1
				}
			}
			if vc == 5 && box[i/5] == 0 {
				var sum = 0 // sum calculation stays exactly the same...
				for x := (i / 5) * 5; x < (i/5)*5+5; x++ {
					for y := 0; y < 5; y++ {
						if b[x][y] > 0 {
							sum = sum + b[x][y]
							//fmt.Println(b[x][y])
						}
					}
				}
				//fmt.Println(b)

				fmt.Println("lastnum:", nums[j], "sum:", sum, "box:", i/5, " -->", (nums[j] * sum))
				//os.Exit(0)
				box[i/5] = 1
			}
		}

	}

	//fmt.Println(b)

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
