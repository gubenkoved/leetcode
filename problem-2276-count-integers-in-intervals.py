from sortedcontainers import SortedList


def size(interval):
    return interval[1] - interval[0] + 1


def intersects(interval1, interval2):
    if interval2[0] < interval1[0]:
        interval1, interval2 = interval2, interval1
    # consider "touching" intervals intersecting as well
    # like [1,2] and [2, 3] as they both include "2"
    return interval2[0] <= interval1[1]


def union(interval1, interval2):
    if interval2[0] < interval1[0]:
        interval1, interval2 = interval2, interval1
    return interval1[0], max(interval2[1], interval1[1])


class CountIntervals:
    def __init__(self):
        self.intervals = SortedList()
        self._count = 0

    def add(self, left: int, right: int) -> None:
        interval = left, right
        idx = self.intervals.bisect_left(interval)

        if idx > 0:
            left_interval = self.intervals[idx - 1]
            if left_interval[1] >= left:
                self.intervals.remove(left_interval)
                self._count -= size(left_interval)
                left = left_interval[0]
                right = max(right, left_interval[1])
                interval = left, right
                idx -= 1

        while idx < len(self.intervals):
            cur_interval = self.intervals[idx]
            if not intersects(cur_interval, interval):
                break
            self.intervals.pop(idx)
            self._count -= size(cur_interval)
            right = max(right, cur_interval[1])
            interval = left, right

        self.intervals.add(interval)
        self._count += size(interval)

    def count(self) -> int:
        return self._count


if __name__ == '__main__':
    x = CountIntervals()

    # x.add(39, 44)
    # x.add(13, 49)
    # assert x.count() == 37
    # x.add(47, 50)
    # assert x.count() == 38

    # x.add(33, 49)
    # x.add(43, 47)
    # x.add(37, 37)
    # x.add(26, 38)
    # x.add(11, 11)
    # assert x.count() == 25

    # [5, 10], [3, 5]
    # x.add(5, 10)
    # x.add(3, 5)
    # assert x.count() == 8

    x.add(5, 10)
    x.add(10, 12)
    assert x.count() == 8
