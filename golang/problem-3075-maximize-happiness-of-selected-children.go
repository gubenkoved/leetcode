//go:build ignore

package main

import (
	"cmp"
	"slices"
)

func maximumHappinessSum(happiness []int, k int) int64 {
	slices.SortFunc(happiness, func(a, b int) int {
		return -1 * cmp.Compare(a, b)
	})

	result := int64(0)
	for idx := range k {
		result += max(0, int64(happiness[idx]-idx))
	}
	return result
}
