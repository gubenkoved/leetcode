package main

import (
	"fmt"
)

func numberOfPaths(grid [][]int, k int) int {
	// it seems we can just track the number of paths for each cell
	// starting left/top corner and track number of paths for each reminder
	// then we can calculate each next cell using left and top cells

	Q := int(1e9) + 7

	rows := len(grid)
	cols := len(grid[0])

	// dp[row][col][reminder] will correspond to amount of paths to (row, col)
	// with a given reminder mod k
	var dp [][][]int

	// init the dp array
	for row := 0; row < rows; row++ {
		dp = append(dp, [][]int{})
		for col := 0; col < cols; col++ {
			dp[row] = append(dp[row], make([]int, k))
		}
	}

	// init the very first cell
	start_val := grid[0][0]
	dp[0][0][start_val%k] = 1

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			for prev_rem := 0; prev_rem < k; prev_rem++ {
				new_reminder := (prev_rem + grid[row][col]) % k
				new_ways := 0

				if row > 0 {
					new_ways += dp[row-1][col][prev_rem]
				}

				if col > 0 {
					new_ways += dp[row][col-1][prev_rem]
				}

				dp[row][col][new_reminder] += new_ways
				dp[row][col][new_reminder] = dp[row][col][new_reminder] % Q
			}
		}
	}

	// fmt.Println(dp)

	return dp[rows-1][cols-1][0]
}

func main() {
	fmt.Println(numberOfPaths([][]int{{5, 2, 4}, {3, 0, 5}, {0, 7, 2}}, 3))
	fmt.Println(numberOfPaths([][]int{{0, 0}}, 5))
	fmt.Println(numberOfPaths([][]int{{7, 3, 4, 9}, {2, 3, 6, 2}, {2, 3, 7, 0}}, 1))
}
