from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def gen(idx, cur, allowed):

            if not allowed:
                results.append(cur)

            for element in allowed:
                new_allowed = set(allowed)
                new_allowed.discard(element)
                gen(idx + 1, cur + [element], new_allowed)

        # run the generator
        gen(0, [], set(nums))

        return results
