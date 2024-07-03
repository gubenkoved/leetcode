from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        # count amount of zeros surrounded by 1 and -1
        # -1 0 ... 0 1
        # or
        # 1 0 ... 0 -1
        start_idx = 0
        result = 0
        for idx in range(1, len(forts)):
            if forts[idx] != 0:
                if forts[idx] * forts[start_idx] == -1:
                    result = max(result, idx - start_idx - 1)
                start_idx = idx
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]))
    print(x.captureForts([0, 0, 1, -1]))
    print(x.captureForts([-1, -1, -1, -1, 1, -1, 0, 1, 1, -1, 1, -1]))
    print(x.captureForts([1, -1, -1, 1, 1]))
    print(x.captureForts([-1, -1, 1, -1, 0, 1, 0, 0]))
