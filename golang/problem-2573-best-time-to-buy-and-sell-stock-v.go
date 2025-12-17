//go:build ignore

package main

import (
	"fmt"
)

func maximumProfit(prices []int, k int) int64 {
	// looks like we can solve with 2D dynamic programming
	// dp[d][t] which is max profit can be made on day "d" with up to "t" trades

	var maxProfit func(d int, trades int, state int) int64

	// states:
	// 0 - not holding position
	// 1 - holding long
	// 2 - holding short

	// maxProfit(d, trades, state) is max profit at day "d" while making
	// "trades" trades either not holding position, holding long or holding short
	// note that we will separately track "profit" from buying and selling stock
	// not from the trade as a whole

	memo := map[[3]int]int64{}

	maxProfit = func(d, trades, state int) int64 {
		key := [3]int{d, trades, state}

		cached, ok := memo[key]
		if ok {
			return cached
		}

		var result int64

		if trades == 0 {
			return 0
		}

		p := int64(prices[d])

		if d == 0 {
			if state == 0 {
				result = 0
			} else if state == 1 {
				// have to buy (will have to sell later)
				result = -p
			} else if state == 2 {
				// short selling (will have to buy later)
				result = +p
			}
		} else {
			// did not do anything -- state is the same as previous day
			result = maxProfit(d-1, trades, state)

			// it is not obvious why we have to decrement trade count on entering
			// the deal, not when exiting it, but otherwise there will be boundary
			// issue when we land with 0 trades while needing to enter long/short

			if state == 0 {
				// either we did not do anything
				// OR closing our long position
				// OR closing our short position
				result = max(
					result,
					maxProfit(d-1, trades, 1)+p, // closed long (selling)
					maxProfit(d-1, trades, 2)-p, // closed short (buying)
				)
			} else if state == 1 {
				// if state is 1 it means transfer from no position was made via buying
				result = max(
					result,
					maxProfit(d-1, trades-1, 0)-p,
				)
			} else if state == 2 {
				// did not hold position, but selling now
				result = max(
					result,
					maxProfit(d-1, trades-1, 0)+p,
				)
			}
		}

		memo[key] = result

		return result
	}

	days := len(prices)
	return maxProfit(days-1, k, 0)
}

func main() {
	fmt.Println(maximumProfit([]int{1, 5, 5, 1, 3}, 3), 8)
	fmt.Println(maximumProfit([]int{1, 7, 9, 8, 2}, 2), 14)
	fmt.Println(maximumProfit([]int{12, 16, 19, 19, 8, 1, 19, 13, 9}, 3), 36)
}
