import collections
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        # convert to adjacency map
        adjacent = collections.defaultdict(list)

        for a, b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)

        # convert guesses into hashset
        guesses_set = {tuple(x) for x in guesses}

        count = 0

        # suppose root is at 0, calculate correct guesses as a baseline
        queue = collections.deque()
        queue.append((0, 0))
        visited = set()
        correct = 0

        while queue:
            idx, dist = queue.popleft()

            if idx in visited:
                continue

            visited.add(idx)

            for adj_idx in adjacent[idx]:
                if adj_idx not in visited:
                    if (idx, adj_idx) in guesses_set:
                        correct += 1
                    queue.append((adj_idx, dist + 1))

        # now try all other cases but incrementally in DFS order, so that next
        # combination can actually be calculated using the previous one
        visited = set()

        def dfs(idx, correct):
            nonlocal count

            if idx in visited:
                return

            visited.add(idx)

            if correct >= k:
                count += 1

            for adj in adjacent[idx]:
                delta = 0
                if (idx, adj) in guesses_set:
                    delta -= 1
                if (adj, idx) in guesses_set:
                    delta += 1
                dfs(adj, correct + delta)

        dfs(0, correct)

        return count


if __name__ == '__main__':
    x = Solution()
    print(x.rootCount(edges=[[0, 1], [1, 2], [1, 3], [4, 2]], guesses=[[1, 3], [0, 1], [1, 0], [2, 4]], k=3))  # 3
    print(x.rootCount(edges=[[0, 1], [1, 2], [2, 3], [3, 4]], guesses=[[1, 0], [3, 4], [2, 1], [3, 2]], k=1))  # 5

    with open('input.txt') as f:
        edges = eval(f.readline())
        guesses = eval(f.readline())
        k = eval(f.readline())
        print(x.rootCount(edges, guesses, k))  # 9070
