class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        m = 5
        while m <= n:
            result += n // m
            m *= 5
        return result


if __name__ == '__main__':
    x = Solution()

    assert x.trailingZeroes(30) == 7
    assert x.trailingZeroes(3) == 0
    assert x.trailingZeroes(5) == 1
    assert x.trailingZeroes(10) == 2
