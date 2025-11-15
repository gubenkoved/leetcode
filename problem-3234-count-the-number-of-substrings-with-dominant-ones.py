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
        # equal than that;

        # next_zero[idx] should return index of next (to the right zero) or
        # None if it does not exist
        next_zero = [None] * n

        nz = None
        for idx in range(n - 1, -1, -1):
            next_zero[idx] = nz
            if s[idx] == '0':
                nz = idx

        # ranges are inclusive
        for i in range(n):
            j = i
            while j < n:
                ones = ones_count[j]

                if i > 0:
                    ones -= ones_count[i - 1]

                zeros = j - i + 1 - ones

                if ones >= zeros * zeros:
                    # go to the next zero, as ones would still count as we only
                    # increase dominance
                    if next_zero[j] is None:
                        # all the way to the end are dominant
                        result += n - j
                        break
                    else:
                        result += next_zero[j] - j
                        j = next_zero[j]
                else:
                    j += 1

                # no longer possible to have dominant
                if zeros > sqrt_n:
                    break

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.numberOfSubstrings('111'))
    print(x.numberOfSubstrings('11111'))
