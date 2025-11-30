//go:build ignore

package main

var vowels = map[rune]bool{
	'a': true,
	'e': true,
	'i': true,
	'o': true,
	'u': true,
}

func isVowel(char rune) bool {
	return vowels[char]
}

func doesAliceWin(s string) bool {
	// if number of vowels is odd Alice wins right away by taking whole thing
	// if even, then Alice also wins by taking all leaving 1 vowel containing
	// substring
	// only if string does NOT have any vowels Alice can not take step and
	// looses

	vowelCount := 0
	for _, r := range s {
		if isVowel(r) {
			vowelCount += 1
		}
	}

	return vowelCount != 0
}
