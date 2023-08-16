from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def construct(a):
            if not a:
                return None

            mid = len(a) // 2
            root = TreeNode(a[mid])

            root.left = construct(a[:mid])
            root.right = construct(a[mid + 1:])

            return root

        return construct(nums)
