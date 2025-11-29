//go:build ignore

package main

import "fmt"

func prefixesDivBy5(nums []int) []bool {
	x := 0
	result := []bool{}
	for _, b := range nums {
		x = (x << 1) | b

		var cur bool

		if x%5 == 0 {
			cur = true
		} else {
			cur = false
		}

		// keep x low
		x = x % 10

		result = append(result, cur)
	}
	return result
}

func main() {
	fmt.Println(prefixesDivBy5([]int{0, 1, 1}))
}
