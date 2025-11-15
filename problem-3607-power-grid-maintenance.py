from typing import List
import heapq


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # basically we need to process connections and maintain disjoint set
        # of power grids;
        # the root of the set (smallest ID of the station) can be associated
        # with total stations online to resolve the queries quickly

        parent = [0]
        for x in range(1, c + 1):
            # start with parent pointing to itself (that is the root of the
            # grid)
            parent.append(x)

        def root_of(x):
            cur = x
            while parent[cur] != cur:
                cur = parent[cur]
            # reparent to speedup the next time calculation
            parent[x] = cur
            return cur

        # process connections
        for a, b in connections:
            a_root, b_root = root_of(a), root_of(b)

            # already in the same grid
            if a_root == b_root:
                continue

            # merge the grids (union), maintain smallest number as a root
            if a_root <= b_root:
                parent[b_root] = a_root
            else:
                parent[a_root] = b_root

        # map from the root of the grid to a minheap of indexes it composed of
        # when we will taking the stations offline we will temporarily have
        # offline stations there as well
        operational = {}

        for x in range(1, c + 1):
            grid_id = root_of(x)
            if grid_id not in operational:
                operational[grid_id] = []
            heapq.heappush(operational[grid_id], x)

        # track stations offline
        offline = set()

        result = []
        for type, x in queries:
            grid_id = root_of(x)

            if type == 1:
                # probing
                if x not in offline:
                    # if station is not offline -> resolve via itself
                    result.append(x)
                else:
                    # see if there is an operational station left
                    heap = operational[grid_id]

                    # drop ones which are offline
                    while heap and heap[0] in offline:
                        heapq.heappop(heap)

                    if heap:
                        result.append(heap[0])
                    else:
                        result.append(-1)
            elif type == 2:
                # goes offline
                if x in offline:
                    continue
                offline.add(x)

        return result
