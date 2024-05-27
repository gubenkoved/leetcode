from typing import List, Tuple
import bisect


# process END of the interval if it is the same time before the START
START = 1
END = 0


class MyCalendarThree:
    def __init__(self):
        self.intervals: List[Tuple[int, int]] = []

    def book(self, startTime: int, endTime: int) -> int:
        # O(n)
        bisect.insort(self.intervals, (startTime, START))
        bisect.insort(self.intervals, (endTime, END))
        max_count = 0
        cur_count = 0
        # O(n)
        for time, event in self.intervals:
            if event == START:
                cur_count += 1
                max_count = max(max_count, cur_count)
            elif event == END:
                cur_count -= 1
        return max_count


if __name__ == '__main__':
    def check(bookings, expected):
        print('checking for %s bookings...' % bookings)
        x = MyCalendarThree()
        results = []
        for booking in bookings:
            results.append(x.book(booking[0], booking[1]))
            # if results != expected[:len(results)]:
            #     assert False, 'Failed at %s, expected %s, got %s' % (booking, expected[len(results) - 1], results[-1])
        assert expected == results, '%s != %s (expected, actual)' % (expected, results)

    check(
        [[10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        [1, 1, 2, 3, 3, 3],
    )
    check(
        [[47, 50], [1, 10], [27, 36], [40, 47], [20, 27], [15, 23], [10, 18]],
        [1, 1, 1, 1, 1, 2, 2],
    )
    check(
        [[47, 50], [1, 10], [27, 36], [40, 47], [20, 27], [15, 23], [10, 18], [27, 36], [17, 25]],
        [1, 1, 1, 1, 1, 2, 2, 2, 3]
    )
    check(
        [[47, 50], [1, 10], [27, 36], [40, 47], [20, 27], [15, 23], [10, 18], [27, 36], [17, 25], [8, 17], [24, 33],
         [23, 28], [21, 27], [47, 50], [14, 21], [26, 32], [16, 21], [2, 7], [24, 33], [6, 13], [44, 50], [33, 39],
         [30, 36], [6, 15], [21, 27], [49, 50], [38, 45], [4, 12], [46, 50], [13, 21]],
        [1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7]
    )
