from typing import List


# TLE on 44/48
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n
        changed = True
        while changed:
            changed = False
            for idx in range(0, n):
                if idx > 0 and ratings[idx] > ratings[idx - 1] and result[idx] <= result[idx - 1]:
                    result[idx] += 1
                    changed = True
                if idx < n - 1 and ratings[idx] > ratings[idx + 1] and result[idx] <= result[idx + 1]:
                    result[idx] += 1
                    changed = True
        return sum(result)


if __name__ == '__main__':
    x = Solution()
    print(x.candy([1, 2, 2]))
    print(x.candy([1, 0, 2]))
