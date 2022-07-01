from typing import List


# TLE on 44/48
class Solution:
    def candy_v1(self, ratings: List[int]) -> int:
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

    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        result = [1] * n

        # forward pass
        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1] and result[idx] <= result[idx - 1]:
                result[idx] = result[idx - 1] + 1

        # backward pass
        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1] and result[idx] <= result[idx + 1]:
                result[idx] = result[idx + 1] + 1

        return sum(result)


if __name__ == '__main__':
    x = Solution()
    print(x.candy([1, 2, 2]))
    print(x.candy([1, 0, 2]))
    f = open('input.txt')
    q = eval(f.read())
    print(x.candy(q))
