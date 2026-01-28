from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('+inf')
        n = len(arr)

        for idx in range(1, n):
            min_diff = min(min_diff, abs(arr[idx] - arr[idx - 1]))

        result = []
        for idx in range(1, n):
            diff = abs(arr[idx] - arr[idx - 1])
            if diff == min_diff:
                result.append([arr[idx - 1], arr[idx]])

        return result
