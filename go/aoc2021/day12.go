package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() { //https://adventofcode.com/2021/day/12
	fmt.Println("\t=> expected 10, got: ", readProcess("day12-0"))
	fmt.Println("\t=> expected 19, got: ", readProcess("day12-1"))
	fmt.Println("\t=> expected 226, got: ", readProcess("day12-2"))
	fmt.Println("\t=> actual puzzle: ", readProcess("day12"))
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
	var paths = 0

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
		//TODO + Question: is building the tree struct the right approach?
		if words[i] != startCaveText { // skip duplicate
			fmt.Println("outer for loop with", i, words[i])
			addCave(words[i], root)
		}
	}

	//TODO print all possible paths starting at root node

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println("total words:", len(words))
	return paths
}

func addCave(s string, r Cave) Cave {
	//var c Cave
	fmt.Println("... adding cave:", s)
	names := strings.Split(s, "-")
	if r.name == names[0] {
		var target Cave
		target.name = names[1]
		target.link = append(target.link, r) // backlink?
		r.link = append(r.link, target)
		fmt.Println("\t ... really appending! ", s, "node:", r.name, len(r.link), "-->", r.link)

	} else {
		for i := 0; i < len(r.link); i++ {
			fmt.Println("\t\t ... trying", r.link[i].name)
			return addCave(s, r.link[i])
		}
	}
	return r
}

func createCave(s string) Cave {
	var c Cave
	names := strings.Split(s, "-")
	c.name = names[0]

	var target Cave
	target.name = names[1]
	target.link = append(target.link, c) // backlink?

	c.link = append(c.link, target)

	return c
}

type Cave struct {
	name string
	//parent	*Cave //do I even need? https://stackoverflow.com/questions/8261058/invalid-recursive-type-in-a-struct-in-go
	//visited bool
	link []Cave
}
