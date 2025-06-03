from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1 = sum(nums1)
        z1 = nums1.count(0)

        s2 = sum(nums2)
        z2 = nums2.count(0)

        # check absolute minimum sums
        ss1 = s1 + z1
        ss2 = s2 + z2

        # if smaller array has at least one zero, we can always make the sum equal

        if ss1 == ss2:
            return ss1
        elif ss1 < ss2:
            if z1 == 0:
                return -1
            return ss2
        else:
            if z2 == 0:
                return -1
            return ss1


if __name__ == '__main__':
    x = Solution()
    # print(x.minSum([8,13,15,18,0,18,0,0,5,20,12,27,3,14,22,0], [29,1,6,0,10,24,27,17,14,13,2,19,2,11]))
    print(x.minSum([0,16,28,12,10,15,25,24,6,0,0], [20,15,19,5,6,29,25,8,12]))