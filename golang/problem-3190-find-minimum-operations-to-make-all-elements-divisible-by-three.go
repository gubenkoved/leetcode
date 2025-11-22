func minimumOperations(nums []int) int {
	result := 0

	for _, num := range nums {
		result += min(num%3, 3-(num%3))
	}

	return result
}
