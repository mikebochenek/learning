package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
	"time"
)
func main() {
	now := time.Now()
	fmt.Println(now, "\n----> ", (4277556 == calc("2025_day6t.txt", 1)))
	fmt.Println("\n----> ", (6299564383938 == calc("2025_day6.txt", 1)))
	//fmt.Println("\n----> ", (43 == calc("2025_day4t.txt", 2)))
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

	lastLine := lines[len(lines) - 1]
	ops := removeBlanks(strings.Split(lastLine, " "))
	//fmt.Println("\t\tops=", len(ops))

	var nums[] string
	for j := 0; j < len(lines)-1; j+=1 {
		line := lines[j]
		//fmt.Println(line)
		nums = removeBlanks(append(nums, line))
	}

	for i := 0; i < len(ops); i+=1 {
		total := 0
		for j := 0; j < len(lines)-1; j+=1 {
			line := lines[j]
			numbers := removeBlanks(strings.Split(line, " "))
			v := safeParse(numbers[i])
			if (ops[i] == "+") {
				//fmt.Println("add", v)
				total += v
			}
			if (ops[i] == "*") {
				if total == 0 {
					total = 1
				}
				//fmt.Println("multiply", v)
				total *= v
			}
		}
		count += total
	}

	fmt.Println(part, fn, "about to return", count)
	return count 
}

func removeBlanks(s []string) []string {
	var v []string
	for i := 0; i < len(s); i++ {
		if s[i] != "" && len(s) > 0 {
			v = append(v, s[i])
		} else {
			//fmt.Println("removing:", s[i], ":")
		}
	}
	return v
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}