import collections
import time
from typing import List


class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        print('%d/%d/%d' % (len(edges), len(guesses), k))
        start_at = time.time()

        # convert to adjacency map
        adjacent = collections.defaultdict(list)

        for a, b in edges:
            adjacent[a].append(b)
            adjacent[b].append(a)

        count = 0
        n = len(edges) + 1
        for root_idx in range(n):
            # suppose root is root idx, check if all the guess are correct
            root_distance = {}

            queue = collections.deque()
            queue.append((root_idx, 0))

            while queue:
                idx, dist = queue.popleft()
                root_distance[idx] = dist
                for adj_idx in adjacent[idx]:
                    if adj_idx not in root_distance:
                        queue.append((adj_idx, dist + 1))

            correct = 0
            for parent, child in guesses:
                if root_distance[parent] == root_distance[child] - 1:
                    correct += 1

                if correct >= k:
                    break

            if correct >= k:
                count += 1

        print('%.5f sec' % (time.time() - start_at))
        return count


if __name__ == '__main__':
    x = Solution()
    print(x.rootCount(edges=[[0, 1], [1, 2], [1, 3], [4, 2]], guesses=[[1, 3], [0, 1], [1, 0], [2, 4]], k=3))
    print(x.rootCount(edges=[[0, 1], [1, 2], [2, 3], [3, 4]], guesses=[[1, 0], [3, 4], [2, 1], [3, 2]], k=1))

    # with open('input.txt') as f:
    #     edges = eval(f.readline())
    #     guesses = eval(f.readline())
    #     k = eval(f.readline())
    #     x.rootCount(edges, guesses, k)
