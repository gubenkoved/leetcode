//go:build ignore

package main

var vowels map[rune]bool = map[rune]bool{
	'a': true,
	'e': true,
	'i': true,
	'o': true,
	'u': true,
}

func isVowel(char rune) bool {
	return vowels[char]
}

func maxFreqSum(s string) int {
	freq := map[rune]int{}

	for _, x := range s {
		freq[x] += 1
	}

	maxVowelFreq := 0
	maxConsonantFreq := 0

	for k, v := range freq {
		if isVowel(k) {
			maxVowelFreq = max(maxVowelFreq, v)
		} else {
			maxConsonantFreq = max(maxConsonantFreq, v)
		}
	}

	return maxVowelFreq + maxConsonantFreq
}
