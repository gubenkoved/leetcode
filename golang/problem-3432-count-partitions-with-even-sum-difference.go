//go:build ignore

package main

func abs(x int) int {
	if x < 0 {
		return -x
	} else {
		return x
	}
}

func countPartitions(nums []int) int {
	sum := 0
	for _, x := range nums {
		sum += x
	}

	result := 0
	left := 0
	right := sum

	for idx := 0; idx < len(nums)-1; idx++ {
		x := nums[idx]
		left += x
		right -= x

		if abs(left-right)%2 == 0 {
			result += 1
		}
	}
	return result
}
