package main

import (
	"fmt"
	"math"
)

func maxSubarraySum(nums []int, k int) int64 {
	n := len(nums)
	prefix_sum := make([]int64, len(nums))

	for idx := 0; idx < n; idx++ {
		prefix_sum[idx] = int64(nums[idx])
		if idx > 0 {
			prefix_sum[idx] += prefix_sum[idx-1]
		}
	}

	var best int64
	var running int64

	best = math.MinInt64

	for offset := 0; offset < k; offset++ {
		running = math.MinInt64
		for l := offset; l+k-1 < n; l += k {
			// right side (inclusive) of the range of size k
			r := l + k - 1
			block_sum := int64(prefix_sum[r])
			if l > 0 {
				block_sum -= prefix_sum[l-1]
			}
			// restart the running if we have better result from the current block
			if running < 0 {
				running = block_sum
			} else {
				running += block_sum
			}
			best = max(best, running)
		}
	}
	return best
}

func main() {
	fmt.Println(maxSubarraySum([]int{1, 2}, 1), 3)
	fmt.Println(maxSubarraySum([]int{1, 2, 3}, 1), 6)
	fmt.Println(maxSubarraySum([]int{-1, -2, -3, -4, -5}, 4), -10)
	fmt.Println(maxSubarraySum([]int{-5, -1, -2, -3, -4}, 4), -10)
}
