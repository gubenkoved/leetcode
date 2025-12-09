//go:build ignore

package main

func specialTriplets(nums []int) int {
	freqBefore := map[int]int{}
	freqAfter := map[int]int{}

	// populate freq after
	for _, x := range nums {
		freqAfter[x] += 1
	}

	result := 0
	for _, x := range nums {
		// discard current element from freqAfter
		freqAfter[x] -= 1

		t := x * 2
		result += freqBefore[t] * freqAfter[t]

		// add current to freqBefore
		freqBefore[x] += 1
	}

	M := int(1e9 + 7)
	return result % M
}
