from collections import defaultdict, deque
from typing import List, Tuple
from functools import lru_cache


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency = defaultdict(set)

        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)

        # handle special case: node only has single adjacent node and
        # we record the answer associating it with that adjacent node because
        # for topologies with node at center it optimizes a lot
        cutoff = {}

        # returns amount of nodes and sum of distances for subtree that starts
        # at "target" but never gets back to "prev" node -- this allows to
        # decompose the task into reusable components to avoid repeat calculations
        @lru_cache(maxsize=None)
        def sum_distances(prev, target) -> Tuple[int, int]:
            # start with count equal to 1 to account for the "target" node itself
            count, dist = 1, 0

            single_path_case = len(adjacency[prev]) == 1

            if single_path_case:
                adj_node = next(iter(adjacency[prev]))
                if adj_node in cutoff:
                    return cutoff[adj_node]

            for adjacent in adjacency[target]:

                if adjacent == prev:
                    continue

                sub_count, sub_dist = sum_distances(prev=target, target=adjacent)

                # add found nodes to current node's count
                count += sub_count

                # all these nodes are 1 node farther comparing to "adjacent", so
                # we add 1 x count of these nodes to the distance here
                dist += sub_dist + sub_count

            if single_path_case:
                cutoff[adj_node] = count, dist

            return count, dist

        return [sum_distances(-1, idx)[1] for idx in range(n)]


if __name__ == '__main__':
    x = Solution()
    print(x.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))