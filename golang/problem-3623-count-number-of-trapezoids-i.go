//go:build ignore

package main

import "fmt"

func comb(x int) int {
	return x * (x - 1) / 2
}

func countTrapezoids(points [][]int) int {
	// suppose counts per each horizontal line are
	// n1, n2, .., nk
	// then the answer is going to be
	//   C(2, n1) * (C(2, n2) + C(2, n3) + ... + C(2, nk))
	// + C(2, n2) * (C(2, n1) + C(2, n3) + ... + C(2, nk))
	// ..
	// + C(2, nk) * (C(2, n1) + C(2, n2) + ... + C(2, nk-1))
	// ... OR we can simplify to
	// C(2, n1) * C + C(2, n2) * C + ... + C(2, nk) * C - C(2,n1)^2 - C(2, n2)^2 - ... - C(2, nk)^2
	// where C is C(2, n1) + C(2, n2) + ... + C(2, nk)
	// (we also double counted them all)

	countsPerY := map[int]int{}

	for _, p := range points {
		y := p[1]
		countsPerY[y] += 1
	}

	C := int64(0)

	for _, y := range countsPerY {
		C += int64(comb(y))
	}

	result := int64(0)
	for _, y := range countsPerY {
		cy := int64(comb(y))
		result += cy * C
		result -= cy * cy
	}

	result /= 2

	q := int64(1e9 + 7)
	return int(result % q)
}

func main() {
	fmt.Println(countTrapezoids([][]int{{1, 0}, {2, 0}, {3, 0}, {2, 2}, {3, 2}}))
	fmt.Println(countTrapezoids([][]int{{0, 0}, {1, 0}, {0, 1}, {2, 1}}))
}
