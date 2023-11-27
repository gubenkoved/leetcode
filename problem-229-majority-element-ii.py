from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 2:
            return list(set(nums))

        # find two most frequent elements first considering the answer is
        # always up to two elements
        vals = [None, None]
        balance = [0, 0]

        for x in nums:
            if x == vals[0]:
                balance[0] += 1
            elif x == vals[1]:
                balance[1] += 1
            elif balance[0] == 0:
                vals[0] = x
                balance[0] = 1
            elif balance[1] == 0:
                vals[1] = x
                balance[1] = 1
            else:
                balance[0] -= 1
                balance[1] -= 1

        return [x for x in vals if nums.count(x) > n / 3]


if __name__ == '__main__':
    x = Solution()

    assert x.majorityElement([1, 2, 3]) == []
    assert x.majorityElement([1]) == [1]
    assert x.majorityElement([1, 2]) == [1, 2]
    assert x.majorityElement([1, 1, 1, 2, 2, 2, 3]) == [1, 2]
    assert x.majorityElement([1, 2, 1, 3, 1, 4, 1]) == [1]
    assert x.majorityElement([2, 2]) == [2]
    assert x.majorityElement([1, 3, 3, 4]) == [3]
    assert x.majorityElement([3, 3, 1, 1, 1, 1, 2, 4, 4, 3, 3, 3, 4, 4]) == [3]
    assert x.majorityElement([2, 1, 1, 3, 1, 4, 5, 6]) == [1]
    assert x.majorityElement([1] * 30 + [2] * 30 + [3] * 40) == [3]
    assert x.majorityElement([2, 1, 1, 3, 1, 4, 5, 6]) == [1]
