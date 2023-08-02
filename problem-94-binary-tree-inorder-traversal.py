from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def walk(node):
            if node.left:
                walk(node.left)
            result.append(node.val)
            if node.right:
                walk(node.right)

        if root:
            walk(root)

        return result
