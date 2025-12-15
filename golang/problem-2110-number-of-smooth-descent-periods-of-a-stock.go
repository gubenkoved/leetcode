//go:build ignore

package main

import "fmt"

func getDescentPeriods(prices []int) int64 {
	n := len(prices)
	result := int64(0)
	l := int64(0)

	for idx := 0; idx < n; idx++ {
		// fmt.Printf("process idx %d, l is %d\n", idx, l)
		if idx == 0 || prices[idx-1]-prices[idx] == 1 {
			l += 1
		} else {
			// sum of 1, 2, 3, ..., l is
			// l * (1 + l) // 2
			result += (l * (1 + l)) / 2
			l = 1
		}
	}

	// process the last segment
	// fmt.Printf("final l is %d\n", l)
	result += (l * (1 + l)) / 2

	return result
}

func main() {
	fmt.Println(getDescentPeriods([]int{3, 2, 1, 4}), 7)
	fmt.Println(getDescentPeriods([]int{8, 6, 7, 7}), 4)
	fmt.Println(getDescentPeriods([]int{1}), 1)
}
