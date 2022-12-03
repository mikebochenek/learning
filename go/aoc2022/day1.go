package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"sort"
)

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/day1-0.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var nums []int
	nums = append(nums, 0) // how do you append again? https://linuxhint.com/array-append-golang/
	for scanner.Scan() {
		line := scanner.Text()
		calories := safeParse(line)

		if (calories == -1) {
			nums = append(nums, 0)
		} else {
			idx := len(nums)-1
			nums[idx] = nums[idx] + calories
		}
	}

	sort.Sort(sort.IntSlice(nums)) // how to sort again? https://stackoverflow.com/questions/37695209/golang-sort-slice-ascending-or-descending
	ns := len(nums)-1
	max := nums[ns]
	/* for i := 0; i < len(nums); i++ {
		if (nums[i] >= max) { 
			max = nums[i]
		}
	} */
	max3 := nums[ns] + nums[ns-1] + nums[ns-2]

	fmt.Println(nums)
	fmt.Println("\n----> total elfs:", len(nums), " max:", max, " top3 max", max3)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
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