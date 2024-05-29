from typing import List, Tuple


class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def range_overlap(one: Tuple[int, int], two: Tuple[int, int]) -> Tuple[int, int] | None:
            if one[0] > two[0]:
                one, two = two, one
            if two[0] < one[1]:
                return two[0], min(one[1], two[1])
            return None

        def range_subtract(range: Tuple[int, int], to_subtract: Tuple[int, int]) -> List[Tuple[int, int]]:
            overlap = range_overlap(range, to_subtract)

            if overlap is None:
                # unchanged as there is no overlap
                return [range]

            result = []
            if range[0] != overlap[0]:
                result.append((range[0], overlap[0]))
            if range[1] != overlap[1]:
                result.append((overlap[1], range[1]))

            return result

        def subtract(rect, to_subtract_rect) -> List:
            # subtracts one rectangle from another, it is possible to have
            # multiple rectangles in the result:
            # 0 rectangles when we subtract whole source rectangle with nothing left
            # 1 rectangle when we either did not subtract anything or we subtract in a way
            #   that some "half" of the original rectangle is cut
            # 2 rectangles when we subtracted a "corner" of the rectangle so that
            #   the result is no longer can be represented as a single rectangle;
            #   or when the middle part is taken away
            # 3 when the center part is subtracted

            rect_x = rect[0], rect[2]
            rect_y = rect[1], rect[3]

            to_subtract_rect_x = to_subtract_rect[0], to_subtract_rect[2]
            to_subtract_rect_y = to_subtract_rect[1], to_subtract_rect[3]

            x_overlap = range_overlap(rect_x, to_subtract_rect_x)
            y_overlap = range_overlap(rect_y, to_subtract_rect_y)

            if not x_overlap or not y_overlap:
                # at least one coordinate does not overlap -> NO overlap at all
                # meaning the original rect is not changed
                return [rect]

            # if we got here, it means there is an overlap

            # check for full overlap meaning complete subtraction
            if x_overlap == rect_x and y_overlap == rect_y:
                # nothing left from the original rectangle
                return []

            x_subtracted = range_subtract(rect_x, x_overlap)
            y_subtracted = range_subtract(rect_y, y_overlap)

            assert x_subtracted or y_subtracted

            result = []
            for y_leftover in y_subtracted:
                # full size by x
                result.append([rect_x[0], y_leftover[0], rect_x[1], y_leftover[1]])

            for x_leftover in x_subtracted:
                # overlap by y
                result.append([x_leftover[0], y_overlap[0], x_leftover[1], y_overlap[1]])

            return result

        def subtract_many(rect: List, to_subtract: List) -> List:
            # subtracts many (potentially overlapping) rectangles from some
            # single rectangle; returns resulting rectangles that were
            # never subtracted
            cur = [rect]

            for rect_to_subtract in to_subtract:
                cur, copy = [], cur
                for rect_from in copy:
                    cur.extend(subtract(rect_from, rect_to_subtract))

            return cur

        def area(rect: List):
            assert rect[2] > rect[0]
            assert rect[3] > rect[1]
            return (rect[2] - rect[0]) * (rect[3] - rect[1])

        result = 0
        processed = []
        for rect in rectangles:
            leftover = subtract_many(rect, to_subtract=processed)
            result += sum(area(rect) for rect in leftover)
            processed.append(rect)

        return result % (10 ** 9 + 7)


if __name__ == '__main__':
    x = Solution()
    assert x.rectangleArea([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]]) == 6
    assert x.rectangleArea([[0, 0, 1000000000, 1000000000]]) == 49
    assert x.rectangleArea([[0, 0, 10, 1], [0, 0, 1, 10]]) == 19
    assert x.rectangleArea([[0, 0, 10, 1], [0, 0, 1, 10], [0, 0, 1, 1]]) == 19
    assert x.rectangleArea([[0, 0, 10, 1], [0, 0, 1, 10], [0, 0, 2, 2]]) == 20
    assert x.rectangleArea([[0, 0, 10, 1], [0, 0, 1, 10], [1, 1, 2, 2]]) == 20
    assert x.rectangleArea([[0, 0, 10, 1], [0, 0, 1, 10], [0, 0, 3, 3]]) == 23
    assert x.rectangleArea([[22, 24, 67, 34], [23, 18, 39, 41], [10, 63, 80, 98]]) == 3108
