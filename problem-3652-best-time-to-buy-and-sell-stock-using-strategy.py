from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        # different place to apply the strategy can happen N - k + 1 times
        # however can can just do that in single pass because only a few changes
        # will be needed elements will be different between next and prev steps:
        #
        # x x x 0 0 0 0 1 1 1 1 x x x x x   <<<< prev step
        # x x x x 0 0 0 0 1 1 1 1 x x x x   <<<< new step
        #       ^       ^       ^

        n = len(prices)
        orig_prefix_sums = [0] * n

        # calculate original result
        for idx in range(n):
            cur = prices[idx] * strategy[idx]
            orig_prefix_sums[idx] = cur
            if idx > 0:
                orig_prefix_sums[idx] += orig_prefix_sums[idx-1]

        # sliding window showing result inside window of size k with updated
        # strategy
        window = 0

        # setup the first window
        for idx in range(k):
            if idx < k // 2:
                # first k / 2 are hold (0) in updated
                pass
            else:
                # last k / 2 are sell
                window += prices[idx]

        result = orig_prefix_sums[n - 1]

        # handle the first window
        result = max(
            result,
            window + (orig_prefix_sums[n-1] - orig_prefix_sums[k-1])
        )

        #       offset
        #         v
        # 0 1 2 3 4 5 6 7 8 9
        # x x x 0 0 0 0 1 1 1 1 x x x x x  << prev
        # x x x x 0 0 0 0 1 1 1 1 x x x x  << cur
        #               ^       ^
        # in order to calculate current window result from previous 2 updates
        # has to happen

        # offset is tracking offset of updated window of len k
        for offset in range(1, n - k + 1):
            # update the window
            window += prices[offset + k - 1] - prices[offset + (k // 2) - 1]

            cur_result = window

            # add original result using prefix sum (before the updated win)
            cur_result += orig_prefix_sums[offset-1]

            # ... and after the updated window
            cur_result += orig_prefix_sums[n-1]-orig_prefix_sums[offset + k - 1]

            result = max(result, cur_result)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2), 10)
