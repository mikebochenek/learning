package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	fmt.Println("\t----> ", 3 == calc("2025_day5t.txt", 1))
	fmt.Println("\t----> ", 739 == calc("2025_day5.txt", 1))
	fmt.Println("\nPART II")
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

	m := make(map[int]bool)

	if (part == 2) {
		for i := 0; i < len(from); i+=1 {
			for j := from[i]; j <= to[i]; j+=1 {
				m[j] = true
			}
		}
	}
	


	if part == 1 {
		fmt.Println("part I:  will return", m, "for", fn)
		return count
	} else {
		fmt.Println("part II: will return", len(m), "for", fn)
		return len(m)
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