from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        starts_map = {}
        ends_map = {}
        for start, end in queries:
            if start not in starts_map:
                starts_map[start] = 0
            if end not in ends_map:
                ends_map[end] = 0
            starts_map[start] += 1
            ends_map[end] += 1

        n = len(nums)
        depth = 0

        for idx in range(n):
            depth += starts_map.get(idx, 0)

            if nums[idx] > depth:
                return False

            depth -= ends_map.get(idx, 0)

        return True


if __name__ == '__main__':
    x = Solution()
    print(x.isZeroArray(nums = [1,0,1], queries = [[0,2]]))
    print(x.isZeroArray([4,3,2,1], queries = [[1,3],[0,2]]))
    print(x.isZeroArray([1, 8], [[1,1],[0,1],[1,1],[1,1],[1,1],[0,0],[0,0],[1,1],[1,1],[1,1],[0,0],[0,1],[1,1],[1,1],[1,1]]))
