//go:build ignore

package main

/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guess(num int) int

func guessNumber(n int) int {
	left_incl := 0
	right_excl := 2 << 32

	for right_excl-left_incl > 1 {
		mid := (left_incl + right_excl) / 2
		if guess(mid) >= 0 {
			left_incl = mid
		} else {
			right_excl = mid
		}
	}

	return left_incl
}
