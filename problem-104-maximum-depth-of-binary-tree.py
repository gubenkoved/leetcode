from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # BFS or DFS -- does no really matter, we still have to traverse whole tree
        max_depth = 1
        stack = [(root, 1)]
        while stack:
            node, depth = stack.pop(-1)

            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))

            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth

