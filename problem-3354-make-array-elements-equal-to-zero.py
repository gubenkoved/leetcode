from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)

        def sim(data: List[int], pos: int, direction: int) -> bool:
            while True:
                pos = pos + direction

                if pos < 0 or pos >= n:
                    # out of range
                    return all(x == 0 for x in data)

                if data[pos] > 0:
                    data[pos] -= 1
                    direction *= -1

        result = 0
        for idx in range(n):
            if nums[idx] == 0:
                if sim(list(nums), idx, +1):
                    result += 1
                if sim(list(nums), idx, -1):
                    result += 1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.countValidSelections([1,0,2,0,3]), 2)
