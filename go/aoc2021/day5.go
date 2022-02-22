package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	f, err := os.Open("/home/mike/Documents/day5-0.txt") // open file
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close() // remember to close the file at the end of the program

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanLines)

	var lines = 0
	const size = 10  //00
	var p1 [size][]string
	var p2 [size][]string
	for scanner.Scan() {
		line := scanner.Text()
		points := strings.Split(line, " -> ")
		p1[lines] = strings.Split(points[0], ",")
		p2[lines] = strings.Split(points[1], ",")
		lines = lines + 1
		//fmt.Println(lines, p1, p2)
	}

	var matrix [size][size]int

	for i := 0; i < size; i++ {
		if p1[i] != nil && p2[i] != nil {
			fmt.Println(p1[i], p2[i])
			p1x := safeParse(p1[i][0])
			p1y := safeParse(p1[i][1])
			p2x := safeParse(p2[i][0])
			p2y := safeParse(p2[i][1])

			startY := p1y
			endY := p2y
			if p2y < p1y {
				startY = p2y
				endY = p1y
			}

			startX := p1x
			endX := p2x
			if p2x < p1x {
				startX = p2x
				endX = p1x
			}

			if p1x == p2x { // vertical
				//fmt.Println("vertical at x", p1x, startY, endY)
				for j := startY; j <= endY; j++ {
					matrix[j][p1x] = matrix[j][p1x] + 1
				}
			} else if p1y == p2y { // horizontal
				//fmt.Println("horizontal at y", p1y, startX, endX)
				for j := startX; j <= endX; j++ {
					matrix[p1y][j] = matrix[p1y][j] + 1
				}
			} else if (p1x > p2x) { // diagonal -  
				fmt.Println("\t\tdiagonal_A y", startY, endY, " x", startX, endX)
				for j := startX; j <= endX; j++ {
					matrix[startY+j-startX][j] = matrix[startY+j-startX][j] + 1
				}
			} else if (p1x < p2x) { // diagonal -  
				fmt.Println("\t\tdiagonal_B y", startY, endY, " x", startX, endX)
				for j := startX; j <= endX; j++ {
					//matrix[j][startY+j-startX] = matrix[j][startY+j-startX] + 1
					//matrix[startX+j-startY][j] = matrix[startX+j-startY][j] + 1
				}
			}
		}
	}

	count := 0
	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			if matrix[i][j] > 1 { //== maxOverlap) {
				count = count + 1
			}
		}
		fmt.Println(matrix[i])
	}

	fmt.Println("count:", count, "maxOverlap:", 2)

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}
}

func safeParse(g string) int {
	if i, err := strconv.Atoi(g); err != nil {
		fmt.Println(err)
		return -1
	} else {
		return i
	}
}
