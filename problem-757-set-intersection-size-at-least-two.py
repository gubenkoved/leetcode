from typing import List


def in_range(start, end, num):
    return start <= num <= end


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        result = 0

        # two max values from the covering array
        a = float('-inf')
        b = float('-inf')

        for start, end in intervals:
            needed = 2

            if a is not None and in_range(start, end, a):
                needed -= 1

            if b is not None and in_range(start, end, b):
                needed -= 1

            x = end
            while needed > 0:
                if x != a and x != b:
                    # replace the smaller one
                    if a < b:
                        a = x
                    else:
                        b = x
                    needed -= 1
                    result += 1
                x -= 1

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.intersectionSizeTwo([[1,3], [3,7], [8,9]]), 5)
    print(x.intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7, 8]]), 5)  # 2, 3, 7, 6, 8
