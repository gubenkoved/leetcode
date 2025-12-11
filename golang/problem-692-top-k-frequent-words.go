//go:build ignore

package main

import (
	"cmp"
	"slices"
)

func topKFrequent(words []string, k int) []string {
	freq := map[string]int{}

	for _, word := range words {
		freq[word] += 1
	}

	// instead of sorting whole freq list we can put the numbers into min heap
	// maintaining it to be size not bigger than K which will take O(n*logK)

	// array of tuples (word, freq)

	type Item struct {
		Word string
		Freq int
	}

	freqsArray := []Item{}
	for word, f := range freq {
		freqsArray = append(freqsArray, Item{word, f})
	}

	slices.SortFunc(freqsArray, func(a, b Item) int {
		res := -1 * cmp.Compare(a.Freq, b.Freq)
		if res != 0 {
			return res
		}
		return cmp.Compare(a.Word, b.Word)
	})

	// take first K
	result := []string{}

	for idx := 0; idx < k; idx++ {
		result = append(result, freqsArray[idx].Word)
	}

	return result
}
