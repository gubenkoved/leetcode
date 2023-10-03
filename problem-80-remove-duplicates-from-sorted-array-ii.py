from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow, fast = 0, 1
        last_count = 0

        n = len(nums)
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                slow += 1
                nums[slow] = nums[fast]
                last_count = 1
            else:  # same element, still carry if count less than 2
                if last_count < 2:
                    slow += 1
                    nums[slow] = nums[fast]
                    last_count = 2

            fast += 1

        return slow + 1


if __name__ == '__main__':
    x = Solution()


    def case(a):
        lst = list(a)
        k = x.removeDuplicates(lst)
        print(lst)
        print(k)
        print()


    case([1, 1, 1, 2, 2, 3])
    case([1, 1, 1, 1])
