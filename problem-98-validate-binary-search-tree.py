from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_val, max_val):
            if node.val < min_val or node.val > max_val:
                return False

            if node.left:
                if not validate(node.left, min_val, node.val):
                    return False

            if node.right:
                if not validate(node.right, node.val, max_val):
                    return False

            return True

        if not root:
            return True

        return validate(root, -math.inf, math.inf)
