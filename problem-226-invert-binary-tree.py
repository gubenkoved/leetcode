from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if node is None:
                return None

            return TreeNode(
                node.val,
                left=invert(node.right),
                right=invert(node.left),
            )

        return invert(root)
