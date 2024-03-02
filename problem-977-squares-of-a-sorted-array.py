from typing import List


class Solution:
    # O(n logn) but actually works faster for the test cases...
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x ** 2 for x in nums])

    # solves follow up in O(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # can be binary search, but does not change asymptotic
        # find index of the element which is closest to 0 by absolute value
        center = min(enumerate(nums), key=lambda t: abs(t[1]))[0]
        left, right = center - 1, center + 1
        result = [nums[center] ** 2]
        n = len(nums)

        # now we move left and right similar to merge sort yielding the result
        while left >= 0 or right < n:
            if left < 0:
                go_left = False
            elif right >= n:
                go_left = True
            else:
                go_left = abs(nums[left]) < abs(nums[right])

            if go_left:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.sortedSquares([-4,-1,0,3,10]))