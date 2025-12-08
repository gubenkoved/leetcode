//go:build ignore

package main

import (
	"fmt"
	"math"
)

func countTriples(n int) int {
	count := 0

	for a := 1; a <= n; a++ {
		for b := 1; b <= n; b++ {
			c := int(math.Sqrt(float64(a*a + b*b)))

			if a*a+b*b != c*c {
				continue
			}

			if c <= n {
				count += 1
				// fmt.Println(a, b, c)
			}
		}
	}

	return count
}

func main() {
	fmt.Println(countTriples(5))
}
