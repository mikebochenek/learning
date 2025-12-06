package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"time"
)

func main() {
	now := time.Now()
	fmt.Println("\n\n*** ", now)
	fmt.Println("\t----> ", 3 == calc("2025_day5t.txt", 1))
	fmt.Println("\t----> ", 739 == calc("2025_day5.txt", 1))
	fmt.Println("\t----> ", 14 == calc("2025_day5t.txt", 2))
	fmt.Println("\t----> ", 14 == calc("2025_day5.txt", 2))
}

func calc(fn string, part int) int {
	f, err := os.Open("c:\\dev\\data\\aoc\\" + fn) 
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() 

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var ids []int
	var from [] int
	var to [] int
	for scanner.Scan() {
		line := scanner.Text()
		//fmt.Println(line)
		p := strings.Split(line, "-")
		if (len(line) >= 1) {
			if (strings.Contains(line, "-")) {
				from = append(from, safeParse(p[0]))
				to = append(to, safeParse(p[1]))
			} else {
				ids = append(ids, safeParse(line)) 
			}
		}
	}

	//fmt.Println(from, to, ids)

	count := 0
	for j := 0; j < len(ids); j+=1 {
		found := false
		for i := 0; i < len(from) && found == false; i+= 1 {
			if (ids[j] >= from[i]) {
				if (ids[j] <= to[i]) {
					//fmt.Println("fresh", ids[j], from[i], to[i])
					count += 1
					found = true
				}
			}
		}
	}

	if (part == 2) {
		var eFrom [] int
		var eTo [] int // extended/for answer purpose

		minFrom := 0
		maxTo := 0

		for i := 0; i < len(from); i+= 1 {

			if (i == 0) {
				eFrom = append(eFrom, from[i])
				eTo = append(eTo, to[i])
				minFrom = from[i]
				maxTo = to[i]
			}

			if (from[i] < minFrom) {
				minFrom = from[i]
			}
			if (to[i] > maxTo) {
				maxTo = to[i]
			}


			// check for overlaps, and add to extended from/to
			// hmm... but won't merging be a big mess?!
		}

		fmt.Println(eFrom, eTo, minFrom, maxTo, "dif", (maxTo-minFrom))

		for i := 0; i < len(eFrom); i+= 1 {

		}
	}

	fmt.Println("part I/II:  will return", count, "for", fn)
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