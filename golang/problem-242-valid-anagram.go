//go:build ignore

package main

import "slices"

func isAnagram(s string, t string) bool {
	s2 := []rune(s)
	t2 := []rune(t)

	slices.Sort(s2)
	slices.Sort(t2)

	return string(s2) == string(t2)
}
