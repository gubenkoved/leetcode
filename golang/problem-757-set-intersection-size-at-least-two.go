//go:build ignore

package main

import (
	"sort"
)

func insideInterval(start int, end int, x int) bool {
	return start <= x && x <= end
}

func intersectionSizeTwo(intervals [][]int) int {
	// sort by decreasing end point
	sort.Slice(intervals, func(i, j int) bool {
		if intervals[i][1] == intervals[j][1] {
			return intervals[i][0] > intervals[j][0]
		}
		return intervals[i][1] < intervals[j][1]
	})

	res := 0

	// array of two max items
	max_items := []int{-1, -1}

	for i := 0; i < len(intervals); {
		// println("processing interval at index", i, ":", intervals[i][0], intervals[i][1])

		needed := 2
		if insideInterval(intervals[i][0], intervals[i][1], max_items[1]) {
			needed--
		}
		if insideInterval(intervals[i][0], intervals[i][1], max_items[0]) {
			needed--
		}

		cur := intervals[i][1]
		for needed > 0 {
			if cur == max_items[0] || cur == max_items[1] {
				cur--
				continue
			}

			// replace the min item inside max_items
			if max_items[0] < max_items[1] {
				max_items[0] = cur
			} else {
				max_items[1] = cur
			}

			res++
			cur -= 1
			needed -= 1
		}

		i += 1
	}

	return res
}

func main() {
	println(intersectionSizeTwo([][]int{{1, 3}, {3, 7}, {8, 9}}))
}
