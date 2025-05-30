from typing import List
import heapq


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        adjacent = {}

        for source, target in enumerate(edges):
            if target == -1:
                continue
            if source not in adjacent:
                adjacent[source] = []
            adjacent[source].append(target)

        n = len(edges)

        def distances_from(node):
            dist_map = {}
            visited = set()
            queue = [
                (0, node)
            ]

            while queue:
                dist, cur = heapq.heappop(queue)

                if cur in visited:
                    continue

                visited.add(cur)
                dist_map[cur] = dist

                for neighbor in adjacent.get(cur, []):
                    if neighbor in visited:
                        continue
                    heapq.heappush(queue, (1 + dist, neighbor))

            return dist_map

        d1 = distances_from(node1)
        d2 = distances_from(node2)

        best, best_node = float('inf'), None
        for x in range(n):
            d = max(d1.get(x, float('inf')), d2.get(x, float('inf')))
            if d < best:
                best = d
                best_node = x

        if best_node is None:
            return -1

        return best_node


if __name__ == '__main__':
    s = Solution()
    print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
