from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        # returns a map from the node id to amount of nodes in the radius of k
        def process_tree(edges, radius) -> dict[int, int]:

            # compute adjacency lists for faster traversals
            adjacent = {}

            for n1, n2 in edges:
                if n1 not in adjacent:
                    adjacent[n1] = []
                if n2 not in adjacent:
                    adjacent[n2] = []

                adjacent[n1].append(n2)
                adjacent[n2].append(n1)

            def compute(node, node_radius, visited):
                assert node not in visited
                visited.add(node)

                if node_radius < 0:
                    return 0

                node_result = 1  # itself

                # stop condition
                if node_radius == 0:
                    return node_result

                for neighbor in adjacent[node]:
                    if neighbor in visited:
                        continue
                    node_result += compute(neighbor, node_radius - 1, visited)

                return node_result

            result_map = {}

            for n in adjacent:
                result_map[n] = compute(n, radius, set())

            return result_map

        tree1_map = process_tree(edges1, k)
        tree2_map = process_tree(edges2, k - 1)

        # from second tree we just need a single node which gives the most neighbors
        # in the radius of (k - 1)

        tree2_best_result = max(tree2_map.values())

        n = max(tree1_map)
        result = []

        for x in range(n + 1):
            result.append(
                tree1_map[x] + tree2_best_result
            )

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.maxTargetNodes(edges1=[[0, 1], [0, 2], [2, 3], [2, 4]],
    #                        edges2=[[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]], k=2))
    print(x.maxTargetNodes(edges1=[[0, 1]], edges2=[[0, 1]], k=0))
