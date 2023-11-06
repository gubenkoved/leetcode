from typing import List
from collections import deque
from functools import lru_cache


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        @lru_cache(maxsize=None)
        def mutation_count(a, b):
            result = 0
            for idx in range(len(a)):
                if a[idx] != b[idx]:
                    result += 1
            return result


        queue = deque()
        queue.append(startGene)
        visited = set()
        distance = {}
        distance[startGene] = 0

        # BFS...
        while queue:
            gene = queue.popleft()

            if gene in visited:
                continue

            visited.add(gene)

            for gene2 in bank:
                if gene2 in visited:
                    continue

                # overall distance is unknown yet
                if gene2 not in distance:
                    if mutation_count(gene, gene2) == 1:
                        queue.append(gene2)
                        distance[gene2] = distance[gene] + 1

                        if gene2 == endGene:
                            return distance[endGene]

        return -1
