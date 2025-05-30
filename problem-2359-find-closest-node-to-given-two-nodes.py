from typing import List
from collections import deque


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def distances_from(node):
            dist_map = {}
            queue = deque([(0, node)])

            while queue:
                dist, cur = queue.popleft()
                if cur in dist_map:
                    continue
                dist_map[cur] = dist
                if edges[cur] != -1:
                    queue.append((dist + 1, edges[cur]))

            return dist_map

        d1 = distances_from(node1)
        d2 = distances_from(node2)

        best, best_node = float('inf'), None
        for x in range(n):
            if x not in d1 or x not in d2:
                continue
            d = max(d1[x], d2[x])
            if d < best:
                best = d
                best_node = x

        if best_node is None:
            return -1

        return best_node


if __name__ == '__main__':
    s = Solution()
    print(s.closestMeetingNode(edges = [2,2,3,-1], node1 = 0, node2 = 1))
    print(s.closestMeetingNode([5,4,5,4,3,6,-1], 0, 1))
