from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}
        for idx, x in enumerate(nums):
            idx_map[x] = idx
        for idx, x in enumerate(nums):
            compl_idx = idx_map.get(target - x)
            if compl_idx and compl_idx != idx:
                return [idx, compl_idx]
        raise RuntimeError()


if __name__ == '__main__':
    x = Solution()
    print(x.twoSum([1, 3, 4, 2], 6))
