from collections import deque


class Solution:
    def racecar(self, target: int) -> int:
        print('\nsolving for %d' % target)

        queue = deque()

        queue.append((0, 1, 0))

        while queue:
            pos, speed, action_count = queue.popleft()

            if pos == target:
                print('actions: %d' % action_count)
                print('queue size: %d' % len(queue))
                return action_count

            # accelerate
            queue.append((pos + speed, 2 * speed, action_count + 1))

            # reverse
            queue.append((pos, -1 if speed > 0 else 1, action_count + 1))

        assert False


if __name__ == '__main__':
    x = Solution()
    assert x.racecar(3) == 2
    assert x.racecar(6) == 5
    assert x.racecar(330) == 24
    assert x.racecar(10 ** 3) == 23
    assert x.racecar(10 ** 4) == 0
