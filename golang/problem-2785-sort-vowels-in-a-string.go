//go:build ignore

package main

import (
	"fmt"
	"slices"
	"unicode"
)

var vowelsMap = map[rune]bool{
	'a': true,
	'e': true,
	'i': true,
	'o': true,
	'u': true,
}

func isVowel(char rune) bool {
	char = unicode.ToLower(char)
	return vowelsMap[char]
}

func sortVowels(s string) string {
	vowels := []rune{}
	for _, r := range s {
		if isVowel(r) {
			vowels = append(vowels, r)
		}
	}

	// sort
	slices.Sort(vowels)

	result := []rune{}
	vowelsIdx := 0

	for _, r := range s {
		if !isVowel(r) {
			result = append(result, r)
		} else {
			// add from the sorted list
			result = append(result, vowels[vowelsIdx])
			vowelsIdx += 1
		}
	}

	return string(result)
}

func main() {
	fmt.Println(sortVowels("lEetcOde"), "lEOtcede")
}
