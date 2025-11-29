//go:build ignore

package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	Rating int
	Index  int
	Food   string
}

type Heap []*Item

func (h Heap) Len() int {
	return len(h)
}

func (h Heap) Less(i, j int) bool {
	if h[i].Rating != h[j].Rating {
		return h[i].Rating > h[j].Rating
	} else {
		return h[i].Food < h[j].Food
	}
}

func (h Heap) Swap(i, j int) {
	tmp := h[i]
	h[i] = h[j]
	h[j] = tmp

	h[i].Index = i
	h[j].Index = j
}

func (h *Heap) Pop() any {
	n := len(*h)
	item := (*h)[n-1]
	*h = (*h)[:n-1]
	return item
}

func (h *Heap) Push(item any) {
	el := item.(*Item)
	el.Index = len(*h)
	*h = append(*h, el)
}

type FoodRatings struct {
	perCuisineHeap map[string]*Heap
	foodToCuisine  map[string]string
	foodToItem     map[string]*Item
}

func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
	instance := FoodRatings{
		perCuisineHeap: map[string]*Heap{},
		foodToCuisine:  map[string]string{},
		foodToItem:     map[string]*Item{},
	}

	// process start conditions
	for idx, food := range foods {
		cuisine := cuisines[idx]
		rating := ratings[idx]

		// add the food
		item := &Item{
			Rating: rating,
			Food:   food,
		}

		if instance.perCuisineHeap[cuisine] == nil {
			instance.perCuisineHeap[cuisine] = &Heap{}
		}
		h := instance.perCuisineHeap[cuisine]

		heap.Push(h, item)

		instance.foodToCuisine[food] = cuisine
		instance.foodToItem[food] = item
	}

	return instance
}

func (this *FoodRatings) ChangeRating(food string, newRating int) {
	cuisine := this.foodToCuisine[food]
	h := this.perCuisineHeap[cuisine]
	item := this.foodToItem[food]
	hIndex := item.Index
	(*h)[hIndex].Rating = newRating
	heap.Fix(h, hIndex)
}

func (this *FoodRatings) HighestRated(cuisine string) string {
	h := this.perCuisineHeap[cuisine]
	return (*h)[0].Food
}

func main() {
	obj := Constructor(
		[]string{"kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"},
		[]string{"korean", "japanese", "japanese", "greek", "japanese", "korean"},
		[]int{9, 12, 8, 15, 14, 7})

	fmt.Println(obj.HighestRated("korean"), "kimchi")
	fmt.Println(obj.HighestRated("japanese"), "ramen")
	obj.ChangeRating("sushi", 16)
	fmt.Println(obj.HighestRated("japanese"), "sushi")
	obj.ChangeRating("ramen", 16)
	fmt.Println(obj.HighestRated("japanese"), "ramen")
}
