from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode(%s)' % self.val


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        deepest = 0
        depth_map = {}

        def walk(node, depth):
            nonlocal deepest

            if node.left:
                walk(node.left, depth + 1)

            if node.right:
                walk(node.right, depth + 1)

            depth_map[node] = depth
            deepest = max(deepest, depth)

        # calculate the depth map
        walk(root, 1)

        def min_subtree_with_all_deepest(node):
            if not node:
                return None

            if depth_map[node] == deepest:
                return node

            left_inner = min_subtree_with_all_deepest(node.left)
            right_inner = min_subtree_with_all_deepest(node.right)

            if left_inner and right_inner:
                return node

            return left_inner or right_inner

        return min_subtree_with_all_deepest(root)


if __name__ == '__main__':
    x = Solution()

    root = TreeNode(
        3,
        left=TreeNode(
            5,
            left=TreeNode(6),
            right=TreeNode(
                2,
                TreeNode(7),
                TreeNode(4),
            )
        ),
        right=TreeNode(
            1,
            left=TreeNode(0),
            right=TreeNode(0),
        ),
    )

    print(x.subtreeWithAllDeepest(root).val, 2)
