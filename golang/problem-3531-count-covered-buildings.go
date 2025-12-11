//go:build ignore

package main

import (
	"cmp"
	"fmt"
	"slices"
)

func countCoveredBuildings(n int, buildings [][]int) int {
	// maps X coordinate into list of indexes of building in that X coordinate
	groupsByX := map[int][]int{}
	// same for Y
	groupsByY := map[int][]int{}

	for idx, coordinates := range buildings {
		x := coordinates[0]
		y := coordinates[1]

		if groupsByX[x] == nil {
			groupsByX[x] = []int{}
		}
		if groupsByY[y] == nil {
			groupsByY[y] = []int{}
		}

		groupsByX[x] = append(groupsByX[x], idx)
		groupsByY[y] = append(groupsByY[y], idx)
	}

	// indexes of exposed buildings
	exposed := map[int]bool{}

	// sort all the groups
	for _, v := range groupsByX {
		// compare by Y coordinate
		slices.SortFunc(v, func(a, b int) int {
			return cmp.Compare(buildings[a][1], buildings[b][1])
		})

		// in each group first and last are exposed, others are shielded by them
		exposed[v[0]] = true
		exposed[v[len(v)-1]] = true
	}
	for _, v := range groupsByY {
		// compare by X coordinate
		slices.SortFunc(v, func(a, b int) int {
			return cmp.Compare(buildings[a][0], buildings[b][0])
		})
		exposed[v[0]] = true
		exposed[v[len(v)-1]] = true
	}

	return len(buildings) - len(exposed)
}

func main() {
	fmt.Println(countCoveredBuildings(10, [][]int{{1, 2}, {2, 2}, {3, 2}, {2, 1}, {2, 3}}), 1)
}
