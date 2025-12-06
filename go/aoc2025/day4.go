package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	fmt.Println("\n----> ", (13 == calc("2025_day4t.txt", 1)))
	fmt.Println("\n----> ", (1516 == calc("2025_day4.txt", 1)))
	fmt.Println("\n----> ", (43 == calc("2025_day4t.txt", 2)))
	fmt.Println("\n----> ", (9122 == calc("2025_day4.txt", 2)))
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
	
	count := 0

	for k := 0; k < 10000; k+=1 { // 9110 is too low Sat 10:27

	c := 0

	for j := 0; j < len(lines); j+=1 {
		line := lines[j]
		for i := 0; i < len(line); i+= 1 {
			if (line[i] == '@') {
				n := 0
				if (j == 0 && i == 0) { //&& part == 1) {
					if (k % 2 == 0) {
						c += 1
						lines[j] = string(append(append([]rune(lines[j][:i]), 'x'), []rune(lines[j][(i+1):])...))
					}
				} else if (j == 0 && i == len(line) - 1) {
					if (k % 2 == 0) {
						c += 1
						lines[j] = string(append(append([]rune(lines[j][:i]), 'x'), []rune(lines[j][(i+1):])...))
					}
				} else if (j == len(lines) - 1 && i == 0) {
					if (k % 2 == 0) {
						c += 1
						lines[j] = string(append(append([]rune(lines[j][:i]), 'x'), []rune(lines[j][(i+1):])...))
					}
				} else if (j == len(lines) - 1 && i == len(line) - 1) {
					if (k % 2 == 0) {
						c += 1 
						lines[j] = string(append(append([]rune(lines[j][:i]), 'x'), []rune(lines[j][(i+1):])...))
					}
				} else if (j == 0) { // top line
					n += 3 
					//fmt.Println(i, j, line) 
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
					if (k % 2 == 0) {
						c += 1
					} else {
						if (part == 2) {
							// this is OK, except for the corners..


							// hmm... can I immediately replace?
							//rep := append(append([]rune(line[:i]), '.'), []rune(line[(i+1):])...) 
							rep := append(append([]rune(lines[j][:i]), 'x'), []rune(lines[j][(i+1):])...)
							//fmt.Println("j=", j, "i=", i, "replace", lines[j], string(rep))
							lines[j] = string(rep)
							// learning\go\aoc2025\day4.go:119:8: cannot assign to lines[j][i] (neither addressable nor a map index expression)
							// https://go.dev/play/p/xozL-Ufcbk6
							// Universitätstrasse 101, 8006 Zürich
						}
					}
				}
			}
		}
	}

	//fmt.Println("removing", c)

	for j := 0; j < len(lines); j+=1 {
		lines[j] = strings.Replace(lines[j], "x", ".", -1) // really remove here!

		//fmt.Println(k, "\t\t", lines[j])
	}

	count += c

	if ((k % 2 == 0 && c <= 0) || part == 1) {
		break;
	}


	} // note benne...

	fmt.Println(part, fn, "about to return count", count)

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