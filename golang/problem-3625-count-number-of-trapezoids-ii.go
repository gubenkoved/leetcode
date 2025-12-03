//go:build ignore

package main

import (
	"fmt"
	"math"
	"slices"
)

func abs(value int) int {
	if value < 0 {
		return -value
	} else {
		return value
	}
}

func gcd(a, b int) int {
	if b > a {
		return gcd(b, a)
	}
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

func normalize(dx, dy int) vector {
	div := gcd(abs(dx), abs(dy))

	// unify the directions which are going parallel, but in opposite ways
	if dy < 0 {
		return [2]float64{float64(-dy / div), float64(-dx / div)}
	} else {
		return [2]float64{float64(dy / div), float64(dx / div)}
	}
}

// edge will be defined as pair of points by their indexes in the original
// slice
type vector [2]float64
type point [2]int
type line [2]point

func comb2(x int) int {
	return x * (x - 1) / 2
}

func orthogonal(v vector) vector {
	return vector{v[1], v[0]}
}

func lengthSquared(v vector) float64 {
	dx := v[0]
	dy := v[1]
	return dx*dx + dy*dy
}

func length(v vector) float64 {
	return math.Sqrt(float64(lengthSquared(v)))
}

func vectorDotProduct(v1 vector, v2 vector) float64 {
	return v1[0]*v2[0] + v1[1]*v2[1]
}

func vectorProduct(v vector, fact float64) vector {
	return vector{
		float64(v[0] * fact),
		float64(v[1] * fact),
	}
}

// v1 - v2
func vectorSubtract(v1 vector, v2 vector) vector {
	return vector{
		v1[0] - v2[0],
		v1[1] - v2[1],
	}
}

func toUnitVector(vec vector) vector {
	d := length(vec)
	return vector{
		vec[0] / d,
		vec[1] / d,
	}
}

func distance(point point, vec vector) float64 {
	pointVectorInv := vector{
		float64(-point[0]),
		float64(-point[1]),
	}
	return length(
		vectorSubtract(
			pointVectorInv,
			vectorProduct(vec, vectorDotProduct(vec, pointVectorInv))))
}

func roundFloat(x float64, prec int) float64 {
	fact := math.Pow10(prec)
	return math.Round(x*fact) / fact
}

func zeroAreaCount(bucketLines []line) int {
	line := bucketLines[0]
	direction := vector{
		float64(line[1][0] - line[0][0]),
		float64(line[1][1] - line[0][1]),
	}
	direction = toUnitVector(direction)

	subgroupsCounts := map[float64]int{}
	for _, line := range bucketLines {
		dist := distance(line[0], direction)
		dist = roundFloat(dist, 3)
		subgroupsCounts[dist] += 1
	}

	result := 0
	for _, v := range subgroupsCounts {
		result += comb2(v)
	}

	return result
}

func parallelogramCount(bucketLines []line) int {
	byLenCount := map[float64]int{}

	for _, line := range bucketLines {
		vec := vector{
			float64(line[1][0] - line[0][0]),
			float64(line[1][1] - line[0][1]),
		}
		byLenCount[length(vec)] += 1
	}
	result := 0
	for _, count := range byLenCount {
		result += comb2(count)
	}
	return result
}

func countTrapezoids(points [][]int) int {
	n := len(points)

	// direction does not really matter, need to normalize, we will do that
	// by sorting by X, and each edge goes from point which x is not bigger
	// than of the end point
	slices.SortFunc(points, func(a, b []int) int {
		x1 := a[0]
		x2 := b[0]
		if x1 == x2 {
			return 0
		} else if x1 < x2 {
			return -1
		} else {
			return +1
		}
	})

	// slope -> slice of edges
	buckets := map[vector][]line{}

	for i := 0; i < n-1; i++ {
		for j := i + 1; j < n; j++ {
			dx := points[j][0] - points[i][0]
			dy := points[j][1] - points[i][1]

			slope := normalize(dx, dy)

			if buckets[slope] == nil {
				buckets[slope] = []line{}
			}
			p1 := point{points[i][0], points[i][1]}
			p2 := point{points[j][0], points[j][1]}
			line := line{p1, p2}
			buckets[slope] = append(buckets[slope], line)
		}
	}

	result := 0
	pCount := 0

	// TODO: we now undercount -- we subtracted parallelograms of zero area as
	//  well: either do not consider these parallelograms (preferrable) OR
	//  find a way to count zero area "parallelograms" and add them back to avoid
	//  double subtraction for them
	for _, edges := range buckets {
		// inside each bucket of the same slope we should pick a pair of
		// edges which we can do C(2, k) different ways
		result += comb2(len(edges))

		// subtract for cases where we ended up counting zero area ones
		// (both sides on the same line)
		result -= zeroAreaCount(edges)

		// count parallelograms which will be overcounted due to 2 directions
		// being present
		pCount += parallelogramCount(edges)
	}

	// pCount itself is double counted!
	pCount /= 2

	return result - pCount
}

func main() {
	// fmt.Println(countTrapezoids([][]int{{-1, -1}, {1, 1}, {-1, 1}, {1, -1}, {0, 0}}))

	// fmt.Println(countTrapezoids([][]int{{-3, 2}, {3, 0}, {2, 3}, {3, 2}, {2, -3}}), 2)
	// fmt.Println(countTrapezoids([][]int{{0, 0}, {1, 0}, {0, 1}, {2, 1}}), 1)

	// fmt.Println(countTrapezoids([][]int{{0, 10}, {0, 20}, {0, 30}, {2, 40}}), 0)

	// fmt.Println(countTrapezoids([][]int{{0, 1}, {0, 2}, {0, 3}, {0, 4}}), 0)

	// fmt.Println(countTrapezoids([][]int{{0, 1}, {0, 3}, {0, 7}, {1, 113}, {1, 127}, {1, 139}}), 9)

	// single parallelogram
	fmt.Println(countTrapezoids([][]int{{0, 0}, {1, 0}, {1, 1}, {2, 1}}), 1)

	fmt.Println(countTrapezoids([][]int{{71, -89}, {-75, -89}, {-9, 11}, {-24, -89}, {-51, -89}, {-77, -89}, {42, 11}}), 10)
}
