//go:build ignore

package main

import (
	"fmt"
	"strings"
)

var vowels = []string{
	"a", "e", "i", "o", "u",
}

func vowelNorm(s string) string {
	for _, vowel := range vowels {
		s = strings.Replace(s, vowel, vowels[0], -1)
	}
	return s
}

func caseNorm(s string) string {
	return strings.ToLower(s)
}

func spellchecker(wordlist []string, queries []string) []string {
	wordsMap := make(map[string]bool)
	capitalNormMap := make(map[string]string)
	vowelNormMap := make(map[string]string)

	n := len(wordlist)
	for idx := n - 1; idx >= 0; idx-- {
		word := wordlist[idx]
		wordsMap[word] = true
		capitalNormMap[caseNorm(word)] = word
		vowelNormMap[vowelNorm(caseNorm(word))] = word
	}

	result := []string{}
	for _, query := range queries {
		// exact match
		if wordsMap[query] {
			result = append(result, query)
		} else if response, ok := capitalNormMap[caseNorm(query)]; ok {
			result = append(result, response)
		} else if response, ok := vowelNormMap[vowelNorm(caseNorm(query))]; ok {
			result = append(result, response)
		} else {
			result = append(result, "")
		}
	}
	return result
}

func main() {
	// fmt.Println(spellchecker([]string{"KiTe", "kite", "hare", "Hare"}, []string{"kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"}))
	fmt.Println(spellchecker([]string{"YellOw"}, []string{"yollow"}))
}
