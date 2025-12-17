//go:build ignore

package main

import "fmt"

func maximumProfit(prices []int, k int) int64 {
	// looks like we can solve with 2D dynamic programming
	// dp[d][t] which is max profit can be made on day "d" with up to "t" trades

	D := len(prices)

	dp := make([][]int64, D+1)
	for d := 0; d <= D; d++ {
		dp[d] = make([]int64, k+1)
	}

	// TLE as this is O(k * D * D), D is up to 10^3, K is up to D/2
	for dealNum := 1; dealNum <= k; dealNum++ {
		// NOTE: dClose/dOpen are 1 based to make code a bit simpler when we
		// accessing DP table
		for dClose := 2; dClose <= D; dClose++ {
			// can either bought earlier and sold on day "dClose" (long)
			// OR sold earlier and bought on day "dClose" (short selling)
			// this previous day would be denoted as dOpen

			bestProfit := dp[dClose-1][dealNum]

			for dOpen := 1; dOpen < dClose; dOpen++ {
				// do nothing
				bestProfit = max(bestProfit, dp[dOpen][dealNum-1])

				// long
				bestProfit = max(bestProfit, int64(prices[dClose-1]-prices[dOpen-1])+dp[dOpen-1][dealNum-1])

				// short
				bestProfit = max(bestProfit, int64(prices[dOpen-1]-prices[dClose-1])+dp[dOpen-1][dealNum-1])
			}

			dp[dClose][dealNum] = bestProfit
		}
	}

	// fmt.Println(dp)

	return dp[D][k]
}

func main() {
	fmt.Println(maximumProfit([]int{1, 5, 5, 1, 3}, 3), 8)
	fmt.Println(maximumProfit([]int{1, 7, 9, 8, 2}, 2), 14)
	fmt.Println(maximumProfit([]int{12, 16, 19, 19, 8, 1, 19, 13, 9}, 3), 36)
}
