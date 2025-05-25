from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = {}

        # count all the words
        for word in words:
            if word not in m:
                m[word] = 0
            m[word] += 1

        def reverse(word: str) -> str:
            return ''.join(word[::-1])

        result = 0

        # paired words can be computed lazily
        for word in words:
            if m[word] == 0:
                continue

            reversed_word = reverse(word)

            if word != reversed_word:
                if m.get(reversed_word, 0) > 0:
                    # paired!
                    result += len(word) + len(reversed_word)
                    m[reversed_word] -= 1
                    m[word] -= 1
            else:  # same word
                if m[word] >= 2:
                    result += len(word) * 2
                    m[word] -= 2

        # now at the very center we can add up to 1 uncompensated word
        #  if it is symmetrical
        for word in words:
            if m[word] == 0:
                continue

            if word == reverse(word):
                result += len(word)
                # only single one is possible w/o loosing symmetry
                break

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.longestPalindrome(["lc","cl","gg"]))
    print(x.longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
    print(x.longestPalindrome(["cc","ll","xx"]))