//go:build ignore

package main

func minOperations(nums []int, k int) int {
	sum := 0
	for _, x := range nums {
		sum += x
	}
	return sum % k
}
