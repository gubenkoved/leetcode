//go:build ignore

package main

import "fmt"

func countOdds(low int, high int) int {
	n := high - low + 1
	k := n / 2 // each pair have to yield an odd number
	m := n % 2
	if m == 1 && high%2 == 1 {
		k += 1
	}
	return k
}

func main() {
	fmt.Println(countOdds(3, 7), 3)
	fmt.Println(countOdds(8, 10), 1)
	fmt.Println(countOdds(7, 9), 2)
}
