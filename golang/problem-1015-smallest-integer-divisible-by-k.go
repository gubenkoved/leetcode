//go:build ignore

package main

import (
	"fmt"
)

func smallestRepunitDivByK(k int) int {
	// with each round number converts from, say, A to A * 10 + 1 and we need
	// efficient way to maintain the mod K w/o tracking the whole number itself;
	// the thing is that we can always store number mod K instead of full number
	// here is why:
	// Say we know A mod K from a previous round, we want to know (A * 10 + 1) mod K
	// Let's express A as (Q * K + B) then
	// (A * 10 + 1) mod K = ((Q * K + B) * 10 + 1) mod K =
	// = Q * K * 10 mod K + B * 10 mod K + 1 mod K =
	// = (0 + B * 10 + 1) mod K
	// where B is basically A mod K...

	// also, we have unsolvable situation if we get to the same reminder twice
	// as it makes the loop

	A := 1
	len := 1
	seen := map[int]bool{}
	for {
		// fmt.Println("len", len, "A", A)

		if seen[A] {
			return -1
		}

		seen[A] = true

		if A%k == 0 {
			return len
		}

		// go to the next one
		A = (A*10 + 1) % k
		len += 1
	}
}

func main() {
	fmt.Println(smallestRepunitDivByK(3))
}
