//go:build ignore

package main

import (
	"fmt"
	"sort"
)

func triangleNumber(nums []int) int {
	sort.Ints(nums)

	n := len(nums)
	result := 0

	// i > j > k, try all i, j, find all k using binary search using triangle
	// inequality: a + b > c, use smallest a + b
	for i := 2; i < n; i++ {
		for j := 1; j < i; j++ {
			// binary search for amount for index of first number which is
			// bigger than nums[i] - nums[j] to fulfil inequality
			target := nums[i] - nums[j]
			target_idx := sort.Search(n, func(idx int) bool {
				return nums[idx] > target
			})
			// fmt.Println("i", i, "j", j, "target idx", target_idx)

			if target_idx < j {
				result += j - target_idx
			}
		}
	}

	return result
}

func main() {
	fmt.Println(triangleNumber([]int{2, 2, 3, 4}))
	fmt.Println(triangleNumber([]int{4, 2, 3, 4}))
}
