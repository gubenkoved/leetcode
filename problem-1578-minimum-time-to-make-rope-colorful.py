from typing import List
import heapq


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        heap = []
        group_sum = 0
        result = 0
        colors += '0'  # simpler handling for the finish
        neededTime.append(0)
        for idx in range(len(colors)):
            color = colors[idx]
            if idx > 0 and color != colors[idx - 1]:
                if len(heap) > 1:
                    result += group_sum + heapq.heappop(heap)
                heap = []
                group_sum = 0
            heapq.heappush(heap, -neededTime[idx])
            group_sum += neededTime[idx]
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
    print(x.minCost(colors="bbbaaa", neededTime=[4,9,3,8,8,9]), 23)
