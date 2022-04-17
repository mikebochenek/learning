package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

const FILENAME = "day10-1"
const size = 90

func main() {
	f, err := os.Open("/home/mike/Documents/aoc/" + FILENAME + ".txt")
	if err != nil {
		fmt.Println(err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	scanner.Split(bufio.ScanWords)

	var lines = 0
	var total = 0
	var words [size]string
	var scores []int
	for scanner.Scan() {
		word := scanner.Text()
		s := score(word)
		//fmt.Println("\t", word, s)
		if s < 0 { // or <= 0
			words[lines] = word
			lines++
			total += s * -1
			scores = append(scores, s*-1)
		} else {
			//essentially discard
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println(err)
	}

	//fmt.Println(len(words), words)
	sort.Ints(scores)
	fmt.Println(len(scores), scores)
	fmt.Println("\t middle score", scores[len(scores)/2])
	fmt.Println("\tlines:", lines, len(words), "\tTOTAL:", total)
}

/*
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
*/
func autocomplete(w string) int {
	if w == ")" {
		return 1
	} else if w == "]" {
		return 2
	} else if w == "}" {
		return 3
	} else if w == ">" {
		return 4
	}
	return 0
}

func score(w string) int {
	var s = make(stack, 0)
	var v int
	for i := 0; i < len(w); i++ {
		if w[i] == '(' {
			s = s.Push(3)
		} else if w[i] == '[' {
			s = s.Push(57)
		} else if w[i] == '{' {
			s = s.Push(1197)
		} else if w[i] == '<' {
			s = s.Push(25137)

		} else if w[i] == ')' {
			s, v = s.Pop()
			if v != 3 {
				//suggest here?! fmt.Println(s, v, i)
				return penalize(w[i])
			}
		} else if w[i] == ']' {
			s, v = s.Pop()
			if v != 57 {
				//fmt.Println(s, v, i)
				return penalize(w[i])
			}
		} else if w[i] == '}' {
			s, v = s.Pop()
			if v != 1197 {
				//fmt.Println(s, v, i)
				return penalize(w[i])
			}
		} else if w[i] == '>' {
			s, v = s.Pop()
			if v != 25137 {
				//fmt.Println(s, v, i)
				return penalize(w[i])
			}
		}

	}
	//fmt.Println("\t\t", s, len(s))

	var total = 0
	max := len(s)
	for i := 0; i < max; i++ {
		total = total * 5
		s, v = s.Pop()
		total = total + translate(v)
		//fmt.Println(" - ", total, v, translate(v))
	}
	//fmt.Println("\t\t\t\t", total)

	return -1 * total
}

/*
): 1 point.
]: 2 points.
}: 3 points.
>: 4 points.
*/
func translate(i int) int {
	if i == 3 {
		return 1
	}
	if i == 57 {
		return 2
	}
	if i == 1197 {
		return 3
	}
	if i == 25137 {
		return 4
	}
	return 0
}

/*
): 3 points.
]: 57 points.
}: 1197 points.
>: 25137 points.
*/
func penalize(c byte) int {
	//fmt.Println("expected, but got", string(c))
	if c == ')' {
		return 3
	} else if c == ']' {
		return 57
	} else if c == '}' {
		return 1197
	} else if c == '>' {
		return 25137
	} else {
		return 100000
	}
}

type stack []int // https://stackoverflow.com/questions/28541609/looking-for-reasonable-stack-implementation-in-golang

func (s stack) Push(v int) stack {
	return append(s, v)
}

func (s stack) Pop() (stack, int) {
	if len(s) == 0 { //What do we do if the stack is empty, though?
		fmt.Println("empty stack!", s)
	}

	l := len(s)
	return s[:l-1], s[l-1]
}
