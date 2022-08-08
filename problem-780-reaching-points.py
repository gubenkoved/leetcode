from collections import deque


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        target = (tx, ty)
        cur = (sx, sy)
        queue = deque([cur])

        while queue:
            cur = queue.popleft()

            if cur == target:
                return True

            next_items = [
                (cur[0], cur[0] + cur[1]),
                (cur[0] + cur[1], cur[1])
            ]

            for item in next_items:
                if item[0] <= tx and item[1] <= ty:
                    queue.append(item)

        return False


if __name__ == '__main__':
    x = Solution()
    print(x.reachingPoints(1, 1, 3, 5))
    print(x.reachingPoints(1, 1, 2, 2))
    print(x.reachingPoints(1, 1, 1, 1))
    # print(x.reachingPoints(35, 13, 455955547, 420098884))
