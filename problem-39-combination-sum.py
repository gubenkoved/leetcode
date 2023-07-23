from typing import List
from functools import lru_cache


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache()
        def search(needed):
            found = set()
            for x in candidates:
                if x < needed:
                    for inner in search(needed - x):
                        found.add(tuple(sorted((x,) + inner)))
                elif x == needed:
                    found.add((x,))
            return found

        return [list(x) for x in search(target)]


if __name__ == '__main__':
    x = Solution()
    print(x.combinationSum(candidates=[2, 3, 6, 7], target=7))
