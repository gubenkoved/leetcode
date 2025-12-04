//go:build ignore

package main

import "fmt"

func countCollisions(directions string) int {
	collisions := 0
	n := len(directions)

	// only cars which do not collide -- a "prefix" going to LEFT
	// and suffix going to the right, we will discard them later
	// stationary cars do not contribute since collision counter
	// only yields 1 for such case (by definition)
	for _, chr := range directions {
		if chr == 'R' || chr == 'L' {
			collisions += 1
		}
	}

	// discard cars which do not actually collide
	for idx := 0; idx < n; idx++ {
		if directions[idx] != 'L' {
			break
		}
		collisions -= 1
	}
	for idx := n - 1; idx >= 0; idx-- {
		if directions[idx] != 'R' {
			break
		}
		collisions -= 1
	}

	return collisions
}

func main() {
	// fmt.Println(countCollisions("RLRSLL"), 5)
	fmt.Println(countCollisions("RSLLRSSL"), 5)
	// collision is actually non local and can propagate
	fmt.Println(countCollisions("SLLLLLL"), 6)
	fmt.Println(countCollisions("RRRRRRS"), 6)
	fmt.Println(countCollisions("RLLLLL"), 6)
	fmt.Println(countCollisions("RRL"), 3)
	fmt.Println(countCollisions("RRR"), 0)
	fmt.Println(countCollisions("LLLRRR"), 0)
	fmt.Println(countCollisions("LLL"), 0)
}
