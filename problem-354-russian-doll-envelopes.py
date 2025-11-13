from typing import List
import bisect


def smartass_lis_len(seq: List[int]) -> int:
    tails = [float('-inf')]

    for x in seq:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x

    return len(tails) - 1


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by second dimension descending so that in width is the same
        # we do not consider this a fit for LIS below
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        return smartass_lis_len([h for _, h in envelopes])


if __name__ == '__main__':
    x = Solution()
    print(x.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]), 3)
