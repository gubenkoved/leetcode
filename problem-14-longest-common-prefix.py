from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        result_idx = 0
        while True:
            if result_idx >= len(strs[0]):
                break
            c = strs[0][result_idx]
            ok = True
            for str_idx in range(1, n):
                if len(strs[str_idx]) <= result_idx or strs[str_idx][result_idx] != c:
                    ok = False
                    break
            if not ok:
                break
            result_idx += 1
        return strs[0][:result_idx]


if __name__ == '__main__':
    x = Solution()
    print(x.longestCommonPrefix(["flower","flow","flight"]))