from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by the start
        intervals = sorted(intervals, key=lambda x: x[0])

        n = len(intervals)
        left_idx = 0
        right_idx = 0
        results = []

        while left_idx < n:
            reference = intervals[left_idx][1]

            while right_idx + 1 < n and intervals[right_idx + 1][0] <= reference:
                # collides with the next, move forward
                right_idx += 1
                reference = max(reference, intervals[right_idx][1])

            # emit interval
            results.append([intervals[left_idx][0], reference])

            # go further
            left_idx = right_idx + 1
            right_idx = left_idx

        return results


if __name__ == '__main__':
    x = Solution()
    # print(x.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # print(x.merge([[1, 4], [4, 5]]))
    print(x.merge([[1, 4], [2, 3]]))
