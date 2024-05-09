from collections import defaultdict, deque
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacency = defaultdict(set)

        for a, b in edges:
            adjacency[a].add(b)
            adjacency[b].add(a)

        def sum_distances(start):
            distance = {start: 0}

            queue = deque()
            queue.append(start)

            while queue:
                node = queue.popleft()

                for adjacent in adjacency[node]:
                    if adjacent not in distance:
                        queue.append(adjacent)
                        distance[adjacent] = distance[node] + 1

            return sum(distance.values())

        return [sum_distances(idx) for idx in range(n)]


if __name__ == '__main__':
    x = Solution()
    print(x.sumOfDistancesInTree(6, [[0,1],[0,2],[2,3],[2,4],[2,5]]))
