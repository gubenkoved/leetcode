from typing import List


def x_sum(x, arr):
    counter = {}
    for k in arr:
        if k not in counter:
            counter[k] = 0
        counter[k] += 1

    inv = [(freq, k) for k, freq in counter.items()]
    inv.sort()

    return sum(freq * k for freq, k in inv[-x:])

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        return [x_sum(x, nums[i:i + k]) for i in range(len(nums) - k + 1)]


if __name__ == '__main__':
    x = Solution()
    print(x.findXSum([1,1,2,2,3,4,2,3], k = 6, x = 2))
