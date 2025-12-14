//go:build ignore

package main

import (
	"fmt"
	"strings"
)

func numberOfWays(corridor string) int {
	// split into segments and track amount of trailing plants
	// each segment should have exactly two chairs

	// drop trailing/leading plants as they do not matter
	corridor = strings.Trim(corridor, "P")

	// track trailing plants in each
	segments := []int{}

	n := len(corridor)
	seatCounter := 0
	conseqPlants := 0
	for idx := 0; idx < n; idx++ {
		if corridor[idx] == 'S' {
			seatCounter += 1

			// process start of new segment
			if seatCounter != 1 && seatCounter%2 == 1 {
				segments = append(segments, conseqPlants)
			}

			conseqPlants = 0
		} else {
			conseqPlants += 1
		}
	}

	// non even number of seats OR no seats at all
	if seatCounter%2 != 0 || seatCounter == 0 {
		return 0
	}

	M := int(1e9 + 7)
	result := 1

	for _, p := range segments {
		result = result * (p + 1) % M
	}

	return result
}

func main() {
	fmt.Println(numberOfWays("SSPPSPS"), 3)
	fmt.Println(numberOfWays("PPSPSP"), 1)
}
