package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
)

func main() {
	f, err := os.Open("c:\\dev\\data\\aoc\\2025_day4.txt")
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