package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() { //https://adventofcode.com/2021/day/12
	readProcess("day12-0")
	readProcess("day12-1")
	readProcess("day12-2")
	readProcess("day12")
}

func readProcess(filename string) int {
	fmt.Println("-->", filename)
	f, err := os.Open("/home/mike/Documents/aoc/" + filename + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	var words []string
	for scanner.Scan() {
		word := scanner.Text()
		words = append(words, word)
	}

	var startCaveText = ""
	for i := 0; i < len(words); i++ { // find one start node
		if strings.HasPrefix(words[i], "start-") {
			startCaveText = words[i]
		}
	}
	root := createCave(startCaveText)
	fmt.Println("\t root node:", root)

	// anyways, we probably need to handle duplicates and graph cycles..
	for i := 0; i < len(words); i++ {
		//TODO
		//Question: is building the tree struct the right approach?
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("total words:", len(words))
	return 0
}

func createCave(s string) Cave {
	var c Cave
	names := strings.Split(s, "-")
	c.name = names[0]

	var target Cave
	target.name = names[1]

	c.link = append(c.link, target)

	return c
}

type Cave struct {
	name    string
	visited bool
	link    []Cave
}
