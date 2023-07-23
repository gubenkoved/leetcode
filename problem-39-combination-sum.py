from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        found = set()
        current = []

        def search(needed):
            if needed < 0:
                return

            if needed == 0:
                found.add(tuple(sorted(current)))
                return

            for x in candidates:
                current.append(x)
                if x <= needed:
                    search(needed - x)
                current.pop(-1)

        search(target)
        return [list(x) for x in found]


if __name__ == '__main__':
    x = Solution()
    print(x.combinationSum(candidates=[2, 3, 6, 7], target=7))
