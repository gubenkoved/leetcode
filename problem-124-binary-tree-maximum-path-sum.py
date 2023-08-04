import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path_sum_map = {}

        def walk(cur: TreeNode, depth: int):
            print('%d, depth %d' % (cur.val, depth))

            sub_result = 0

            if cur.left:
                sub_result = max(0, walk(cur.left, depth + 1))

            if cur.right:
                right_result = max(0, walk(cur.right, depth + 1))
                sub_result = max(sub_result, right_result)

            cur_result = cur.val + sub_result
            max_path_sum_map[cur] = cur_result
            return cur_result

        # precalculate max path sums
        walk(root, 0)

        # for each node -- assume it is a root of the result and calculate the
        # sum of the max sum paths for left and right subtrees

        best_result = -1001

        def walk2(cur: TreeNode):
            nonlocal best_result

            cur_result = cur.val

            if cur.left:
                cur_result += max(0, max_path_sum_map[cur.left])

            if cur.right:
                cur_result += max(0, max_path_sum_map[cur.right])

            best_result = max(best_result, cur_result)

            if cur.left:
                walk2(cur.left)

            if cur.right:
                walk2(cur.right)

        walk2(root)

        return best_result
