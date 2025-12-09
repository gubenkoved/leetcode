//go:build ignore

package main

import "fmt"

func largestRectangleArea(heights []int) int {
	// stack will hold (h, width) as we will be merging items on stack
	stack := [][2]int{}
	result := 0

	// last element edge case
	heights = append(heights, 0)

	for _, x := range heights {
		collapsingWidth := 0
		stackMin := -1

		for len(stack) > 0 && stack[len(stack)-1][0] > x {
			// element on stack is bigger, we do not really need it anymore
			// as we encounter element that will be limiting all further
			// rectangles
			top := stack[len(stack)-1]
			collapsingWidth += top[1]
			if stackMin != -1 {
				stackMin = min(stackMin, top[0])
			} else {
				stackMin = top[0]
			}
			curArea := collapsingWidth * stackMin
			result = max(result, curArea)
			stack = stack[:len(stack)-1]
		}

		// replace the all merged items on stack with a new one
		if collapsingWidth > 0 {
			stack = append(stack, [2]int{x, collapsingWidth + 1})
		} else {
			// new element is bigger -> add to the stack!
			stack = append(stack, [2]int{x, 1})
		}
	}

	return result
}

func main() {
	fmt.Println(largestRectangleArea([]int{2, 1, 5, 6, 2, 3}), 10)
}
