package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	f, err := os.Open("c:\\dev\\data\\aoc\\2025_day2t.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var nums []int
	invalid := 0
	nums = append(nums, 0) // how do you append again? https://linuxhint.com/array-append-golang/
	for scanner.Scan() {
		line := scanner.Text()
		products := strings.Split(line, ",")
		for j := 0; j < len(products); j+=1 {
			p := strings.Split(products[j], "-")
			fmt.Println(p[0], " vs. ", p[1])
			low := safeParse(p[0])
			high := safeParse(p[1])
			for i := low; i <= high; i+=1 {
				v := strconv.Itoa(i)
				//fmt.Println(len(v), v, v[:len(v)/2])
				x := v[:len(v)/2]
				if (strings.HasSuffix(v, x)) { // https://gobyexample.com/string-functions
					fmt.Println("invalid", p, x)
				}
			}
		}
	}
	fmt.Println("\n----> invalid:", invalid, nums)
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println("safeParse fails -> ", err)
		return -1
	} else {
		return i
	}
}