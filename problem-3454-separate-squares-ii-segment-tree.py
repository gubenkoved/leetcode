from typing import List
import decimal

decimal.getcontext().prec = 20

INF = float('+inf')

class SegmentTree:
    def __init__(self, x):
        # idx of point -> its real coordinate (sorted)
        self.x = x
        self.xn = len(x)

        # determine the first power of 2 that holds all the leaf nodes
        n = 1
        while n < len(x):
            n *= 2

        # this is basically the size of the "leaf" layer, the ST is twice as big
        self.n = n

        # segment tree is twice as big with root at index 1
        # for each "node" we will store amount of segments it is covered with
        # inside "counter" and total covered area inside "coverage"
        self.counter = [0] * (2 * n)
        self.coverage = [0] * (2 * n)

    # updates the segment tree by adding/removing segment [x_left, x_right)
    # there real coordinates are used AND it is guaranteed that these are
    # the part of the "x" array
    def update(self, x_left, x_right, is_added):

        # updates ST node at index that covers [l, r) leaf nodes
        def updater(idx, l, r, seg_left_x, seg_right_x):
            m = (l + r) // 2

            # left child covers leaf indexes [l, m)
            # right child covers leaf indexes [m, r)

            # no intersection with the target interval? exit!
            if seg_left_x >= x_right or seg_right_x <= x_left:
                return

            # is current segment fully covered?
            if seg_left_x >= x_left and seg_right_x <= x_right:
                self.counter[idx] += +1 if is_added else -1
            else:
                # coverage is not full, need to go to child nodes
                seg_mid_x = INF if m >= self.xn else self.x[m]

                updater(2 * idx, l, m, seg_left_x, seg_mid_x)

                if seg_mid_x != INF:
                    updater(2 * idx + 1, m, r, seg_mid_x, seg_right_x)

            # post-order update the covered width for affected nodes in the ST

            if self.counter[idx] > 0:
                # if segment is fully covered -- use its full width
                self.coverage[idx] = seg_right_x - seg_left_x
            else:  # no full coverage
                # update the coverage using the children coverage
                if idx < self.n:
                    self.coverage[idx] = self.coverage[2 * idx] + self.coverage[2 * idx + 1]
                else:
                    # no children and no full coverage -> 0
                    self.coverage[idx] = 0

        # update the tree starting at root
        updater(1, 0, self.n, self.x[0], INF)


    def total_covered(self):
        return self.coverage[1]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:

        # stage 1 -- go scanning line (parallel to X) from the bottom
        # to the highest and compute equivalent rectangles which will
        # not intersect;
        # each rectangle is identified by (y, w, h) which is rect with width "w"
        # from "y" to "y + h";
        # notice that it does NOT matter for us how exactly it is positioned
        # by the X axis for the purpose of this task;

        rectangles = []

        # phase 1 -- try to infer the shape of the merge result over all the squares
        events = []
        unique_x = set()
        for x, y, s in squares:
            # when our scanning line progresses from bottom to top we will need
            # to process 2 events: first new "range" [x, x + s] is added, then
            # after we go via it, it will be removed
            events.append((y, x, x + s, 'add'))
            events.append((y + s, x, x + s, 'del'))
            unique_x.add(x)
            unique_x.add(x + s)

        # sort events by y coordinate
        events.sort(key=lambda t: t[0])

        # "ranges" in scope -- the covered distance of them drives the "width" of
        # the equivalent rectangle
        prev_width = 0
        prev_y = 0

        x = list(sorted(unique_x))
        st = SegmentTree(x)

        for idx in range(len(events)):
            y, x1, x2, event_type = events[idx]

            if event_type == 'add':
                st.update(x1, x2, is_added=True)
            elif event_type == 'del':
                st.update(x1, x2, is_added=False)

            # add a new rectangle (skip empty ones)
            # simple optimization: if there are multiple events for the same Y
            # only process the updated width once to save CPU
            if idx + 1 == len(events) or events[idx + 1][0] != y:
                if prev_width * (y - prev_y):
                    rectangles.append((prev_y, prev_width, y - prev_y))
                prev_width = st.total_covered()
                prev_y = y

        # sort the events by y (sweeping line moving up)
        events.sort(key=lambda t: t[0])

        # phase 2 -- simple binary search on the non-intersecting rectangles
        min_y = rectangles[0][0]
        max_y = rectangles[0][0] + rectangles[0][2]
        total_area = 0
        for y, w, h in rectangles:
            min_y = min(min_y, y)
            max_y = max(max_y, y + h)
            total_area += w * h

        half_total_area = decimal.Decimal(total_area) / 2

        eps = 10 ** -5
        l, r = min_y, max_y
        while r - l > eps:
            mid = (l + r) / 2

            # calculate area below mid
            area_below_mid = decimal.Decimal(0)
            for y, w, h in rectangles:
                if mid <= y:
                    continue
                if mid >= y + h:
                    area_below_mid += w * h
                    continue
                ratio = decimal.Decimal(mid - y) / decimal.Decimal(h)
                area_below_mid += ratio * w * h

            if area_below_mid >= half_total_area:
                r = mid
            else:
                l = mid

        return (l + r) / 2


if __name__ == '__main__':
    x = Solution()
    # print(x.separateSquares([[0,0,1],[2,2,1]]), 1)
    # print(x.separateSquares([[0,0,2],[1,1,1]]), 1)
    # print(x.separateSquares([[0,0,9999999],[10000000,0,9999999],[0,9999999,1],[0,10000000,9999999],[10000000,10000000,9999999]]), 9999999.5)
    # print(x.separateSquares([[15,21,2],[19,21,3]]), 22.3)
    print(x.separateSquares([[11,13,1],[9,21,5]]), 23.4)
