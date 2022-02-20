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
		fmt.Println("\ttest after 80 days?:", 5934 == smartSimulate(pos, 80))
		fmt.Println("\ttest after 18 days?:", 26 == smartSimulate(pos, 18))
		fmt.Println("\ttest after 18 days?:", 26 == simulate(pos, 18)) // old simulate destroys input array!
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func smartSimulate(p []int, days int) int {
	counts := [10]int{0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
	for j := 0; j < len(p); j++ {
		counts[p[j]] = counts[p[j]] + 1
	}
	total := sumup(counts)
	fmt.Println("Initial state:", p, "\t*len:", total, "\t", counts)

	for i := 0; i < days; i++ {
		counts[9] = counts[0]             // new fish
		counts[6] = counts[6] + counts[0] // respawn parent
		for j := 0; j < 9; j++ {
			counts[j] = counts[j+1]
		}

		total = sumup(counts)
		fmt.Println("after day", (i + 1), "\t\t\t len:", total, "\t", counts)
	}
	fmt.Println("after", days, "there are", total)
	return total
}

func sumup(p [10]int) int {
	total := 0
	for j := 0; j < len(p); j++ {
		total = total + p[j]
	}
	return total
}

func simulate(p []int, days int) int {
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
		fmt.Println("after day", (i + 1), p, "\tlen:", len(p))
	}
	fmt.Println("after", days, "there are", len(p))
	return len(p)
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
