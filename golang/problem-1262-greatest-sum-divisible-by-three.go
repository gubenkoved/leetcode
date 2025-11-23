package main

import (
	"fmt"
)

func maxSumDivThree(nums []int) int {
	n := len(nums)
	var dp [][]int

	for i := 0; i < n; i++ {
		dp = append(dp, make([]int, 3))
	}

	for i := 0; i < n; i++ {
		num := nums[i]
		reminder := num % 3
		if i == 0 {
			// first edge case
			dp[0][reminder] = num
		} else {
			// base case -> carry over previous
			for j := 0; j < 3; j++ {
				dp[i][j] = dp[i-1][j]
			}
			for j := 0; j < 3; j++ {
				new_sum := dp[i-1][j] + num
				new_rem := new_sum % 3
				if new_sum > dp[i][new_rem] {
					dp[i][new_rem] = new_sum
				}
			}
		}
	}

	fmt.Println(dp)

	return dp[n-1][0]
}

func main() {
	fmt.Println(maxSumDivThree([]int{3, 6, 5, 1, 8}), 18)
	fmt.Println(maxSumDivThree([]int{4}), 0)
	fmt.Println(maxSumDivThree([]int{1, 2, 3, 4, 4}), 12)
}
