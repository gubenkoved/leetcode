# Given two strings word1 and word2, return the minimum number of
# operations required to convert word1 to word2.
#
# You have the following three operations permitted on a word:
#
# > Insert a character
# > Delete a character
# > Replace a character

from functools import lru_cache


class Solution:
    def minDistance_tle(self, word1: str, word2: str) -> int:
        # compute the worst case distance
        best_distance = abs(len(word1) - len(word2))
        for idx in range(min(len(word1), len(word2))):
            if word1[idx] != word2[idx]:
                best_distance += 1

        def find(a, b, cur_distance) -> None:
            nonlocal best_distance

            if cur_distance >= best_distance:
                return

            if a == b:
                if cur_distance < best_distance:
                    print(f'updated best distance to {cur_distance}')
                    best_distance = cur_distance
                return

            # try replacing char
            for replace_at in range(min(len(a), len(b))):
                if a[replace_at] == b[replace_at]:
                    continue
                a_new = a[:replace_at] + b[replace_at] + a[replace_at+1:]
                find(a_new, b, cur_distance + 1)

            # try removing character in "a"
            if len(a) >= len(b):
                for remove_at in range(len(a)):
                    a_new = a[:remove_at] + a[remove_at+1:]
                    find(a_new, b, cur_distance + 1)

            # try removing char in "b" (equivalent to inserting into "a")
            if len(b) >= len(a):
                for remove_at in range(len(b)):
                    b_new = b[:remove_at] + b[remove_at+1:]
                    find(a, b_new, cur_distance + 1)

        find(word1, word2, 0)

        return best_distance

    # after looking for an answer
    def minDistance(self, word1: str, word2: str) -> int:

        @lru_cache(None)
        def find(i: int, j: int) -> int:
            if i == len(word1):
                return len(word2) - j

            if j == len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return find(i + 1, j + 1)

            return min(
                # insert
                1 + find(i, j + 1),
                # replace
                1 + find(i + 1, j + 1),
                # delete
                1 + find(i + 1, j),
            )

        return find(0, 0)


if __name__ == '__main__':
    x = Solution()
    assert x.minDistance('horse', 'horse') == 0
    assert x.minDistance('horse', 'hors') == 1
    assert x.minDistance('horse', 'horses') == 1
    assert x.minDistance('horse', 'ros') == 3
    assert x.minDistance('abcdef', '0abcde') == 2
    assert x.minDistance('0abcdef', 'abcdefg') == 2
    assert x.minDistance('bcdef', 'abcdef') == 1
    assert x.minDistance('intention', 'execution') == 5
    assert x.minDistance('plasma', 'altruism') == 6
    assert x.minDistance('industry', 'interest') == 6
