from typing import List
import heapq


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        heap = []
        result = 0
        colors += '0'  # simpler handling for the finish
        neededTime.append(0)
        for idx in range(len(colors)):
            color = colors[idx]
            if idx > 0 and color != colors[idx - 1]:
                while len(heap) > 1:
                    result += heapq.heappop(heap)
                heap = []
            heapq.heappush(heap, neededTime[idx])
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
    print(x.minCost(colors="bbbaaa", neededTime=[4,9,3,8,8,9]), 23)
