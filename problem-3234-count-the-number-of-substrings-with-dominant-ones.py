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

        # another optimization -- when I have given amount of ones and zeros
        # at a given step we can actually skip some of the steps if we assume
        # that ALL of the next K values would be zero, and we still be dominant;
        # for instance, in subrange there are 10 ones, and 0 zeros, we can
        # step at least next 3 and be sure ALL of them are dominant, because
        # if all were zeros, we would then have 10 ones, 3 zeros, still dominant
        # (may be this logic is better applies to count non dominant, as we can
        # skip much more!)

        # ranges are inclusive
        for i in range(n):
            j = i
            while j < n:
                ones = ones_count[j]

                if i > 0:
                    ones -= ones_count[i - 1]

                zeros = j - i + 1 - ones

                if ones >= zeros * zeros:
                    # how much can we step?
                    #
                    # ones >= (zeros + K) ^ 2
                    # sqrt(ones) >= zeros + K
                    # K <= sqrt(ones) - zeros
                    K = math.floor(math.sqrt(ones) - zeros)

                    # make sure we do not go out of range
                    K = min(K, n - j - 1)

                    j += K + 1
                    result += K + 1
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
