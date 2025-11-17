from typing import List

class Solution:
    # value is in 1..10^5
    # len(nums) is in 1..10^5 as well
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # counts of numbers in source array mod value -- this is because all
        # values with same reminder modulo value are interchangeable when it
        # comes to getting any other number with same modulo
        mod_counter = {}

        for num in nums:
            mod = num % value
            if mod not in mod_counter:
                mod_counter[mod] = 0
            mod_counter[mod] += 1

        # iterate over the result and see if which is the first number we
        # will not be able to get
        for x in range(len(nums) + 1):
            mod = x % value

            if mod_counter.get(mod, 0) == 0:
                return x

            mod_counter[mod] -= 1

        assert False
