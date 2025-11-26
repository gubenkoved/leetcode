package main

func maxFrequencyElements(nums []int) int {
	freqs := make(map[int]int)
	max_frequency := 0

	for _, x := range nums {
		freqs[x] += 1

		max_frequency = max(max_frequency, freqs[x])
	}

	result := 0

	for _, v := range freqs {
		if v == max_frequency {
			result += v
		}
	}

	return result
}
