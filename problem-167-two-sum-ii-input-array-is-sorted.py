from typing import List
import bisect


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for idx in range(n - 1):
            idx2 = bisect.bisect_left(numbers, target - numbers[idx], idx + 1)
            if idx2 < n and numbers[idx2] == target - numbers[idx]:
                return [idx + 1, idx2 + 1]
        assert False, 'No solution found'


if __name__ == '__main__':
    x = Solution()
    assert x.twoSum([2, 7, 11, 15], target=9) == [1, 2]
    assert x.twoSum([2, 3, 4], target=6) == [1, 3]
    assert x.twoSum([-1, 0], target=-1) == [1, 2]
