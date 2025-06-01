from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        result = []
        idx, group = 0, groups[0]

        stop = False
        while not stop:
            group = groups[idx]
            result.append(words[idx])

            while groups[idx] == group:
                idx += 1

                if idx == n:
                    stop = True
                    break

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.getLongestSubsequence(words = ["e","a","b"], groups = [0,0,1]))
