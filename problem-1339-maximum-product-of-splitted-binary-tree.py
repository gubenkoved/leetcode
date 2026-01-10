from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


M = 10 ** 9 + 7


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subtree_sum = {}

        def walk(node: TreeNode):
            if node.left:
                walk(node.left)

            if node.right:
                walk(node.right)

            subtree_sum[node] = subtree_sum.get(node.left, 0) + subtree_sum.get(node.right, 0) + node.val

        walk(root)

        # now when all the subtrees sums are caculated we need another traversal attempting to drop each of
        # the edges

        result = None

        def walk2(node: TreeNode):
            nonlocal result

            # now see what happens if we drop edge to left or right subtree
            if node.left:
                cur = subtree_sum[node.left] * (subtree_sum[root] - subtree_sum[node.left])
                if result is None or cur > result:
                    result = cur

                walk2(node.left)

            if node.right:
                cur = subtree_sum[node.right] * (subtree_sum[root] - subtree_sum[node.right])
                if result is None or cur > result:
                    result = cur

                walk2(node.right)

        walk2(root)

        return result % M
