import collections
from typing import List
import heapq

class Solution:
    # FIXME: this is not correct as we pick room which is freed first
    #  when there are multiple rooms available
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        heap = []

        # add all as free at start
        for idx in range(n):
            heapq.heappush(heap, (0, idx))

        # sort by start time increasing
        meetings.sort(key=lambda x: x[0])

        # idx -> amount used
        freq = collections.defaultdict(lambda: 0)

        for start, end in meetings:
            # find next free room
            t, idx = heapq.heappop(heap)
            freq[idx] += 1

            if t > start:
                # delay
                delay = t - start
                heapq.heappush(heap, (end + delay, idx))
            else:
                # no delay
                heapq.heappush(heap, (end, idx))

        return max(freq.items(), key=lambda t: t[1])[0]


if __name__ == '__main__':
    x = Solution()
    print(x.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]), 0)
    print(x.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]), 1)
