import math
from typing import List
import heapq


class Solution:
    # building is (left, right, height)
    def getSkyline_v1(self, buildings: List[List[int]]) -> List[List[int]]:
        skyline = []  # list of [left, height]
        events = []

        for idx, (left, right, height) in enumerate(buildings):
            events.append((left, idx, 0))  # open events
            events.append((right, idx, 1))  # close events

        heapq.heapify(events)

        n = len(buildings)
        l = max(1, math.ceil(math.log2(n)))
        tree_size = 2 ** (l + 1)
        tree = [0] * tree_size
        leaf_offset = 2 ** l - 1

        def tree_parent(idx):
            return (idx - 1) // 2

        def tree_children(idx):
            return 2 * idx + 1, 2 * idx + 2

        # pushes the update via the tree re-calculating up to the top
        def update_tree(idx):
            left_idx, right_idx = tree_children(idx)
            new_val = max(tree[left_idx], tree[right_idx])
            if tree[idx] == new_val:
                return
            tree[idx] = new_val
            if idx != 0:
                update_tree(tree_parent(idx))

        prev_max = 0

        while events:
            process_at = events[0][0]

            # process all elements at this coordinate
            while events and events[0][0] == process_at:
                at, idx, is_close = heapq.heappop(events)
                h = buildings[idx][2] if not is_close else 0
                tree[leaf_offset + idx] = h
                update_tree(tree_parent(leaf_offset + idx))

            # process active set
            active_max = tree[0]

            if active_max != prev_max:
                skyline.append([process_at, active_max])
                prev_max = active_max

        return skyline

    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for idx, (left, right, height) in enumerate(buildings):
            events.append((left, idx, 0))  # open events
            events.append((right, idx, 1))  # close events

        events.sort()

        skyline = []
        heap = []
        prev = 0

        events_cursor = 0
        while events_cursor < len(events):
            process_at = events[events_cursor][0]

            while events_cursor < len(events) and events[events_cursor][0] == process_at:
                at, idx, is_close = events[events_cursor]
                _, right, h = buildings[idx]
                if not is_close:
                    heapq.heappush(heap, (-h, right))
                events_cursor += 1

            while heap and heap[0][1] <= process_at:
                heapq.heappop(heap)

            cur_val = -heap[0][0] if heap else 0
            if prev != cur_val:
                skyline.append([process_at, cur_val])
                prev = cur_val

        return skyline


if __name__ == '__main__':
    x = Solution()
    print(x.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
    print(x.getSkyline([[0,2,3],[2,5,3]]))
    print(x.getSkyline([[0, 1, 3]]))

    # [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
    # [[0, 3], [5, 0]]
    # [[0, 3], [1, 0]]

