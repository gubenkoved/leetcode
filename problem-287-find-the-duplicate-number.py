from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        # stage 1. find intersection point between slow and fast pointers
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]

        # stage 2. now find the "cycle entrance" by starting at start point and
        # intersection point and going with the same speed
        #
        # here is why this gives a right answer:
        # Let F be the distance from the start to the cycle entrance
        #     a be the distance from the entrance to the intersection point
        #     C length of the cycle
        #
        #        cycle          v-------- intersection point
        #      entrance-\   ----X---      (a) hops from the cycle start
        #                \ /         \
        #       -----------          |
        #           ^      \        /
        #           |       --------
        #           F
        #
        # Then we can say the following from the first pass:
        # Slow pointer traversed (F + a) units and
        # the fast one traversed (F + a + n * C) units, where n is some positive integer
        # Given fast pointer traversed twice as much we can say that:
        #
        #              2 * (F + a) = F + a + n * C, which is equivalent to
        #              F + a = n * C
        #
        # Now let us consider what will happen if we start the first pointer
        # from the very start and the second pointer will start from the intersection
        # and both pointers will make F hops
        # First pointer will reach the cycle entrance at F
        # Second pointer will start at (F + a) distance from the start and make;
        # F more hops with total distance equal to (F + a + F);
        #
        # From the equation above we can replace (F + a) with n * C and it gives:
        #
        #                 F + n * C
        #
        # Which means that the second pointer will be exactly at cycle entrance plus
        # some amount of cycles which means it will coincide with the first pointer;
        #
        # So we will use this condition (pointers colliding) as the stop condition
        # for the second stage;

        ptr1, ptr2 = 0, slow

        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1


if __name__ == '__main__':
    x = Solution()
    print(x.findDuplicate([1, 3, 4, 2, 2]))
    print(x.findDuplicate([3, 1, 3, 4, 2]))
    print(x.findDuplicate([2, 5, 9, 6, 9, 3, 8, 9, 7, 1]))
