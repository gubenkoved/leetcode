from typing import List


def in_range(start, end, num):
    return start <= num <= end


class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        nums = set()
        intervals.sort(key=lambda interval: interval[1])

        for start, end in intervals:
            count = sum(1 for x in nums if in_range(start, end, x))

            if count < 2:
                needed = 2 - count
                x = end
                while needed > 0:
                    if x not in nums:
                        nums.add(x)
                        needed -= 1
                    x -= 1

        return len(nums)


if __name__ == '__main__':
    x = Solution()
    # print(x.intersectionSizeTwo([[1,3], [3,7], [8,9]]), 5)
    print(x.intersectionSizeTwo([[1, 3], [3, 7], [5, 7], [7, 8]]), 5)  # 2, 3, 7, 6, 8
