package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fmt.Println("\n----> ", (13 == calc("2025_day4t.txt", 1)))
	fmt.Println("\n----> ", (1516 == calc("2025_day4.txt", 1)))
	fmt.Println("\n----> ", (43 == calc("2025_day4t.txt", 2)))
}

func calc(fn string, part int) int {
	f, err := os.Open("c:\\dev\\data\\aoc\\" + fn) 
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() 

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var lines []string

	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}
	c := 0
	for j := 0; j < len(lines); j+=1 {
		line := lines[j]
		for i := 0; i < len(line); i+= 1 {
			if (line[i] == '@') {
				n := 0
				if (j == 0 && i == 0) {
					c += 1
				} else if (j == 0 && i == len(line) - 1) {
					c += 1
				} else if (j == len(lines) - 1 && i == 0) {
					c += 1
				} else if (j == len(lines) - 1 && i == len(line) - 1) {
					c += 1
				} else if (j == 0) { // top line
					n += 3 
					if (line[i-1] == '.') { n += 1 } 
					if (line[i+1] == '.') { n += 1 } 
					nline := lines[j+1]
					if (nline[i-1] == '.') { n += 1 } 
					if (nline[i-0] == '.') { n += 1 } 
					if (nline[i+1] == '.') { n += 1 } 
				} else if (j == len(lines) - 1) { // bottom line}
					n += 3 
					if (line[i-1] == '.') { n += 1 } 
					if (line[i+1] == '.') { n += 1 } 
					pline := lines[j-1]
					if (pline[i-1] == '.') { n += 1 } 
					if (pline[i-0] == '.') { n += 1 } 
					if (pline[i+1] == '.') { n += 1 } 
				} else if (i == 0) { // left column

					n += 3 
					nline := lines[j+1]
					if (nline[i-0] == '.') { n += 1 } 
					if (nline[i+1] == '.') { n += 1 } 
					
					if (line[i+1] == '.') { n += 1 } 
					
					pline := lines[j-1]
					if (pline[i-0] == '.') { n += 1 } 
					if (pline[i+1] == '.') { n += 1 } 


				} else if (i == len(line) - 1) { // right column 

					n += 3 
					nline := lines[j+1]
					if (nline[i-1] == '.') { n += 1 } 
					if (nline[i-0] == '.') { n += 1 } 
					
					if (line[i-1] == '.') { n += 1 } 
					
					pline := lines[j-1]
					if (pline[i-1] == '.') { n += 1 } 
					if (pline[i-0] == '.') { n += 1 } 
					

				} else { // "regular case"
					nline := lines[j+1]
					if (nline[i-1] == '.') { n += 1 } 
					if (nline[i-0] == '.') { n += 1 } 
					if (nline[i+1] == '.') { n += 1 } 
					
					if (line[i-1] == '.') { n += 1 } 
					if (line[i+1] == '.') { n += 1 } 
					
					pline := lines[j-1]
					if (pline[i-1] == '.') { n += 1 } 
					if (pline[i-0] == '.') { n += 1 } 
					if (pline[i+1] == '.') { n += 1 } 

				}

				if (n > 4) {
					c += 1
				}
			}
		}
	}
	return c 
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}