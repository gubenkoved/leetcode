//go:build ignore

package main

import "fmt"

func gcd(a, b int) int {
	if a < b {
		return gcd(b, a)
	}
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func are_coprimes(a, b int) bool {
	return gcd(a, b) == 1
}

func replaceNonCoprimes(nums []int) []int {
	result := []int{}

	for _, x := range nums {
		result = append(result, x)

		// check if we formed co-primes which should be replaced
		for len(result) >= 2 {
			n := len(result)
			a := result[n-1]
			b := result[n-2]

			if are_coprimes(a, b) {
				break
			}

			result = result[:n-2]
			result = append(result, lcm(a, b))
		}
	}

	return result
}

func main() {
	fmt.Println(replaceNonCoprimes([]int{6, 4, 3, 2, 7, 6, 2}))
	fmt.Println(replaceNonCoprimes([]int{2, 2, 1, 1, 3, 3, 3}))
}
