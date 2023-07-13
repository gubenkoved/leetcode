from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        def is_set(number, bit_idx):
            return number & (2 ** bit_idx)

        bit_counters = [0] * 32
        for x in nums:
            for bit_idx in range(0, 32):
                if is_set(x, bit_idx):
                    bit_counters[bit_idx] += 1

        # restore the single number
        result = 0
        for bit_idx in range(0, 32):
            if bit_counters[bit_idx] % 3 == 1:
                # see https://en.wikipedia.org/wiki/Two%27s_complement
                # if sign bit is set we have to subtract the exponent value to get
                # the real number
                if bit_idx != 31:
                    result += 2 ** bit_idx
                else:
                    result -= 2 ** bit_idx

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.singleNumber([1, 3, 1, 1]))
    print(x.singleNumber([4]))
    print(x.singleNumber([1, 2, 3, 1, 2, 3, 1, 2, 3, 7, ]))
    print(x.singleNumber([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]))
