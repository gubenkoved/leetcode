import collections
from typing import List
import heapq


class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:

        # edge -> adjacency list which is list of tuples (adjacent, cost)
        adjacency = collections.defaultdict(list)

        for start, end, cost in edges:
            adjacency[start].append((end, cost))

            # add reversed option
            adjacency[end].append((start, 2 * cost))

        heap = [(0, 0)]
        visited = set()
        cost_map = {}

        while heap:
            cur_cost, node = heapq.heappop(heap)

            if node in visited:
                continue

            visited.add(node)
            cost_map[node] = cur_cost

            # add neighbors
            for neigh, cost in adjacency.get(node, []):
                heapq.heappush(heap, (cur_cost + cost, neigh))

        return cost_map.get(n - 1, -1)

if __name__ == '__main__':
    x = Solution()
    print(x.minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]), 5)
    print(x.minCost(5, [[1,2,17],[1,0,6],[1,3,5],[2,4,12],[1,4,19],[4,3,11],[2,3,4],[0,2,20],[0,3,3],[3,0,25]]), 23)
