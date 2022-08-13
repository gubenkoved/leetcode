class Solution:
    # returns amount of zeros for the x!
    def zero_count(self, x):
        count = 0
        n = 5
        while n <= x:
            count += x // n
            n *= 5
        return count

    # looking at the results we can see that the result is either 5 or 0
    # so the the task can be rephrased as: figure out if there is x where
    # x! has k zeros, if positive then the answer is 5, otherwise 0
    def preimageSizeFZF(self, k: int) -> int:

        # finds a number factorial of which has exactly k zeros
        def find(left, right):
            if right - left <= 1:
                left_count = self.zero_count(left)
                right_count = self.zero_count(right)

                if left_count == k:
                    return left

                if right_count == k:
                    return right

                return None

            mid = (left + right) // 2
            mid_count = self.zero_count(mid)
            if mid_count > k:
                return find(left, mid)  # go left
            elif mid_count < k:
                return find(mid, right)
            else:
                return mid

        num = find(1, k * 5)

        if num is not None:
            return 5

        return 0


if __name__ == '__main__':
    x = Solution()
    assert x.preimageSizeFZF(0) == 5
    assert x.preimageSizeFZF(3) == 5
    assert x.preimageSizeFZF(5) == 0
