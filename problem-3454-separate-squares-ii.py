from typing import List
import decimal

decimal.getcontext().prec = 20

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
        for x, y, s in squares:
            # when our scanning line progresses from bottom to top we will need
            # to process 2 events: first new "range" [x, x + s] is added, then
            # after we go via it, it will be removed
            events.append((y, x, x + s, 'add'))
            events.append((y + s, x, x + s, 'del'))

        # sort events by y coordinate
        events.sort(key=lambda t: t[0])

        # "ranges" in scope -- the covered distance of them drives the "width" of
        # the equivalent rectangle
        prev_width = 0
        prev_y = 0
        in_scope = []

        # TODO: replace with something more efficient
        def in_scope_covered_width():
            events = []
            for x1, x2 in in_scope:
                events.append((x1, 0))
                events.append((x2, 1))
            events.sort()
            depth = 0
            result = 0
            segment_start = 0
            for x, type in events:
                if type == 0:
                    if depth == 0:
                        segment_start = x
                    depth += 1
                elif type == 1:
                    depth -= 1
                    if depth == 0:
                        result += x - segment_start
            return result

        for idx in range(len(events)):
            y, x1, x2, event_type = events[idx]
            if event_type == 'add':
                in_scope.append((x1, x2))
            elif event_type == 'del':
                in_scope.remove((x1, x2))

            # add a new rectangle (skip empty ones)
            # simple optimization: if there are multiple events for the same Y
            # only process the updated width once to save CPU
            if idx + 1 == len(events) or events[idx + 1][0] != y:
                if prev_width * (y - prev_y):
                    rectangles.append((prev_y, prev_width, y - prev_y))
                prev_width = in_scope_covered_width()
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
    print(x.separateSquares([[0,0,9999999],[10000000,0,9999999],[0,9999999,1],[0,10000000,9999999],[10000000,10000000,9999999]]), 9999999.5)
