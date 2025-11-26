package main

import (
	"fmt"
	"sort"
)

type Packet struct {
	source      int
	destination int
	timestamp   int
}

type Router struct {
	// circular buffer of packets
	buffer      []Packet
	consumerIdx int
	producerIdx int
	detector    map[Packet]bool
}

func Constructor(memoryLimit int) Router {
	return Router{
		buffer:      make([]Packet, memoryLimit),
		consumerIdx: 0,
		producerIdx: 0,
		detector:    make(map[Packet]bool),
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
	this.buffer[this.producerIdx%len(this.buffer)] = packet
	this.producerIdx += 1

	// buffer overflow tracking
	if this.producerIdx-this.consumerIdx > len(this.buffer) {
		this.consumerIdx += 1
	}

	return true
}

func (this *Router) ForwardPacket() []int {
	if this.consumerIdx == this.producerIdx {
		return []int{}
	}
	packet := this.buffer[this.consumerIdx%len(this.buffer)]
	this.consumerIdx += 1

	// drop from detector
	delete(this.detector, packet)

	return []int{
		packet.source,
		packet.destination,
		packet.timestamp,
	}
}

// TODO: how to calculate this per destination efficiently? do we need per destination buffer?
func (this *Router) GetCount(destination int, startTime int, endTime int) int {
	// binary search over the circular buffer
	// note: left index we search as first element with timestamp >= startTime
	// but last indexes we need the first index which timestamp >= endTime + 1
	// so that we calculate all the occurrences of the endTime
	start_offset := sort.Search(this.producerIdx-this.consumerIdx, func(offset int) bool {
		idx := (this.consumerIdx + offset) % len(this.buffer)
		return this.buffer[idx].timestamp >= startTime
	})
	end_offset := sort.Search(this.producerIdx-this.consumerIdx, func(offset int) bool {
		idx := (this.consumerIdx + offset) % len(this.buffer)
		return this.buffer[idx].timestamp >= endTime+1
	})

	// filter per destination now?
	count := 0
	for offset := start_offset; offset < end_offset; offset++ {
		packet := this.buffer[(this.consumerIdx+offset)%len(this.buffer)]
		if packet.destination == destination {
			count += 1
		}
	}

	return count
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
