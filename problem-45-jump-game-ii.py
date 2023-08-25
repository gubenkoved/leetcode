from typing import List

from collections import deque


class Solution:
    def jump(self, nums: List[int]) -> int:
        queue = deque()
        queue.append((0, 0))
        visited = set()
        n = len(nums)

        while queue:
            x, d = queue.popleft()

            if x in visited:
                continue

            visited.add(x)

            if x == n - 1:
                return d

            for reachable in range(x + 1, min(x + nums[x] + 1, n)):
                queue.append((reachable, d + 1))

        return -1

    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        rolling_farthest = 0
        cur_jump_farthest = 0

        for idx in range(n):
            rolling_farthest = max(rolling_farthest, idx + nums[idx])

            if idx == cur_jump_farthest and idx != n - 1:
                print('with %d jumps could reach up to %d' % (jumps, cur_jump_farthest))
                jumps += 1
                cur_jump_farthest = rolling_farthest

        return jumps


if __name__ == '__main__':
    x = Solution()
    print(x.jump([2, 3, 1, 1, 4]))
    print(x.jump([0]))
