from typing import List


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        n = len(arr)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if abs(arr[j] - arr[i]) > a:
                        continue
                    if abs(arr[k] - arr[j]) > b:
                        continue
                    if abs(arr[k] - arr[i]) > c:
                        continue
                    result += 1
        return result
