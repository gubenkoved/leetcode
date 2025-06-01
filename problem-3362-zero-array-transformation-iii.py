import heapq
from typing import List


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        # sort queries by its starting point
        queries.sort(key=lambda x: x[0])

        # index tracking position inside the queries to quickly determine
        # started queries
        query_by_start_idx = 0

        # aux array of tuples (end, query_idx)
        queries_end_sorted = sorted((end, idx) for idx, (_, end) in enumerate(queries))
        query_by_end_idx = 0

        # heap tracking indexes of currently "available" queries
        # heap is min heap and we want have queries which have the farthest
        # end point processed first, so we go with (-end, idx)
        available = []

        used = set()
        usage_counter = 0

        for cell_idx in range(n):
            # update the heap with "available" queries
            while query_by_start_idx < len(queries) and queries[query_by_start_idx][0] == cell_idx:
                heapq.heappush(available, (-queries[query_by_start_idx][1], query_by_start_idx))
                query_by_start_idx += 1

            while nums[cell_idx] > len(used):
                if not available:
                    return -1
                # greedily pick a new "query"
                _, picked_query_idx = heapq.heappop(available)

                if queries[picked_query_idx][1] < cell_idx:
                    # out of range already, skip
                    continue

                used.add(picked_query_idx)
                usage_counter += 1

            # evict queries which go out of range
            while query_by_end_idx < len(queries) and queries_end_sorted[query_by_end_idx][0] == cell_idx:
                query_idx = queries_end_sorted[query_by_end_idx][1]
                used.discard(query_idx)
                query_by_end_idx += 1

        return len(queries) - usage_counter


if __name__ == '__main__':
    x = Solution()
    print(x.maxRemoval(nums=[2, 0, 2], queries=[[0, 2], [0, 2], [1, 1]]))
    print(x.maxRemoval(nums=[1, 1, 1, 1], queries=[[1, 3], [0, 2], [1, 3], [1, 2]]))
    print(x.maxRemoval(nums=[1, 2, 3, 4], queries=[[0, 3]]))
    print(x.maxRemoval([0, 0, 3], [[0, 2], [1, 1], [0, 0], [0, 0]]))
