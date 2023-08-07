from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = None
        traversed = 0

        def walk(node):
            nonlocal result
            nonlocal traversed

            if node.left:
                walk(node.left)

            traversed += 1

            if traversed == k:
                result = node

            if node.right:
                walk(node.right)

        walk(root)

        return result.val


if __name__ == '__main__':
    x = Solution()

    # [3,1,4,null,2]
    root = TreeNode(
        3,
        TreeNode(
            1,
            None,
            TreeNode(2)
        ),
        TreeNode(4),
    )
    print(x.kthSmallest(root, 1))
