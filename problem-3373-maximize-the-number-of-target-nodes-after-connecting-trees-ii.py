import collections
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def distances_from(edges, node):
            adjacent = {}
            for source, target in edges:
                if source not in adjacent:
                    adjacent[source] = []
                if target not in adjacent:
                    adjacent[target] = []
                adjacent[source].append(target)
                adjacent[target].append(source)

            dist_map = {}
            even_count, odd_count = 0, 0
            queue = collections.deque([(node, 0, None)])
            while queue:
                cur, cur_dist, parent = queue.popleft()
                dist_map[cur] = cur_dist

                if cur_dist % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1

                for neighbor in adjacent[cur]:
                    if neighbor == parent:
                        continue
                    queue.append((neighbor, cur_dist + 1, cur))
            return dist_map, even_count, odd_count

        d1, d1_even, d1_odd = distances_from(edges1, 0)
        d2, d2_even, d2_odd = distances_from(edges2, 0)

        d2_best = max(d2_even, d2_odd)

        n = len(edges1) + 1

        return [
            (d1_even + d2_best) if d1[x] % 2 == 0 else (d1_odd + d2_best)
            for x in range(n)
        ]


if __name__ == '__main__':
    x = Solution()
    print(x.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))
