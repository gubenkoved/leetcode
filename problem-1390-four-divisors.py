from typing import List
import math

def factorize(x):
    factors = {1, x}
    for f in range(2, int(math.sqrt(x) + 1)):
        if x % f == 0:
            factors.add(f)
            factors.add(x // f)
    return factors

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        # unimplemented observation:
        # given there are four divisors and 1 is always a divisor and itself is
        # also always a divisor we are basically looking at the following cases:
        # number is
        # X = 4 * P where P is prime as it gives 4 divisors: 1, 2, 4, K
        # X = P1 * P2 with 4 divisors: 1, P1, P2 and P1 * P2

        result = 0

        for x in nums:
            factors = factorize(x)
            if len(factors) == 4:
                result += sum(factors)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.sumFourDivisors([21,4,7]), 32)
