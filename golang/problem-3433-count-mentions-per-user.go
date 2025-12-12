//go:build ignore

package main

import (
	"strconv"
	"strings"
)

func parseInt(s string) int {
	r, err := strconv.Atoi(s)
	if err != nil {
		panic("bad")
	}
	return r
}

func countMentions(numberOfUsers int, events [][]string) []int {
	maxT := 100100
	hereMentions := make([]int, maxT)
	goesOfflineTimes := make([][]int, numberOfUsers)

	allMentionsCount := 0
	specificMentionsMap := map[int]int{}

	for _, event := range events {
		t := parseInt(event[1])
		if event[0] == "MESSAGE" {
			ms := event[2]
			if ms == "ALL" {
				allMentionsCount += 1
			} else if ms == "HERE" {
				hereMentions[t] += 1
			} else {
				refs := strings.Split(event[2], " ")
				for _, ref := range refs {
					uid := parseInt(ref[2:])
					specificMentionsMap[uid] += 1
				}
			}
		} else if event[0] == "OFFLINE" {
			uid := parseInt(event[2])
			goesOfflineTimes[uid] = append(goesOfflineTimes[uid], t)
		}
	}

	hereMentionsPrefixSum := make([]int, maxT)
	for idx := 0; idx < len(hereMentionsPrefixSum); idx++ {
		hereMentionsPrefixSum[idx] = hereMentions[idx]
		if idx > 0 {
			hereMentionsPrefixSum[idx] += hereMentionsPrefixSum[idx-1]
		}
	}

	result := make([]int, numberOfUsers)

	for idx := range len(result) {
		result[idx] = allMentionsCount + specificMentionsMap[idx] + hereMentionsPrefixSum[maxT-1]

		// now subtract for all the ranges user was offline while here mention
		for _, offlineAt := range goesOfflineTimes[idx] {
			backOnlineAt := offlineAt + 60
			hereMentionsWhileOffline := hereMentionsPrefixSum[backOnlineAt-1]
			if offlineAt > 0 {
				hereMentionsWhileOffline -= hereMentionsPrefixSum[offlineAt-1]
			}
			result[idx] -= hereMentionsWhileOffline
		}
	}

	return result
}
