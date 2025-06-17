import math

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        result = m

        for x in range(n - k - 1):
            result *= m - 1
            result %= mod

        result *= math.comb(n - 1, k) % mod
        return result % mod


if __name__ == '__main__':
    x = Solution()
    print(x.countGoodArrays(3, 2, 1))
    print(x.countGoodArrays(4, 2, 2))
    print(x.countGoodArrays(10000, 10000, 5000))
