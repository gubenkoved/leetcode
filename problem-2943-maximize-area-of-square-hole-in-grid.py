from typing import List

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        hBars.sort()
        vBars.sort()

        def max_conseq(arr: List[int]) -> int:
            max_r = 1
            r = 1
            for idx in range(1, len(arr)):
                if arr[idx] == arr[idx - 1] + 1:
                    r += 1
                    max_r = max(max_r, r)
                else:
                    r = 1
            return max_r

        d = min(
            max_conseq(hBars),
            max_conseq(vBars),
        )

        return (d + 1) ** 2


if __name__ == '__main__':
    x = Solution()
    # print(x.maximizeSquareHoleArea(3, 2, [3, 2, 4], [3, 2]), 9)
    print(x.maximizeSquareHoleArea(4, 40, [5,3,2,4], [36,41,6,34,33]), 9)
