class Solution:
    def smallestNumber(self, n: int) -> int:
        bl = n.bit_length()
        result = 0
        for b_idx in range(bl):
            result |= 1 << b_idx
        return result
