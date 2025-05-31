import collections
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def distances_from(edges, node) -> dict[int, int]:
            adjacent = {}
            for source, target in edges:
                if source not in adjacent:
                    adjacent[source] = []
                if target not in adjacent:
                    adjacent[target] = []
                adjacent[source].append(target)
                adjacent[target].append(source)

            dist_map = {}
            queue = collections.deque([(node, 0, None)])
            while queue:
                cur, cur_dist, parent = queue.popleft()
                dist_map[cur] = cur_dist

                for neighbor in adjacent[cur]:
                    if neighbor == parent:
                        continue
                    queue.append((neighbor, cur_dist + 1, cur))
            return dist_map

        def summarize(dist_map: dict[int, int]) -> tuple[int, int]:
            even_count = len(list(x for x in dist_map.values() if x % 2 == 0))
            return even_count, len(dist_map) - even_count

        d1 = distances_from(edges1, 0)
        d2 = distances_from(edges2, 0)

        d1_even, d1_odd = summarize(d1)
        d2_even, d2_odd = summarize(d2)

        n, m = len(edges1) + 1, len(edges2) + 1

        result = []
        for x in range(n):
            if d1[x] % 2 == 0:
                result.append(d1_even + max(d2_even, d2_odd))
            else:
                result.append(d1_odd + max(d2_even, d2_odd))

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]))
