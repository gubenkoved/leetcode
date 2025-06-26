class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # start from the right side and extend the resulting sequence while
        # it still less than k greedily
        idx = len(s) - 1
        while idx > 0 and int(s[idx - 1:], 2) <= k:
            idx -= 1

        # and then add all the zeros from the left side
        result = len(s) - idx

        idx -= 1

        while idx >= 0:
            result += 1 if s[idx] == '0' else 0
            idx -= 1

        return result

if __name__ == '__main__':
    x = Solution()
    print(x.longestSubsequence("1001010", k = 5))
    print(x.longestSubsequence("00101001", k = 1))
