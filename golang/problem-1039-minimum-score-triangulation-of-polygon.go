package main

import (
	"fmt"
)

func minScoreTriangulation(values []int) int {

	cache := make(map[[2]int]int)

	// solves the original problem for polygon with indexes from original
	// values array starting at i and till j inclusive
	var solve func(i, j int) int

	solve = func(i, j int) int {
		cache_key := [2]int{i, j}
		if res, ok := cache[cache_key]; ok {
			return res
		}

		if j-i <= 1 {
			panic("at least 3 vertices needed")
		}

		result := -1
		if j-i == 2 {
			result = values[i] * values[i+1] * values[i+2]
		} else {
			// verticies at i and j are included, iterate the position of third one
			result = 0
			for m := i + 1; m < j; m++ {
				cur := values[i] * values[m] * values[j]

				// left poly
				if m-i >= 2 {
					cur += solve(i, m)
				}

				// right poly
				if j-m >= 2 {
					cur += solve(m, j)
				}

				if result == 0 {
					result = cur
				} else {
					result = min(result, cur)
				}
			}
		}

		cache[cache_key] = result

		return result
	}

	return solve(0, len(values)-1)
}

func main() {
	fmt.Println(minScoreTriangulation([]int{1, 1, 1, 1}), 2)
	fmt.Println(minScoreTriangulation([]int{1, 1, 1, 1, 1}), 3)
	fmt.Println(minScoreTriangulation([]int{1, 2, 3}), 6)
	fmt.Println(minScoreTriangulation([]int{3, 7, 4, 5}), 144)
	fmt.Println(minScoreTriangulation([]int{1, 3, 1, 4, 1, 5}), 13)
	fmt.Println(minScoreTriangulation([]int{3, 4, 4, 4, 3, 5}), 177)
	fmt.Println(minScoreTriangulation([]int{4, 4, 3, 5, 3}), 129)
}
