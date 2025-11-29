//go:build ignore

package main

import (
	"fmt"
	"strings"
)

func fractionToDecimal(numerator int, denominator int) string {
	// 4 / 9
	// 0.   40 / 9
	// 0.(4)  4 / 9  << same input repeated, then we are in the loop!
	//
	// we actually need to track when we entered the loop as well, see:
	//       1 / 6
	// 0.?   10 / 6
	// 0.1   4 / 6
	// 0.1?  40 / 6
	// 0.16  4 / 6

	if numerator*denominator == 0 {
		return "0"
	} else if numerator < 0 && denominator > 0 {
		return "-" + fractionToDecimal(-numerator, denominator)
	} else if numerator > 0 && denominator < 0 {
		return "-" + fractionToDecimal(numerator, -denominator)
	}

	whole_part := numerator / denominator

	reminder := numerator % denominator

	// numbers after the dot
	numbers := []int{}

	// reminder -> amount of numbers seen when we saw this reminder
	seen := map[int]int{}

	for {
		seen_idx, has_seen := seen[reminder]

		if has_seen {
			// loop!
			result := fmt.Sprintf("%d.", whole_part)
			for i := 0; i < seen_idx; i++ {
				result += fmt.Sprintf("%d", numbers[i])
			}
			result += "("
			for i := seen_idx; i < len(numbers); i++ {
				result += fmt.Sprintf("%d", numbers[i])
			}
			result += ")"
			return result
		}

		seen[reminder] = len(numbers)

		if reminder == 0 {
			// no faction needed, complete division done
			result := fmt.Sprintf("%d.", whole_part)

			for _, d := range numbers {
				result += fmt.Sprintf("%d", d)
			}

			// edge case -- no decimal part
			result = strings.TrimSuffix(result, ".")

			return result
		}

		tmp := reminder * 10
		num := tmp / denominator

		numbers = append(numbers, num)

		// next reminder
		reminder = tmp % denominator
	}
}

func main() {
	fmt.Println(fractionToDecimal(2, 1))
	fmt.Println(fractionToDecimal(4, 333))
	fmt.Println(fractionToDecimal(400, 333))
	fmt.Println(fractionToDecimal(401, 4))
	fmt.Println(fractionToDecimal(1, 3))
	fmt.Println(fractionToDecimal(1, 99))
	fmt.Println(fractionToDecimal(1, 99999999))
	fmt.Println(fractionToDecimal(1, 6))
	fmt.Println(fractionToDecimal(50, 8))
	fmt.Println(fractionToDecimal(-50, 8))
}
