from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        k = len(strs[0])

        cache = {}

        # possible states count -- n * k
        def f(last_kept_col_idx: int, idx: int) -> int:
            if idx == k:
                return 0

            key = (last_kept_col_idx, idx)
            if key in cache:
                return cache[key]

            # alt1: keep this column if no contradiction i.e.
            #  all chars are bigger than the last one
            # alt2: drop column - costs 1 col deletion

            can_keep = last_kept_col_idx == -1 or all(
                s[idx] >= s[last_kept_col_idx]
                for s in strs)

            # drop column!
            result = f(last_kept_col_idx, idx + 1) + 1

            if can_keep:
                result = min(result, f(idx, idx+1))

            cache[key] = result

            return result

        return f(-1, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.minDeletionSize(["babca","bbazb"]), 3)
