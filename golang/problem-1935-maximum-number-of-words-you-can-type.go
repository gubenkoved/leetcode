//go:build ignore

package main

import (
	"strings"
)

func canBeTypedWords(text string, brokenLetters string) int {
	words := strings.Split(text, " ")
	brokenSet := make(map[rune]bool)

	for _, ch := range brokenLetters {
		brokenSet[ch] = true
	}

	result := 0
	for _, word := range words {
		idx := strings.IndexAny(word, brokenLetters)
		if idx == -1 {
			result++
		}
	}
	return result
}
