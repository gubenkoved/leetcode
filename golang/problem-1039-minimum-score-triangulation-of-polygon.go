package main

import (
	"fmt"
)

func minScoreTriangulation(values []int) int {
	if len(values) < 3 {
		panic("At least 3 vertices needed")
	}

	if len(values) == 3 {
		return values[0] * values[1] * values[2]
	}

	best := -1
	n := len(values)

	// given each edge is part of SOME triangle, we take edge with verticies
	// at 0 and 1 and enumerate all possible positions
	for m := 2; m < n; m++ {
		cur_triangle := []int{values[0], values[1], values[m]}
		cur := minScoreTriangulation(cur_triangle)

		left := values[1 : m+1]
		if len(left) >= 3 {
			cur += minScoreTriangulation(left)
		}

		right := append(append([]int{}, values[m:]...), values[0])
		if len(right) >= 3 {
			cur += minScoreTriangulation(right)
		}

		if best != -1 {
			best = min(best, cur)
		} else {
			best = cur
		}
	}

	return best
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
