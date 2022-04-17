package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() { //https://adventofcode.com/2021/day/12
	fmt.Println("\t=> expected 1588, got: ", readProcess("day14-0"))
	fmt.Println("\t=> expected 4517, got: ", readProcess("day14-1"))
}

func readProcess(filename string) int {
	fmt.Println("-->", filename)
	f, err := os.Open("/home/mike/Documents/aoc/" + filename + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	m := make(map[string]string)

	scanner.Scan()
	var t string = scanner.Text()

	for scanner.Scan() {
		word := scanner.Text()
		if len(word) > 1 {
			s := strings.Split(word, " -> ")
			//fmt.Println(s)
			m[s[0]] = s[1]
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	return runEvolutions(m, t)
}

func runEvolutions(m map[string]string, t string) int {
	c := make(map[byte]int)
	mc := make(map[string]int)

	for j := 1; j < len(t); j++ { //init
		key := t[j-1 : j+1]
		mc[key]++
		c[t[j]]++
	}
	c[t[0]]++

	for i := 0; i < 40; i++ {
		newmc := make(map[string]int)

		for k, v := range mc {
			child := m[k]
			dad := k[0:1] + child
			mom := child + k[1:2]
			//fmt.Println(i, k,v, dad, mom)

			if v > 0 {
				//fmt.Println("increasing ", mom[0], v)
				c[mom[0]] = c[mom[0]] + v
				newmc[mom] = newmc[mom] + v
				newmc[dad] = newmc[dad] + v
			}
		}

		mc = newmc
		//fmt.Println("\t*", i+1, mc, c)
	}

	most := 0
	least := 9223372036854775807 //https://stackoverflow.com/questions/6878590/the-maximum-value-for-an-int-type-in-go
	total := 0
	for _, v := range c {
		if most < v {
			most = v
		}
		if least > v {
			least = v
		}
		total += v
	}

	fmt.Println("\t\t\t", "most:", most, "least:", least, "total:", total)
	return (most - least)
}
