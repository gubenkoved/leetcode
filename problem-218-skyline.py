from typing import List
import heapq


class Solution:
    # building is (left, right, height)
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []  # list of [left, height]
        events = []

        for idx, (left, right, height) in enumerate(buildings):
            heapq.heappush(events, (left, idx, 0))  # open events
            heapq.heappush(events, (right, idx, 1))  # close events

        active = set()
        prev_max = 0

        while events:
            process_at = events[0][0]

            # process all elements at this coordinate
            while events and events[0][0] == process_at:
                at, idx, is_close = heapq.heappop(events)
                if not is_close:
                    active.add(idx)
                else:
                    active.discard(idx)

            # process active set
            active_max = 0
            for idx in active:
                active_max = max(active_max, buildings[idx][2])

            if active_max != prev_max:
                skyline.append([process_at, active_max])
                prev_max = active_max

        return skyline


if __name__ == '__main__':
    x = Solution()
    print(x.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(x.getSkyline([[0,2,3],[2,5,3]]))
