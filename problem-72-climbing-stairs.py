from functools import lru_cache


class Solution:
    @lru_cache()
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1

        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == '__main__':
    x = Solution()
    for v in range(100):
        print('%d -> %d' % (v, x.climbStairs(v)))
