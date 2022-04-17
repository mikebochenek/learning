package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() { //https://adventofcode.com/2021/day/12
	fmt.Println("\t=> expected 1588, got: ", readProcess("day14-0"))
	fmt.Println("\t=> got: ", readProcess("day14-1"))
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

	for i := 0; i < 10; i++ {
		var newT string = ""
		for j := 1; j < len(t); j++ {
			key := t[j-1 : j+1]
			//fmt.Println("?", key, m[key])
			newT = newT + t[j-1:j] + m[key] // + t[j:j+1]
		}
		newT = newT + t[len(t)-1:len(t)]
		//fmt.Println ((i+1), t, newT)

		t = newT //evolution!!
	}

	//fmt.Println(len(t))

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	return mostLeastCommonDiff(t)

}

func mostLeastCommonDiff(s string) int {
	m := make(map[byte]int)
	for j := 1; j < len(s); j++ {
		m[s[j]] += 1
	}

	most := 0
	least := 10000000
	for _, v := range m {
		if most < v {
			most = v
		}
		if least > v {
			least = v
		}
	}

	//fmt.Println(m, most, least)
	return (most - least)
}
