import time
from collections import deque


STARTED_AT = time.time()
PRINT_ORIG = print


def print(text):
    PRINT_ORIG('[%7.3f] %s' % (time.time() - STARTED_AT, text))


class Solution:
    def racecar(self, target: int) -> int:
        print('\nsolving for %d' % target)

        queue = deque()
        queue.append((0, 1, 0))

        visited = set()

        l, h = -10 ** 4, 10 ** 5  # positions cut-offs

        while queue:
            pos, speed, action_count = queue.popleft()

            visit_key = (pos, speed)
            if visit_key not in visited:
                visited.add(visit_key)
            else:
                continue

            if pos == target:
                print('actions: %d' % action_count)
                print('queue size: %d' % len(queue))
                return action_count

            # accelerate
            if pos + speed < h:
                queue.append((pos + speed, 2 * speed, action_count + 1))

            # reverse
            if pos > l:
                queue.append((pos, -1 if speed > 0 else 1, action_count + 1))

        assert False


if __name__ == '__main__':
    x = Solution()
    assert x.racecar(3) == 2
    assert x.racecar(6) == 5
    assert x.racecar(330) == 24
    assert x.racecar(10 ** 3) == 23
    assert x.racecar(1023) == 10
    assert x.racecar(1024) == 13
    assert x.racecar(1025) == 15
    assert x.racecar(1026) == 14
    assert x.racecar(10 ** 4) == 45
