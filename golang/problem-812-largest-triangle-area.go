package main

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func largestTriangleArea(points [][]int) float64 {
	var result int
	result = 0
	for _, p1 := range points {
		for _, p2 := range points {
			for _, p3 := range points {
				// (1/2) |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
				result = max(result, abs(p1[0]*(p2[1]-p3[1])+p2[0]*(p3[1]-p1[1])+p3[0]*(p1[1]-p2[1])))
			}
		}
	}
	return float64(result) / 2.0
}
