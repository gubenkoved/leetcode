//go:build ignore

package main

import (
	"fmt"
	"math"
	"strconv"
)

func genPrimes(upto int) []int {
	// eratosphen seive?

	result := []int{}

	a := make([]bool, upto+1)
	for x := 2; x <= upto; x++ {
		if !a[x] {
			result = append(result, x)

			// mark other which are devisible by x as non primes
			for i := x; i <= upto; i += x {
				a[i] = true
			}
		}
	}
	return result
}

func isPrime(num int) bool {
	if num == 1 {
		return false
	}
	primes := genPrimes(int(math.Floor(math.Sqrt(float64(num)))))
	for _, prime := range primes {
		if num%prime == 0 {
			return false
		}
	}
	return true
}

func completePrime(num int) bool {
	numString := strconv.Itoa(num)
	digits := len(numString)
	for idx := 0; idx < digits; idx++ {
		prefix, _ := strconv.Atoi(numString[idx:])
		suffix, _ := strconv.Atoi(numString[:digits-idx])

		if !isPrime(prefix) || !isPrime(suffix) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPrime(2))
	fmt.Println(isPrime(3))
	fmt.Println(completePrime(23), true)
	fmt.Println(completePrime(12345678), false)
}
