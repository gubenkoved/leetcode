import collections
from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # heap of (freed_at, idx)
        heap = []

        # heap of free indexes at given moment
        free_indexes_heap = []

        # add all rooms as free at the start
        for idx in range(n):
            heapq.heappush(free_indexes_heap, idx)

        # sort by start time increasing
        meetings.sort(key=lambda x: x[0])

        # idx -> amount used
        freq = collections.defaultdict(lambda: 0)

        for start, end in meetings:

            # see which rooms will be freed at that time
            while heap and heap[0][0] <= start:
                _, idx = heapq.heappop(heap)

                # mark room as free
                heapq.heappush(free_indexes_heap, idx)

            # if there is a free room -> pick one with the smallest ID
            # and for this case there is no delay
            if free_indexes_heap:
                idx = heapq.heappop(free_indexes_heap)
                heapq.heappush(heap, (end, idx))
            else:
                # no room available now, wait for the first free one
                t, idx = heapq.heappop(heap)
                assert t > start
                delay = t - start
                heapq.heappush(heap, (end + delay, idx))

            # find next free room
            freq[idx] += 1

        return max(freq.items(), key=lambda t: t[1])[0]


if __name__ == '__main__':
    x = Solution()
    print(x.mostBooked(n = 2, meetings = [[0,10],[1,5],[2,7],[3,4]]), 0)
    print(x.mostBooked(n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]), 1)
    print(x.mostBooked(n = 4, meetings=[[18,19],[3,12],[17,19],[2,13],[7,10]]), 0)
