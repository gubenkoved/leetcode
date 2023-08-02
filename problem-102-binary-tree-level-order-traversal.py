from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque()
        queue.append((root, 0))

        level_idx = 0
        level = []
        while queue:
            node, node_level_idx = queue.popleft()

            if node_level_idx != level_idx:
                result.append(level)
                level = []
                level_idx = node_level_idx

            level.append(node.val)

            if node.left:
                queue.append((node.left, node_level_idx + 1))

            if node.right:
                queue.append((node.right, node_level_idx + 1))

        # add last level
        if level:
            result.append(level)

        return result
