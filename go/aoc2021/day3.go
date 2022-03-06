package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	const size = 1000
	f, err := os.Open("/home/mike/Documents/aoc/day3-1.txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	var count1s [size]int
	var count0s [size]int
	var words [size]string
	var lines = 0
	for scanner.Scan() {
		word := scanner.Text()
		words[lines] = word
		for i := 0; i < len(word); i++ {
			if word[i] == '0' {
				count0s[i] = count0s[i] + 1
			}
			if word[i] == '1' {
				count1s[i] = count1s[i] + 1
			}
		}
		lines = lines + 1
		//fmt.Println(count1s, count0s, lines)
	}

	fmt.Println(count1s, count0s, lines, words)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	digits := 0
	gamma := ""
	epsilon := ""
	for i := 0; i < size; i++ {
		if count1s[i] > 0 && count0s[i] > 0 {
			digits++

			if count1s[i] > count0s[i] {
				gamma = gamma + "1"
				epsilon = epsilon + "0"
			} else {
				gamma = gamma + "0"
				epsilon = epsilon + "1"
			}

		}
	}

	var gammaVal = myConvert(gamma)
	var epsilonVal = myConvert(epsilon)

	fmt.Println("\t==> digits:", digits, "gamma:", gamma, "epsilon:", epsilon, "product:", gammaVal*epsilonVal, "lines:", lines)

	//clone words array!
	var words2 [size]string
	for i := 0; i < size; i++ {
		words2[i] = words[i]
	}

	// Part II
	var c = ""
	for i := 0; i < digits; i++ {
		var common = '1'
		c1s := 0
		c0s := 0
		for j := 0; j < size; j++ {
			if words[j] != "00000" && words[j] != "" {
				if words[j][i] == '0' {
					c0s++
				} else {
					c1s++
				}
			}
		}
		if c1s < c0s {
			common = '0'
		}
		if c1s == c0s {
			fmt.Println("tie breaker needed at ", i)
		}

		for j := 0; j < size; j++ {
			if words[j] == "00000" || words[j] == "" {

			} else {
				c = words[j]
				if words[j][i] != byte(common) {
					words[j] = ""
				}
			}
		}
		fmt.Println("\n\n", i, words)
	}
	//fmt.Println(c)
	ogr := c

	//TODO am I missing the tie-braker..?

	words = words2
	for i := 0; i < digits; i++ {
		var common = '0'
		c1s := 0
		c0s := 0
		for j := 0; j < size; j++ {
			if words[j] != "00000" && words[j] != "" {
				if words[j][i] == '0' {
					c0s++
				} else {
					c1s++
				}
			}
		}
		if c1s < c0s {
			common = '1'
		}
		if c1s == c0s {
			fmt.Println("tie breaker needed at ", i)
		}

		for j := 0; j < size; j++ {
			if words[j] == "00000" || words[j] == "" {

			} else {
				c = words[j]
				if words[j][i] != byte(common) {
					words[j] = ""
				}
			}
		}
		fmt.Println("\n\n", i, words)
	}
	//fmt.Println(c)
	csr := c

	fmt.Println("\t--> oxygen generator rating:", ogr, "CO2 scrubber rating:", csr)
	ogrV := myConvert(ogr)
	csrV := myConvert(csr)
	fmt.Println("\t--> ogrV:", ogrV, ogr, "csrV:", csrV, csr, "product:", (ogrV * csrV))
}

func myConvert(e string) int64 {
	if i, err := strconv.ParseInt(e, 2, 64); err != nil {
		fmt.Println(err)
		return -1
	} else {
		return i
	}
}
