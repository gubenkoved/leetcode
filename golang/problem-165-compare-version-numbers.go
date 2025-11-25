package main

import (
	"fmt"
	"strconv"
	"strings"
)

func toComponents(version string) []int {
	split := strings.Split(version, ".")
	split_parsed := []int{}

	for _, s := range split {
		s_parsed, err := strconv.ParseInt(s, 10, 32)
		if err != nil {
			panic("bad integer!")
		}
		split_parsed = append(split_parsed, int(s_parsed))
	}
	return split_parsed
}

func getOrFallback[T any](array []T, idx int, fallback T) T {
	if idx < len(array) {
		return array[idx]
	} else {
		return fallback
	}
}

func compareVersion(version1 string, version2 string) int {
	components1 := toComponents(version1)
	components2 := toComponents(version2)

	n := max(len(components1), len(components2))
	for idx := 0; idx < n; idx++ {
		c1 := getOrFallback(components1, idx, 0)
		c2 := getOrFallback(components2, idx, 0)
		if c1 < c2 {
			return -1
		} else if c2 < c1 {
			return +1
		}
	}

	return 0
}

func main() {
	fmt.Println(compareVersion("1.2", "1.10"))
	fmt.Println(compareVersion("1.20", "1.10"))
	fmt.Println(compareVersion("1.0", "1.0.0"))
}
