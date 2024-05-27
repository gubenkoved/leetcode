import bisect
from typing import List, Tuple


class MyCalendarThree:

    def __init__(self):
        self.intervals: List[Tuple[int, int]] = []

    # naive implementation via rearranging all the intervals every time from the
    # very start
    def book(self, startTime: int, endTime: int) -> int:
        bisect.insort(self.intervals, (startTime, endTime))
        layers = [[]]
        for interval in self.intervals:
            self.book_impl(layers, *interval)
        return len(layers)

    def book_impl(self, layers, startTime, endTime):

        is_handled = False
        for layer_idx in range(len(layers)):
            layer = layers[layer_idx]

            candidate_idx = 0
            while candidate_idx != len(layer) and layer[candidate_idx][0] < startTime:
                candidate_idx += 1

            # now check that in this layer it does not intersect with neither left
            # nor right interval
            fits = True
            if candidate_idx > 0:
                if startTime < layer[candidate_idx - 1][1]:
                    fits = False
            if candidate_idx != len(layer):
                if endTime > layer[candidate_idx][0]:
                    fits = False

            if fits:
                layer.insert(candidate_idx, (startTime, endTime))
                # print('adding (%s, %s) to layer %s' % (startTime, endTime, layer_idx))
                is_handled = True
                break

        if not is_handled:
            # adding a new layer
            # print('adding new layer for (%s, %s)' % (startTime, endTime))
            layers.append([(startTime, endTime)])


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
