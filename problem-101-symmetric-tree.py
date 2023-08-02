from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(left, right):
            if left and not right or not left and right:
                return False

            if not left and not right:
                return True

            # both are set if we are here
            if left.val != right.val:
                return False

            # check children
            if not check(left.left, right.right):
                return False

            if not check(left.right, right.left):
                return False

            return True

        return check(root, root)
