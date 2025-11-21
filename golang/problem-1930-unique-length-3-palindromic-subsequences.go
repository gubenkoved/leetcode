package main

import (
	"fmt"
)

func countPalindromicSubsequence(s string) int {
	handled := map[byte]bool{}
	n := len(s)
	result := 0

	for i := 0; i < n-2; i++ {
		char := s[i]
		if handled[char] {
			continue
		}

		// mark as handled
		handled[char] = true

		seen := map[byte]bool{}
		max_unique := 0

		for j := i + 1; j < n; j++ {
			if s[j] == char {
				max_unique = max(max_unique, len(seen))
			}
			seen[s[j]] = true
		}

		result += max_unique
	}

	return result
}

func main() {
	fmt.Println(countPalindromicSubsequence("aabca"))
}
