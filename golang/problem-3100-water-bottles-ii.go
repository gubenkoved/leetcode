package main

import "fmt"

func maxBottlesDrunk(numBottles int, numExchange int) int {
	result := 0
	full := numBottles
	empty := 0
	for {
		// drink all
		result += full
		empty += full
		full = 0

		if empty < numExchange {
			break
		}

		// exchange while we can
		for empty >= numExchange {
			empty -= numExchange
			numExchange += 1
			full += 1
		}
	}

	return result
}

func main() {
	fmt.Println(maxBottlesDrunk(13, 6))
}
