from typing import List
from functools import lru_cache

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        k = len(strs[0])

        # possible states count -- n * k
        @lru_cache(None)
        def f(last_letters_vector: str, idx: int) -> int:
            if idx == k:
                return 0

            # alternative 1: keep this column if no contradiction i.e.
            #  all chars are bigger than the last one
            # alt 2: drop column - costs 1 col deletion

            can_keep = all(
                s[idx] >= last_letters_vector[s_idx]
                for s_idx, s in enumerate(strs))

            # drop column!
            result = f(last_letters_vector, idx + 1) + 1

            if can_keep:
                new_vector = ''.join(s[idx] for s in strs)
                result = min(result, f(new_vector, idx+1))

            return result

        return f('a' * n, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.minDeletionSize(["babca","bbazb"]), 3)
