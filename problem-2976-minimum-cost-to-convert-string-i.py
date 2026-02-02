import collections
import functools
from typing import List
import heapq


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        # char -> list of (char, cost)
        adjacency = collections.defaultdict(list)

        for a, b, tc in zip(original, changed, cost):
            adjacency[a].append((b, tc))

        # (from, to) -> best cost
        best_costs = {}

        @functools.lru_cache(None)
        def cost(a, b) -> int:
            if (a, b) in best_costs:
                return best_costs[a, b]

            visited = set()
            heap = [(0, a)]

            while heap:
                cur_cost, node = heapq.heappop(heap)

                if node in visited:
                    continue
                visited.add(node)

                best_costs[(a, node)] = cur_cost

                if node == b:
                    return cur_cost

                for neigh, neigh_cost in adjacency[node]:
                    heapq.heappush(heap, (neigh_cost + cur_cost, neigh))

            return -1


        result = 0
        for a, b in zip(source, target):
            if a == b:
                continue
            cur_cost = cost(a, b)
            if cur_cost == -1:
                return -1
            # print('%s -> %s costs %d' % (a, b, cur_cost))
            result += cur_cost

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]))
