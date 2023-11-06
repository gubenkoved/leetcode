import collections
from typing import List
from collections import deque


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # this can be thought as graph problem where we search path from one node to another
        # computing overall ration as we go because each edge in the graph has
        # a specific "conversion" rate;
        # when no path can be found then we can not answer the "query" and return "-1"

        # stage 1. Construct directed graph

        # variable -> list of (neighbor, rate)
        neighbors = collections.defaultdict(dict)

        n = len(equations)
        for idx in range(n):
            # a / b = ratio
            a, b = equations[idx]
            ratio = values[idx]

            neighbors[a][b] = ratio
            neighbors[b][a] = 1 / ratio

        # stage 2. Answer queries

        def search(a, b):
            visited = set()
            queue = deque()
            parent = {}
            queue.append(a)

            while queue:
                node = queue.popleft()

                if node in visited:
                    continue

                visited.add(node)

                for neighbor in neighbors.get(node, {}).keys():
                    if neighbor not in visited:
                        parent[neighbor] = node
                        queue.append(neighbor)

            # trace back to get final ratio
            if b not in parent and a != b:
                return -1

            # wierd part of the problem statement: x / x = -1 if we do not know
            # anything about x...
            if a == b and a not in neighbors:
                return -1

            ratio = 1

            cur = b
            while cur != a:
                prev = parent[cur]
                ratio *= neighbors[prev][cur]
                cur = prev

            return ratio

        result = []
        for a, b in queries:
            result.append(search(a, b))

        return result


if __name__ == '__main__':
    x = Solution()

    # assert x.calcEquation(
    #     equations=[["a", "b"], ["b", "c"]],
    #     values=[2.0, 3.0],
    #     queries=[["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [
    #         6.00000, 0.50000, -1.00000, 1.00000,-1.00000]

    assert x.calcEquation(
        equations=[["x1", "x2"]],
        values=[3.0],
        queries=[["x9", "x2"], ["x9", "x9"]]) == [-1, -1]
