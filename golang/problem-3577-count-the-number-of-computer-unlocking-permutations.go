//go:build ignore

package main

func countPermutations(complexity []int) int {
	n := len(complexity)

	// first password complexity has to be strictly less than any other element,
	// otherwise there will be computer which is not possible to decrypt
	for idx := 1; idx < n; idx++ {
		if complexity[idx] <= complexity[0] {
			return 0
		}
	}

	result := 1
	M := int(1e9 + 7)

	// factorial n - 1
	for k := 2; k < len(complexity); k++ {
		result = (k * result) % M
	}

	return result
}
