//go:build ignore

package main

import (
	"container/list"
	"fmt"
)

func topFreqSlow(freqMap map[byte]int) int {
	maxFreq := 0
	for _, v := range freqMap {
		maxFreq = max(maxFreq, v)
	}
	return maxFreq
}

func characterReplacement(s string, k int) int {
	n := len(s)

	l := 0
	r := -1

	// store linked list ordered by frequency + map from char to LinkedListItem
	//  this way we can find most frequent one in O(1)
	freqList := list.New()
	charToElementMap := map[byte]*list.Element{}
	freqMap := map[byte]int{}

	biggestWindow := 0

	for r < n-1 {
		// move right pointer while window still has less then K chars different
		// from the top frequency one (which will be preserved), stop when
		// condition is violated

		for r < n-1 {
			r += 1
			char := s[r]
			freqMap[char] += 1

			if _, ok := charToElementMap[char]; !ok {
				// create new bucket
				el := freqList.PushFront(char)
				charToElementMap[char] = el
			}

			el := charToElementMap[char]

			// move forward if needed
			for el.Next() != nil && freqMap[char] > freqMap[el.Next().Value.(byte)] {
				freqList.MoveAfter(el, el.Next())
			}

			// check if our window matching condition
			topFreqChar := freqList.Back().Value.(byte)
			topFreq := freqMap[topFreqChar]

			// if topFreq != topFreqSlow(freqMap) {
			// 	panic("something is not right")
			// }

			windowSize := r - l + 1
			needReplacement := windowSize - topFreq

			if needReplacement <= k {
				biggestWindow = max(biggestWindow, windowSize)
			} else {
				// too big, stop
				break
			}
		}

		// move the window left while condition still violated
		for l < r {
			char := s[l]
			freqMap[char] -= 1
			l += 1

			// update the linked list if needed
			el := charToElementMap[char]

			for el.Prev() != nil && freqMap[char] < freqMap[el.Prev().Value.(byte)] {
				freqList.MoveBefore(el, el.Prev())
			}

			topFreqChar := freqList.Back().Value.(byte)
			topFreq := freqMap[topFreqChar]

			windowSize := r - l + 1
			needReplacement := windowSize - topFreq

			// back on track, stop shrinking!
			if needReplacement <= k {
				break
			}
		}
	}

	return biggestWindow
}

func main() {
	// fmt.Println(characterReplacement("ABAB", 2), 4)
	// fmt.Println(characterReplacement("AABABBA", 1), 4)
	fmt.Println(characterReplacement("EOEMQLLQTRQDDCOERARHGAAARRBKCCMFTDAQOLOKARBIJBISTGNKBQGKKTALSQNFSABASNOPBMMGDIOETPTDICRBOMBAAHINTFLH", 7), 11)
}
