//go:build ignore

package main

import (
	"fmt"
)

func largestRectangleArea(heights []int) int {
	n := len(heights)

	// idx -> idx of first element smaller than heights[idx] to the left of idx
	firstSmallerIdxToLeft := make([]int, n)
	firstSmallerIdxToLeft[0] = -1

	// idx -> idx of the first element smaller than heights[idx] to the right of idx
	firstSmallerIdxToRight := make([]int, n)
	firstSmallerIdxToRight[n-1] = n

	for idx := 1; idx < n; idx++ {
		targetIdx := idx - 1
		for targetIdx != -1 && heights[targetIdx] >= heights[idx] {
			targetIdx = firstSmallerIdxToLeft[targetIdx]
		}
		firstSmallerIdxToLeft[idx] = targetIdx
	}

	for idx := n - 2; idx >= 0; idx-- {
		targetIdx := idx + 1
		for targetIdx != n && heights[targetIdx] >= heights[idx] {
			targetIdx = firstSmallerIdxToRight[targetIdx]
		}
		firstSmallerIdxToRight[idx] = targetIdx
	}

	result := 0
	for idx := 0; idx < n; idx++ {
		leftIdx := firstSmallerIdxToLeft[idx]
		rightIdx := firstSmallerIdxToRight[idx]
		width := rightIdx - leftIdx - 1
		result = max(result, width*heights[idx])
	}
	return result
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}), 10)
	fmt.Println(largestRectangleArea([]int{1, 1}), 2)
}
