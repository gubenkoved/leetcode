from typing import List


# given there are only 14 words, it seems like we can just brute force it
# as there are only 2^14 (16K) different subsets there
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        letter_counts = {}

        for letter in letters:
            if letter not in letter_counts:
                letter_counts[letter] = 0
            letter_counts[letter] += 1

        letter_to_score = {}
        for letter_idx, letter_score in enumerate(score):
            letter_to_score[chr(letter_idx + ord('a'))] = letter_score

        word_to_letter_count_map = {}
        word_to_score_map = {}

        for word in words:
            word_counts = {}
            word_score = 0
            for letter in word:
                if letter not in word_counts:
                    word_counts[letter] = 0
                word_counts[letter] += 1
                word_score += letter_to_score[letter]
            word_to_letter_count_map[word] = word_counts
            word_to_score_map[word] = word_score

        # max_score will be recursive with pos starting from 0 to N, and it will
        # facilitate trying all the combinations
        def max_score(pos):
            if pos == len(words):
                return 0

            # null-case -- not taking this word, go to the next one
            best = max_score(pos + 1)

            # check if I can take the word
            word = words[pos]
            needed_letters_map = word_to_letter_count_map[word]
            can_take = all(
                letter_counts.get(letter, 0) >= needed
                for letter, needed in needed_letters_map.items()
            )

            if can_take:
                # take the letters!
                for letter, needed in needed_letters_map.items():
                    letter_counts[letter] -= needed

                best = max(best, word_to_score_map[word] + max_score(pos + 1))

                # return the letters!
                for letter, needed in needed_letters_map.items():
                    letter_counts[letter] += needed


            return best

        return max_score(0)


if __name__ == '__main__':
    x = Solution()
    print(x.maxScoreWords(words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]))
    # print(x.maxScoreWords(words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]))
