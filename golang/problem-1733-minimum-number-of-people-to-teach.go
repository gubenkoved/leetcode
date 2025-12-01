//go:build ignore

package main

import "fmt"

func minimumTeachings(n int, languages [][]int, friendships [][]int) int {
	humanToLanguageMap := map[int]map[int]bool{}

	for idx, humanLangs := range languages {
		humanToLanguageMap[idx+1] = map[int]bool{}
		for _, lang := range humanLangs {
			humanToLanguageMap[idx+1][lang] = true
		}
	}

	share_language_pairs := map[[2]int]bool{}

	for _, f_pair := range friendships {
		f1 := f_pair[0]
		f2 := f_pair[1]

		share_lang := false
		for f1lang := range humanToLanguageMap[f1] {
			if humanToLanguageMap[f2][f1lang] {
				share_lang = true
				break
			}
		}

		if share_lang {
			share_language_pairs[[...]int{f1, f2}] = true
			share_language_pairs[[...]int{f2, f1}] = true
		}
	}

	best := len(languages)
	for lang := 1; lang <= n; lang++ {
		needToTeach := map[int]bool{}

		for _, f_pair := range friendships {
			f1 := f_pair[0]
			f2 := f_pair[1]

			if share_language_pairs[[...]int{f1, f2}] {
				continue
			}

			if !humanToLanguageMap[f1][lang] {
				needToTeach[f1] = true
			}
			if !humanToLanguageMap[f2][lang] {
				needToTeach[f2] = true
			}
		}
		best = min(best, len(needToTeach))
	}
	return best
}

func main() {
	fmt.Println(minimumTeachings(2, [][]int{{1}, {2}, {1, 2}}, [][]int{{1, 2}, {1, 3}, {2, 3}}), 1)
	fmt.Println(minimumTeachings(5, [][]int{{1}, {5}, {1, 5}, {5}}, [][]int{{1, 2}, {1, 3}, {1, 4}, {2, 3}}), 1)
}
