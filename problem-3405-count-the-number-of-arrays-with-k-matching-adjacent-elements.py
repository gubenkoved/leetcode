import math

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        result = m * ((m - 1) ** (n - k - 1)) * math.comb(n - 1, k)
        return result % mod


if __name__ == '__main__':
    x = Solution()
    print(x.countGoodArrays(3, 2, 1))
    print(x.countGoodArrays(4, 2, 2))
