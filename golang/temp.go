package main

import "fmt"

func main() {
	foo := []int{0, 1, 2, 3, 4}

	view := foo[1:4]

	// changes original array as there is enough capacity
	// bar := append(view, 9)

	// does NOT change original array as not enough capacity
	bar := append(view, 8, 9)

	fmt.Println(foo)
	fmt.Println(view)
	fmt.Println(bar)
}
