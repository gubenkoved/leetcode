# A frog is crossing a river. The river is divided into some number of units,
# and at each unit, there may or may not exist a stone. The frog can jump
# on a stone, but it must not jump into the water.
#
# Given a list of stones' positions (in units) in sorted ascending order,
# determine if the frog can cross the river by landing on the last stone.
# Initially, the frog is on the first stone and assumes the first jump must
# be 1 unit.
#
# If the frog's last jump was k units, its next jump must be
# either k - 1, k, or k + 1 units. The frog can only jump in the forward
# direction.

from typing import List
from collections import deque


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        all_stones = set(stones)

        # deque of (stone, prev_stone)
        next_stones = deque([(0, 0)])
        checked = set()

        while next_stones:
            cur, prev = next_stones.popleft()

            if (cur, prev) in checked:
                continue

            checked.add((cur, prev))

            delta = cur - prev

            # end condition
            if cur == stones[-1]:
                return True

            if cur + delta in all_stones:
                next_stones.append((cur + delta, cur))
            if cur + delta - 1 in all_stones:
                next_stones.append((cur + delta - 1, cur))
            if cur + delta + 1 in all_stones:
                next_stones.append((cur + delta + 1, cur))

        return False


if __name__ == '__main__':
    x = Solution()
    assert x.canCross([0, 2]) is False
    assert x.canCross([0, 1, 3, 5, 6, 8, 12, 17]) is True
    assert x.canCross([0, 1, 2, 3, 4, 8, 9, 11]) is False
