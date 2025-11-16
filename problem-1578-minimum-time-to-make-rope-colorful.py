from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        group_sum = 0
        group_max_time = 0
        group_count = 0
        result = 0

        for idx in range(len(colors)):
            color = colors[idx]
            if idx > 0 and color != colors[idx - 1]:
                if group_count > 1:
                    result += group_sum - group_max_time
                group_count = 0
                group_sum = 0
                group_max_time = 0
            group_max_time = max(group_max_time, neededTime[idx])
            group_sum += neededTime[idx]
            group_count += 1

        # handle final
        if group_count > 1:
            result += group_sum - group_max_time

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minCost(colors = "abaac", neededTime = [1,2,3,4,5]), 3)
    print(x.minCost(colors="bbbaaa", neededTime=[4,9,3,8,8,9]), 23)
