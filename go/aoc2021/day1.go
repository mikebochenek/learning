package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("/tmp/input.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	ints, err := ReadInts(f)

	count := countSlidingWindowIncreases(ints)

	fmt.Println(ints, err, count)
}

// part one - count the increases
func countIncreases(integers []int) int {
	count := 0
	for j, i := range integers {
		if j > 0 && i > integers[j-1] { // check if current number is larger than previous (i.e. increases)
			count = count + 1
		}
	}
	return count
}

// part two - "count the number of times the sum of measurements in this sliding window increases" (size=3)
func countSlidingWindowIncreases(integers []int) int {
	count := 0
	windowSize := 3
	for i := 1; i <= len(integers)-windowSize; i++ {
		prev := integers[i-1] + integers[i] + integers[i+1]
		curr := integers[i] + integers[i+1] + integers[i+2]
		// I guess it could be enough to compare integers[i-1] < integers[i+2]
		if prev < curr {
			count = count + 1
		}
	}
	return count
}

// ReadInts reads whitespace-separated ints from r. If there's an error, it
// returns the ints successfully read so far as well as the error value.
// https://stackoverflow.com/questions/9862443/golang-is-there-a-better-way-read-a-file-of-integers-into-an-array
func ReadInts(r io.Reader) ([]int, error) {
	scanner := bufio.NewScanner(r)
	scanner.Split(bufio.ScanWords)
	var result []int
	for scanner.Scan() {
		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return result, err
		}
		result = append(result, x)
	}
	return result, scanner.Err()
}
