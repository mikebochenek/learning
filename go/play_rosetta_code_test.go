package main

import "testing"

func fib(a int) int {
	if a < 2 {
		return a
	}
	return fib(a-1) + fib(a-2)
}

/** Iterative using a closure - https://rosettacode.org/wiki/Fibonacci_sequence#Iterative_24 */
func fibNumber() func() int {
	fib1, fib2 := 0, 1
	return func() int {
		fib1, fib2 = fib2, fib1+fib2
		return fib1
	}
}

func fibSequence(n int) int {
	f := fibNumber()
	fib := 0
	for i := 0; i < n; i++ {
		fib = f()
	}
	return fib
}

func TestFib(t *testing.T) {
	if x := fib(5); x != 5 {
		t.Errorf("fib(5) should be 5, but got %v", x)
	}
	if x := fibSequence(12); x != 144 {
		t.Errorf("fibSequence(12) should be 144, but got %v", x)
	}
}
