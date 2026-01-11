from functools import cache

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        @cache
        def f(i, j):
            if i == len(s1):
                return sum(ord(x) for x in s2[j:])

            if j == len(s2):
                return sum(ord(x) for x in s1[i:])

            if s1[i] == s2[j]:
                return f(i + 1, j + 1)

            return min(
                f(i + 1, j) + ord(s1[i]),
                f(i, j + 1) + ord(s2[j]),
            )

        return f(0, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.minimumDeleteSum(s1 = "sea", s2 = "eat"), 231)
    print(x.minimumDeleteSum(s1 = "delete", s2 = "leet"), 403)
