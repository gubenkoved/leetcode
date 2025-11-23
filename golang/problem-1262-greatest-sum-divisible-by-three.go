package main

import (
	"fmt"
)

func maxSumDivThree(nums []int) int {
	n := len(nums)

	// since we only interested in result for previous step
	// we can store only the last column for our DP array

	var dp [3]int

	dp[nums[0]%3] = nums[0]

	for i := 1; i < n; i++ {
		next_dp := dp

		for j := 0; j < 3; j++ {
			new_sum := dp[j] + nums[i]
			new_rem := new_sum % 3
			if new_sum > next_dp[new_rem] {
				next_dp[new_rem] = new_sum
			}
		}

		dp = next_dp
	}

	// fmt.Println(dp)

	return dp[0]
}

func main() {
	fmt.Println(maxSumDivThree([]int{3, 6, 5, 1, 8}), 18)
	fmt.Println(maxSumDivThree([]int{4}), 0)
	fmt.Println(maxSumDivThree([]int{1, 2, 3, 4, 4}), 12)
}
