//go:build ignore

package main

import "fmt"

func minSubarray(nums []int, p int) int {
	n := len(nums)
	prefixSums := make([]int, n+1)

	for idx := 0; idx < n; idx++ {
		prefixSums[idx+1] = nums[idx] + prefixSums[idx]
	}

	K := prefixSums[n] % p

	// edge case: already no reminder
	if K == 0 {
		return 0
	}

	// index of last position that gave us prefix sum with a given reminder
	lastIndexOfPrefixSumReminder := map[int]int{}
	result := -1

	// we need to find a subrange which sum has exactly the reminder of K
	// "reminder"
	for idx := 0; idx < n+1; idx++ {
		curReminder := prefixSums[idx] % p

		// curReminder - targetReminder mod P = K mod P
		// targetReminder = (P + curReminder - K) mod P
		targetReminder := (p + curReminder - K) % p

		if lastIdxSameReminder, ok := lastIndexOfPrefixSumReminder[targetReminder]; ok {
			curLen := idx - lastIdxSameReminder
			if curLen < result || result == -1 {
				result = curLen
			}
		}

		lastIndexOfPrefixSumReminder[curReminder] = idx
	}

	// not allowed to remove whole array
	if result == n {
		return -1
	}

	return result
}

func main() {
	fmt.Println(minSubarray([]int{3, 1, 4, 2}, 6), 1)
	fmt.Println(minSubarray([]int{6, 3, 5, 2}, 9), 2)
	fmt.Println(minSubarray([]int{1, 2, 3, 4}, 77), -1)
	fmt.Println(minSubarray([]int{8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2}, 148), 7)
}
