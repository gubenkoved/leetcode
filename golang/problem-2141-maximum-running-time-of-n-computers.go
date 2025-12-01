// go:build ignore

package main

import "fmt"

func maxRunTime(n int, batteries []int) int64 {
	var sum int64
	sum = 0
	for _, x := range batteries {
		sum += int64(x)
	}

	// find the high boundary
	high := 1 + sum/int64(n) // exclusive
	low := int64(0)

	for {
		if high-low == 1 {
			return low
		}

		mid := (high + low) / 2

		// calculate capped sum
		capped_sum := int64(0)
		for _, x := range batteries {
			capped_sum += min(mid, int64(x))
		}

		if capped_sum/int64(n) < mid {
			high = mid
		} else {
			low = mid
		}
	}
}

func main() {
	fmt.Println(maxRunTime(2, []int{3, 3, 3}))
}
