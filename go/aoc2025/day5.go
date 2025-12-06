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

		count = 0
		for i := 0; i < len(from); i+= 1 {

			//fmt.Println(i)

			dif := to[i] - from[i] + 1

			if (dif <= 1) {
				fmt.Println(from[i], to[i], dif, " ? ")
			} //.... but sometimes diff=1 (meaning range is x to x...? )

			// check for overlaps,
			//  j := i !!! 
			for j := (i+1); j < len(from); j+= 1 {
				//fmt.Println(from[i], to[i], " vs.", from[j], to[j])
				if (from[j] <= from[i] && to[j] <= to[i] && to[j] >= from[i]) {
					dd := (to[j]-from[i]+1)
					fmt.Println("! case 1:", dd)
					dif -= dd
				} else if (to[j] >= to[i] && from[j] <= to[i] && from[j] >= from[i]) {
					dd := (to[i] - from[j]+1)
					fmt.Println("! case 2:", dd)
					dif -= (dd)
				} else if (from[j] <= from[i] && to[j] >= to[i]) {
					dd := (to[i] - from[i]+1)
					fmt.Println("! case 3:", dd)
					dif -= (dd)					
				} else if (from[j] >= from[i] && to[j] <= to[i]) {
					dd := (to[j] - from[j]+1)
					fmt.Println("! case 4:", dd)
					dif -= dd
				}
				// what about exact duplicates? shouldn't it be <= and >=  ?
			}

			if (dif > 1) {
				count += dif
			}

			// fmt.Println("dif", dif)
		}

		//390437132487557 too high 18:34 
		//392203548664963 would also be too high 19:01 :-( 
		//342954507009352 is too low 19:08
		//343735797336618 is too low 19:11
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