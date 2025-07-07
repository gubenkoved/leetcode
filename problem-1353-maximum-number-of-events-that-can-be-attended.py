from typing import List
import heapq

# simple greedy solution -- every day attend the event with the earliest end day
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        assert events
        # sort events by the start day
        events.sort(key=lambda x: x[0])
        n = len(events)
        count = 0
        day = events[0][0]
        open_idx = 0
        # min heap of available events (END, START)
        open = []
        while open_idx < n or open:
            # add available events (if any)
            while open_idx < n and events[open_idx][0] <= day:
                heapq.heappush(open, (events[open_idx][1], events[open_idx][0]))
                open_idx += 1

            # pick the one with earlies end date
            while open:
                end_day, start_day = heapq.heappop(open)
                if end_day < day:
                    continue
                count += 1
                break

            day += 1

        return count


if __name__ == '__main__':
    x = Solution()
    print(5, x.maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))
    print(2, x.maxEvents([[52,79],[7,34]]))
