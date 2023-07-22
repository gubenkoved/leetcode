from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # stage 1: find a first pair from the right where inverse will increase
        # stage 2: sort all numbers in increasing order after the first number which
        #          was changed

        n = len(nums)

        if n <= 1:
            return

        found = False
        for l in range(n - 2, -1, -1):
            for r in range(n - 1, l, -1):
                if nums[l] < nums[r]:
                    found = True
                    break
            if found:
                break

        # this is simple O(n^2) sort, can be replaced by Quick Sort
        def sort_after(idx):
            for left_idx in range(idx + 1, n - 1):
                for right_idx in range(left_idx + 1, n):
                    if nums[left_idx] > nums[right_idx]:
                        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

        if not found:
            sort_after(-1)  # complete sort
            return

        # swap l and r elements and sort everything behind the l lexicographically
        nums[l], nums[r] = nums[r], nums[l]
        sort_after(l)

    # wikipedia suggests simpler algorithm, subset of what I intuited
    # https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # stage 1: find a first pair at indexes (k, k+1) where nums[k] < nums[k+1]
        #          then find the largest index r where nums[r] > nums[l] and swap
        # stage 2: reverse all numbers from k+1 till the end

        n = len(nums)

        if n <= 1:
            return

        found = False
        for k in range(n - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                found = True
                break

        def reverse_after(idx):
            left, right = idx + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if not found:
            reverse_after(-1)  # complete reverse
            return

        # find the largest index r where nums[r] > nums[k]
        for r in range(n - 1, k, -1):
            if nums[r] > nums[k]:
                break

        # swap k and r elements and then reverse everything after k
        nums[k], nums[r] = nums[r], nums[k]
        reverse_after(k)


if __name__ == '__main__':
    x = Solution()

    def case(arr):
        input_ = list(arr)
        x.nextPermutation(input_)
        print(input_)
        return input_

    case([1, 2, 3])  # [1, 3, 2]
    case([1, 3, 2])  # [2, 1, 3]
    case([2, 1, 3])  # [2, 3, 1]
    case([2, 3, 1])  # [3, 1, 2]
    case([3, 1, 2])  # [3, 2, 1]
    case([3, 2, 1])  # [1, 2, 3]

    case([4, 2, 0, 2, 3, 2, 0])  # [4, 2, 0, 3, 0, 2, 2]
