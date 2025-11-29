//go:build ignore

package main

func numWaterBottles(numBottles int, numExchange int) int {
	result := 0
	full := numBottles
	empty := 0
	for {
		result += full
		empty += full
		full = 0

		if empty < numExchange {
			break
		}

		// exchange
		full = empty / numExchange
		empty = empty % numExchange
	}

	return result
}
