from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum = root.val
        best_level = 1

        level = 1
        nodes = [root]

        while nodes:
            level_sum = 0
            next_nodes = []
            for n in nodes:
                level_sum += n.val
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)

            if level_sum > max_sum:
                max_sum = level_sum
                best_level = level

            nodes = next_nodes
            level += 1

        return best_level
