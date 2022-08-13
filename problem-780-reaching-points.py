from collections import deque


class Solution:
    def reachingPoints_v0(self, sx: int, sy: int, tx: int, ty: int) -> bool:
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

    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        cx, cy = tx, ty

        while cx > 0 and cy > 0:
            if (cx, cy) == (sx, sy):
                return True

            if cx > cy:
                n = (cx - cy) // cy
                n = min(n, (cx - sx) // cy)
                n = max(n, 1)
                cx, cy = cx - n * cy, cy
            elif cx < cy:
                n = (cy - cx) // cx
                n = min(n, (cy - sy) // cx)
                n = max(n, 1)
                cx, cy = cx, cy - n * cx
            else:
                return False  # zero increment is not possible

        return False


if __name__ == '__main__':
    x = Solution()
    print(x.reachingPoints(1, 1, 3, 5))
    print(x.reachingPoints(1, 1, 2, 2))
    print(x.reachingPoints(1, 1, 1, 1))
    print(x.reachingPoints(35, 13, 455955547, 420098884))
    print(x.reachingPoints(1, 1, 10 ** 9, 1))
    print(x.reachingPoints(10, 5, 15, 5))
