from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        count = 0

        def walk(node, path):
            nonlocal count

            if node.left:
                walk(node.left, path + [node])

            if node.right:
                walk(node.right, path + [node])

            sum = 0

            for node_ in reversed(path + [node]):
                sum += node_.val

                if sum == targetSum:
                    count += 1

        if root:
            walk(root, [])

        return count


if __name__ == '__main__':
    x = Solution()
    # [10,5,-3,3,2,null,11,3,-2,null,1]
    print(x.pathSum(TreeNode(
        10,
        TreeNode(
            5,
            TreeNode(
                3,
                TreeNode(3),
                TreeNode(-2),
            ),
            TreeNode(
                2,
                None,
                TreeNode(1),
            ),
        ),
        TreeNode(
            -3,
            TreeNode(11)
        ),
    ), 8))
