package main

import (
	"fmt"
	"sort"
)

// dynamic circular buffer that can grow like a dynamic array exponentially so that
// amortized complexity is still low
type CircularBuffer[T any] struct {
	buffer      []T
	consumerIdx int
	producerIdx int
	isFixedSize bool
}

func CreateCircularBuffer[T any](size int, isFixedSize bool) *CircularBuffer[T] {
	return &CircularBuffer[T]{
		buffer:      make([]T, size),
		consumerIdx: 0,
		producerIdx: 0,
		isFixedSize: isFixedSize,
	}
}

// return overwritten element if we evicted, and is_evicted flag
func (cb *CircularBuffer[T]) AddElement(element T) (T, bool) {
	if cb.isFixedSize {
		var evicted T
		is_evicted := false

		if cb.producerIdx-cb.consumerIdx == len(cb.buffer) {
			evicted = cb.buffer[cb.consumerIdx%len(cb.buffer)]
			is_evicted = true
		}

		cb.buffer[cb.producerIdx%len(cb.buffer)] = element
		cb.producerIdx += 1

		// buffer overflow tracking
		if cb.producerIdx-cb.consumerIdx > len(cb.buffer) {
			cb.consumerIdx += 1
		}

		return evicted, is_evicted
	} else {
		if cb.producerIdx-cb.consumerIdx == len(cb.buffer) {
			// need to grow buffer
			new_buffer := make([]T, len(cb.buffer)*2)
			copy(new_buffer, cb.buffer)
			cb.buffer = new_buffer
		}

		cb.buffer[cb.producerIdx%len(cb.buffer)] = element
		cb.producerIdx += 1

		// we never overflow for this type of buffer
		var ret T
		return ret, false
	}
}

// TODO: need to shrink if fill factor goes below given value (like 10%) for
// dynamically sized case
func (cb *CircularBuffer[T]) PopElement() T {
	if cb.consumerIdx == cb.producerIdx {
		panic("nothing more to consume")
	}

	element := cb.buffer[cb.consumerIdx%len(cb.buffer)]
	cb.consumerIdx += 1
	return element
}

func (cb *CircularBuffer[T]) CountElements() int {
	return cb.producerIdx - cb.consumerIdx
}

// assuming sorted order in the buffer returns the first index of element
// which turns the function f to true
func (cb *CircularBuffer[T]) SearchIndexOf(f func(T) bool) int {
	offset := sort.Search(cb.producerIdx-cb.consumerIdx, func(offset int) bool {
		idx := (cb.consumerIdx + offset) % len(cb.buffer)
		return f(cb.buffer[idx])
	})
	return cb.consumerIdx + offset
}

func (cb *CircularBuffer[T]) At(idx int) T {
	return cb.buffer[idx%len(cb.buffer)]
}

type Packet struct {
	source      int
	destination int
	timestamp   int
}

type Router struct {
	buffer                *CircularBuffer[Packet]
	perDestinationBuffers map[int]*CircularBuffer[Packet]
	detector              map[Packet]bool
}

func Constructor(memoryLimit int) Router {
	return Router{
		buffer:                CreateCircularBuffer[Packet](memoryLimit, true),
		perDestinationBuffers: make(map[int]*CircularBuffer[Packet]),
		detector:              make(map[Packet]bool),
	}
}

func (this *Router) AddPacket(source int, destination int, timestamp int) bool {
	packet := Packet{
		source:      source,
		destination: destination,
		timestamp:   timestamp,
	}

	if this.detector[packet] {
		return false
	}

	// add a new packet
	this.detector[packet] = true
	evicted, is_evicted := this.buffer.AddElement(packet)

	// per destination buffers are dynamic in order to NOT preallocate
	// a lot of memory
	if this.perDestinationBuffers[destination] == nil {
		this.perDestinationBuffers[destination] = CreateCircularBuffer[Packet](16, false)
	}

	this.perDestinationBuffers[destination].AddElement(packet)

	if is_evicted {
		this.perDestinationBuffers[evicted.destination].PopElement()
	}

	return true
}

func (this *Router) ForwardPacket() []int {
	if this.buffer.CountElements() == 0 {
		return []int{}
	}

	packet := this.buffer.PopElement()

	// drop from detector
	delete(this.detector, packet)

	// update per destination buffer as well
	this.perDestinationBuffers[packet.destination].PopElement()

	return []int{
		packet.source,
		packet.destination,
		packet.timestamp,
	}
}

func (this *Router) GetCount(destination int, startTime int, endTime int) int {
	// binary search over the circular buffer
	// note: left index we search as first element with timestamp >= startTime
	// but last indexes we need the first index which timestamp >= endTime + 1
	// so that we calculate all the occurrences of the endTime

	buffer := this.perDestinationBuffers[destination]

	if buffer == nil {
		return 0
	}

	start_idx := buffer.SearchIndexOf(func(packet Packet) bool {
		return packet.timestamp >= startTime
	})
	end_idx := buffer.SearchIndexOf(func(packet Packet) bool {
		return packet.timestamp >= endTime+1
	})

	return end_idx - start_idx
}

/**
 * Your Router object will be instantiated and called as such:
 * obj := Constructor(memoryLimit);
 * param_1 := obj.AddPacket(source,destination,timestamp);
 * param_2 := obj.ForwardPacket();
 * param_3 := obj.GetCount(destination,startTime,endTime);
 */

func main() {
	// router := Constructor(10)
	// fmt.Println([]any{
	// 	router.AddPacket(1, 2, 1),
	// 	router.ForwardPacket(),
	// 	router.AddPacket(2, 3, 2),
	// 	router.AddPacket(3, 3, 2),
	// 	router.AddPacket(4, 3, 3),
	// 	router.GetCount(3, 1, 10),
	// 	router.ForwardPacket(),
	// 	router.GetCount(3, 1, 10),
	// 	router.ForwardPacket(),
	// 	router.GetCount(3, 1, 10),
	// 	router.ForwardPacket(),
	// 	router.GetCount(3, 1, 10),
	// })

	// ["Router","addPacket","addPacket","addPacket","getCount","forwardPacket","forwardPacket","forwardPacket"]
	// [[2],[1,5,1],[2,5,1],[1,2,1],[2,1,1],[],[],[]]

	router := Constructor(2)
	fmt.Println([]any{
		router.AddPacket(1, 5, 1),
		router.AddPacket(2, 5, 1),
		router.AddPacket(1, 2, 1),
		router.GetCount(2, 1, 1),
		router.ForwardPacket(),
		router.ForwardPacket(),
		router.ForwardPacket(),
	})
}
