from typing import List
import heapq


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # hi is min heap of top half, and low is max heap is lower half
        hi, low = [], []

        # counts of elements that should not be accounted when rebalancing
        # as out of the window
        extra_hi_count, extra_low_count = 0, 0

        # idx -> True if it was placed into high bucket
        is_high = {}

        # add first k elements
        for idx in range(k):
            if not hi and not low:
                heapq.heappush(hi, (nums[idx], idx))
                is_high[idx] = True
            else:
                if low and nums[idx] <= -low[0][0] or hi and nums[idx] < hi[0][0]:
                    heapq.heappush(low, (-nums[idx], idx))
                    is_high[idx] = False
                else:
                    heapq.heappush(hi, (nums[idx], idx))
                    is_high[idx] = True

            # balance out
            if len(hi) > len(low) + 1:
                popped, popped_idx = heapq.heappop(hi)
                heapq.heappush(low, (-popped, popped_idx))
                is_high[popped_idx] = False
            elif len(low) > len(hi) + 1:
                popped, popped_idx = heapq.heappop(low)
                heapq.heappush(hi, (-popped, popped_idx))
                is_high[popped_idx] = True

        def get_median():
            low_count = len(low) - extra_low_count
            high_count = len(hi) - extra_hi_count

            assert abs(low_count - high_count) <= 1

            if low_count == high_count:
                return (hi[0][0] + -low[0][0]) / 2.0
            elif high_count > low_count:
                return hi[0][0]
            else:
                return -low[0][0]

        medians = []
        medians.append(get_median())

        # process windows
        for idx in range(k, len(nums)):
            drop_idx = idx - k

            if low and nums[idx] > -low[0][0] or hi and nums[idx] >= hi[0][0]:
                heapq.heappush(hi, (nums[idx], idx))
                is_high[idx] = True
            else:
                heapq.heappush(low, (-nums[idx], idx))
                is_high[idx] = False

            if is_high[drop_idx]:
                extra_hi_count += 1
            else:
                extra_low_count += 1

            # rebalance
            while True:
                hi_count = len(hi) - extra_hi_count
                low_count = len(low) - extra_low_count

                if hi_count > low_count + 1:
                    popped, popped_idx = heapq.heappop(hi)
                    if idx - popped_idx >= k:
                        extra_hi_count -= 1
                    else:
                        heapq.heappush(low, (-popped, popped_idx))
                        is_high[popped_idx] = False
                elif low_count > hi_count + 1:
                    popped, popped_idx = heapq.heappop(low)
                    if idx - popped_idx >= k:
                        extra_low_count -= 1
                    else:
                        heapq.heappush(hi, (-popped, popped_idx))
                        is_high[popped_idx] = True
                else:
                    break

            # drop out of window
            while hi and idx - hi[0][1] >= k:
                heapq.heappop(hi)
                extra_hi_count -= 1

            while low and idx - low[0][1] >= k:
                heapq.heappop(low)
                extra_low_count -= 1

            assert extra_hi_count >= 0
            assert extra_low_count >= 0

            medians.append(get_median())

        return medians


if __name__ == '__main__':
    x = Solution()
    print(x.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
    print(x.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], k=3))
    print(x.medianSlidingWindow([1, 2, 3, 4, 2, 3, 1, 4, 2], k=1))
    print(x.medianSlidingWindow([1], k=1))
    print(x.medianSlidingWindow([1, 2], k=1))
    print(x.medianSlidingWindow([2147483647,1,2,3,4,5,6,7,2147483647], k=2))
    print(x.medianSlidingWindow([1,1,1,1], k=2))
