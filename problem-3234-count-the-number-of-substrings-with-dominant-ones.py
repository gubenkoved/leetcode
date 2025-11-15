import math

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        sqrt_n = math.sqrt(n)
        ones_count = [0] * n

        for idx in range(n):
            ones_count[idx] = 1 if s[idx] == '1' else 0
            if idx > 0:
                ones_count[idx] += ones_count[idx - 1]

        result = 0

        # if amount of zeros bigger than sqrt(n), then range can not be dominant
        # anymore as this amount squared would be bigger than n itself, so for
        # each starting index only attempt while amount of zeros is less than or
        # equal than that

        # ranges are inclusive
        for i in range(n):
            for j in range(i, n):
                ones = ones_count[j]
                if i > 0:
                    ones -= ones_count[i - 1]
                zeros = j - i + 1 - ones
                if ones >= zeros * zeros:
                    result += 1
                if zeros > sqrt_n:
                    break

        return result