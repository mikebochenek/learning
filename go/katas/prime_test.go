package main

import (
	"testing"
)

/**
 * page 165 of Discrete Mathematics and Its Applications by Kenneth H. Rosen
 * programming question #4:  find as many primes as possible of the form n^2 + 1
 */
func TestN2PlusOnePrime(t *testing.T) {
	max := 100
	for i := 1; i < max; i += 1 {
		n := i*i + 1
		isPrime := prime(n)
		if isPrime {
			//fmt.Println("is it prime?", isPrime, i, n)
		}
	}
}

/**
 * page 165 of Discrete Mathematics and Its Applications by Kenneth H. Rosen
 * programming question #3:
 * show that n^2 + n + 41 is prime for 0 <= n <= 39
 * (and not for n=40)
 */
func TestN2PlusNPlus41Prime(t *testing.T) {
	max := 100
	for i := 1; i <= max; i += 1 {
		n := i*i + i + 41
		isPrime := prime(n)

		if !isPrime {
			t.Errorf("prime(%v) should true, but got %v (i=%v)", n, isPrime, i)
		}

		//fmt.Println("is prime?", isPrime, i, n)
	}
}

/**
 * page 164 of Discrete Mathematics and Its Applications by Kenneth H. Rosen
 * question #6. Given a positive integer, determine whether it is prime.
 */
func prime(x int) bool {
	for i := 2; i < x; i += 2 {
		if x%i == 0 {
			return false
		}
	}
	return true
}

func TestPrime(t *testing.T) {
	if x := prime(4); x != false {
		t.Errorf("prime(4) is false, but got %v", x)
	}
	if x := prime(7); x != true {
		t.Errorf("prime(7) is true, but got %v", x)
	}

	if x := prime(23244); x != false {
		t.Errorf("prime(23244) is false (23244 = 2 x 2 x 3 x 13 x 149), but got %v", x)
	}

	// http://en.wikipedia.org/wiki/Prime_number#Definition_and_examples
	primes := [...]int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
		43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
		109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,
		179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
		241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311,
		313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383,
		389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
		461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
		547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613,
		617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683,
		691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769,
		773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
		859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
		947, 953, 967, 971, 977, 983, 991, 997}

	for j := 0; j < 100; j++ { // we could re-calc same values in a loop for performance testing
		for i := 0; i < len(primes); i++ {
			if x := prime(primes[i]); x != true {
				t.Errorf("prime(%v) is false, but got %v", primes[i], x)
			}
		}
	}
}

/* also good to know that test files have to end with _test - https://stackoverflow.com/questions/14739188/how-to-fix-this-error-runtime-main-undefined-main-init */
