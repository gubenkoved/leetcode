package main

import (
	"sort"
)

func largestPerimeter(nums []int) int {
	// sort numbers descending
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] > nums[j]
	})

	for idx := 0; idx < len(nums)-2; idx++ {
		a := nums[idx]
		b := nums[idx+1]
		c := nums[idx+2]
		if a < b+c {
			return a + b + c
		}
	}
	return 0
}
