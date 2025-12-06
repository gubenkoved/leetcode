//go:build ignore

package main

import "fmt"

func maxProfit(prices []int, fee int) int {
	profit := 0
	prices = append(prices, -fee-1)
	n := len(prices)

	minToLeft := make([]int, n)
	minToLeft[0] = prices[0]
	maxPriceIdx := 0

	for idx := 1; idx < n; idx++ {
		price := prices[idx]

		if prices[maxPriceIdx]-price > fee {
			potentialProfit := prices[maxPriceIdx] - minToLeft[maxPriceIdx] - fee
			if potentialProfit > 0 {
				profit += potentialProfit
			}
			maxPriceIdx = idx
			minToLeft[idx] = price
		} else {
			if price > prices[maxPriceIdx] {
				maxPriceIdx = idx
			}
			minToLeft[idx] = min(minToLeft[idx-1], price)
		}
	}
	return profit
}

func main() {
	fmt.Println(maxProfit([]int{1, 3, 2, 8, 4, 9}, 2), 8)
	fmt.Println(maxProfit([]int{1, 2, 3, 4, 5, 6}, 2), 3)
	fmt.Println(maxProfit([]int{9, 8, 7, 6, 1}, 2), 0)
	fmt.Println(maxProfit([]int{4, 5, 2, 4, 3, 3, 1, 2, 5, 4}, 1), 4)
	fmt.Println(maxProfit([]int{1, 4, 3, 2, 1, 2, 3, 4, 5}, 1), 5)
}
