from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0

        for num in nums:
            xor ^= num

        # find the bits where two number differ
        group_bit_idx = None
        for bit_idx in range(0, 32):
            if xor & (2 ** bit_idx):
                group_bit_idx = bit_idx
                break
        else:
            assert False, 'what?'

        # group into two groups by the bit known to be different in two numbers
        # we search for
        group_a = 0
        group_b = 0

        for num in nums:
            if num & (2 ** group_bit_idx):
                group_a ^= num
            else:
                group_b ^= num


        return [group_a, group_b]


if __name__ == '__main__':
    x = Solution()
    print(x.singleNumber([1,2,1,3,2,5]))