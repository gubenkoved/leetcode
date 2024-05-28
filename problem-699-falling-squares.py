from typing import List


class Solution:
    # the below probably only works if we add blocks in a way that
    # x coordinate is not decreasing, which is not the case
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        results = []

        # track blocks calculated vertical offset
        offsets = []

        def intersects(range_1, range_2):
            if range_1[0] > range_2[0]:
                range_1, range_2 = range_2, range_1
            return range_2[0] < range_1[1]

        rolling_max = 0

        # overall O(n^2) where n is amount of blocks
        for cur_left, cur_length in positions:
            ceiling = 0

            # check against all blocks currently present
            # NOTE: if self-balancing BST is used then this block can be turn
            # into the O(logn) with overall complexity turning to O(nlogn)
            for block_idx, block_offset in enumerate(offsets):
                block_left = positions[block_idx][0]
                block_right = block_left + positions[block_idx][1]

                if intersects((cur_left, cur_left + cur_length), (block_left, block_right)):
                    ceiling = max(ceiling, block_offset + positions[block_idx][1])

            offsets.append(ceiling)

            rolling_max = max(rolling_max, ceiling + cur_length)
            results.append(rolling_max)

        return results


if __name__ == '__main__':
    x = Solution()
    assert x.fallingSquares([[1, 2], [2, 3], [6, 1]]) == [2, 5, 5]
    assert x.fallingSquares([[6, 1], [9, 2], [2, 4]]) == [1, 2, 4]
