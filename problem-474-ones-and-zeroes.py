from typing import List
import functools


class Solution:
    # up to m zeros, n ones
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        # int to count of zeros and ones
        def count_zeros_ones(x: str) -> tuple[int, int]:
            zeros_count = sum(1 for c in x if c == '0')
            ones_count = sum(1 for c in x if c == '1')
            return zeros_count, ones_count

        counts = [count_zeros_ones(str) for str in strs]

        # DP: using first K elements, max_zeros and max_ones in numbers
        @functools.cache
        def f(k: int, max_zeros: int, max_ones: int) -> int:
            if k == -1:
                return 0

            zeros, ones = counts[k]

            # can pick k-th?
            if max_zeros >= zeros and max_ones >= ones:
                best = 1 + f(k - 1, max_zeros - zeros, max_ones - ones)
            else:
                best = 0

            # do not pick k-th
            best = max(best, f(k - 1, max_zeros, max_ones))

            return best

        return f(len(strs) - 1, m, n)


if __name__ == '__main__':
    x = Solution()
    print(x.findMaxForm(["10","0001","111001","1","0"], 5, 3), 4)
