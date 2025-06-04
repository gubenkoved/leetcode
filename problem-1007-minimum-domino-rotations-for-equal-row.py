from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        result = -1
        for q in range(1, 7):
            t_count = 0
            b_count = 0
            works = True
            for idx in range(n):
                if tops[idx] != q and bottoms[idx] != q:
                    works = False
                t_count += 1 if tops[idx] == q else 0
                b_count += 1 if bottoms[idx] == q else 0
            if works:
                cur_result = min(n - t_count, n - b_count)
                if cur_result < result or result == -1:
                    result = cur_result
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minDominoRotations([6,1,6,4,6,6], [5,6,2,6,3,6]))
