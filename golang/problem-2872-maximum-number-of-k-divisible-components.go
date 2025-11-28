package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	Degree int
	Label  int
	Index  int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].Degree < pq[j].Degree
}

func (pq PriorityQueue) Swap(i, j int) {
	tmp := pq[i]
	pq[i] = pq[j]
	pq[j] = tmp

	// update the indexes
	pq[i].Index = i
	pq[j].Index = j
}

func (pq *PriorityQueue) Push(item any) {
	element := item.(*Item)
	element.Index = len(*pq)
	*pq = append(*pq, element)
}

func (pq *PriorityQueue) Pop() any {
	old := *pq
	popped := old[len(old)-1]
	popped.Index = -1
	*pq = old[:len(old)-1]
	return popped
}

func FirstKey(m map[int]bool) int {
	for k, _ := range m {
		return k
	}
	panic("empty map")
}

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	// priority queue for node degrees as we will need to process from the leafs
	// on each step: pick the leaf and if its value is divisible by K, then separate
	// if not, it has to be part of the parent, merge it with parent

	// process edges
	valuesMap := make(map[int]int)
	adjacencyMap := make(map[int]map[int]bool)

	for _, edge := range edges {
		a := edge[0]
		b := edge[1]

		if adjacencyMap[a] == nil {
			adjacencyMap[a] = make(map[int]bool)
		}
		if adjacencyMap[b] == nil {
			adjacencyMap[b] = make(map[int]bool)
		}

		adjacencyMap[a][b] = true
		adjacencyMap[b][a] = true
	}

	for idx, value := range values {
		valuesMap[idx] = value
	}

	// put nodes into heap by degrees
	degreesHeap := &PriorityQueue{}
	nodeToItemMap := make(map[int]*Item)

	for node, adjacentNodes := range adjacencyMap {
		item := &Item{
			Degree: len(adjacentNodes),
			Label:  node,
		}
		heap.Push(degreesHeap, item)
		nodeToItemMap[node] = item
	}

	if degreesHeap.Len() == 0 {
		return 1
	}

	result := 0

	// process the popped leaf -- either merge with parent OR split
	// in any case the node is removed from the tree, and we either
	// change the parent value OR we increase the result counter
	for {
		popped := heap.Pop(degreesHeap).(*Item)

		if popped.Degree == 0 {
			// isolated node -> finish
			result += 1
			break
		}

		parent := FirstKey(adjacencyMap[popped.Label])

		if valuesMap[popped.Label]%k == 0 {
			// separate
			result += 1
		} else {
			// merge with the parent
			valuesMap[parent] += valuesMap[popped.Label]
		}

		delete(adjacencyMap[popped.Label], parent)
		delete(adjacencyMap[parent], popped.Label)

		// decrease the parent degree in the heap as well?
		parentItem := nodeToItemMap[parent]
		parentItem.Degree -= 1
		heap.Fix(degreesHeap, parentItem.Index)
	}

	return result
}

func main() {
	fmt.Println(maxKDivisibleComponents(5, [][]int{{0, 2}, {1, 2}, {1, 3}, {2, 4}}, []int{1, 8, 1, 4, 4}, 6))
	fmt.Println(maxKDivisibleComponents(1, [][]int{}, []int{0}, 10))
}
