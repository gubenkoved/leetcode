package main

import (
	"cmp"
	"regexp"
	"slices"
)

func validateCoupons(code []string, businessLine []string, isActive []bool) []string {

	validBusinessLines := map[string]int{
		"electronics": 1,
		"grocery":     2,
		"pharmacy":    3,
		"restaurant":  4,
	}

	r, _ := regexp.Compile("^[a-zA-Z0-9_]+$")

	indexes := []int{}
	n := len(code)
	for idx := 0; idx < n; idx++ {
		matched := true
		cur := code[idx]
		cat := businessLine[idx]

		if validBusinessLines[cat] == 0 {
			matched = false
		}

		if !isActive[idx] {
			matched = false
		}

		if !r.MatchString(cur) {
			matched = false
		}

		if matched {
			indexes = append(indexes, idx)
		}
	}

	// sort
	slices.SortFunc(indexes, func(a, b int) int {
		blA := businessLine[a]
		blB := businessLine[b]
		blCmp := cmp.Compare(validBusinessLines[blA], validBusinessLines[blB])

		if blCmp != 0 {
			return blCmp
		}

		return cmp.Compare(code[a], code[b])
	})

	result := []string{}

	for _, idx := range indexes {
		result = append(result, code[idx])
	}

	return result
}
