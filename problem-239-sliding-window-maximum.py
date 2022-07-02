from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        print(f'n={n}')
        result = []
        for idx in range(k, n + 1):
            window = sorted(nums[idx - k:idx])
            result.append(max(window))
        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
    f = open('input.txt')
    a = eval(f.read())
    print(x.maxSlidingWindow(a, k=50000))
