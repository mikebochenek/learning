package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	f, err := os.Open("/tmp/input.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	hPos := 0
	depth := 0
	aim := 0
	cmd := ""
	for scanner.Scan() {
		word := scanner.Text()

		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			cmd = word
		} else {
			if cmd == "down" { //down increases depth
				aim = aim + x
			}
			if cmd == "up" { //up decreases depth
				aim = aim - x
			}
			if cmd == "forward" { //forward increases hPos
				hPos = hPos + x
				depth = depth + aim*x
			}
			fmt.Println(x, cmd, "  ---- ", depth, hPos, aim)
		}

		//fmt.Println(word)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println(depth, hPos, (depth * hPos))
}

func main_part1() {
	f, err := os.Open("/tmp/input.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	hPos := 0
	depth := 0
	cmd := ""
	for scanner.Scan() {
		word := scanner.Text()

		x, err := strconv.Atoi(scanner.Text())
		if err != nil {
			cmd = word
		} else {
			if cmd == "down" { //down increases depth
				depth = depth + x
			}
			if cmd == "up" { //up decreases depth
				depth = depth - x
			}
			if cmd == "forward" { //forward increases hPos
				hPos = hPos + x
			}
			fmt.Println(x, cmd)
		}

		//fmt.Println(word)
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	fmt.Println(depth, hPos, (depth * hPos))
}
