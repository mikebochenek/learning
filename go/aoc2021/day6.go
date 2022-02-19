package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/day6-0.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	if scanner.Scan() {
		word := scanner.Text()
		numbers := strings.Split(word, ",")
		pos := make([]int, len(numbers))
		for i, number := range numbers {
			pos[i] = safeParse(number)
		}
		simulate(pos, 80)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func simulate(p []int, days int) {

	fmt.Println("Initial state:", p, "\tlen:", len(p))

	for i := 0; i < days; i++ {
		for j := 0; j < len(p); j++ {
			if p[j] == 0 {
				p[j] = 6
				p = append(p, 9) // strangely 9 added, not 8 - also neat: https://yourbasic.org/golang/append-explained/
			} else {
				p[j] = p[j] - 1
			}
		}
		//fmt.Println("after day", (i+1), p, "\tlen:", len(p))
	}

	fmt.Println("after", days, "there are", len(p))
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println(err)
		return -1
	} else {
		return i
	}
}

/* Sat Feb 19 08:40:06 CET 2022
Part I: after 80 there are 345387

real	0m0.624s
user	0m0.743s
sys	0m0.184s

switching to 256 days gives me:
fatal error: runtime: out of memory
*/
