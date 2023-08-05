from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        possible = set()
        possible.add(nums[0])
        result = max(possible)

        for idx in range(1, len(nums)):
            new_possible = {nums[idx]}
            for prev in possible:
                new_possible.add(prev * nums[idx])
            possible = new_possible
            result = max(result, max(possible))

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxProduct([2, 3, -2, 4]))
    print(x.maxProduct([-2]))
    print(x.maxProduct([-2, 3]))
    print(x.maxProduct([-2, 3, 4]))
    print(x.maxProduct([-2, 3, -4]))
    print(x.maxProduct([2, -5, -2, -4, 3]))
