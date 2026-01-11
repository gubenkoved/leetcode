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
        max_subtree_depth = {}
        deepest = 0

        def walk(node, depth):
            nonlocal deepest

            if node.left:
                walk(node.left, depth + 1)

            if node.right:
                walk(node.right, depth + 1)

            max_subtree_depth[node] = max(
                max_subtree_depth.get(node.left, 0),
                max_subtree_depth.get(node.right, 0),
                depth,
            )

            deepest = max(deepest, depth)

        # capture max depth
        walk(root, 1)

        result = None

        # find the node which has both left and right subtrees of the same deepest depth
        # OR there is just a single node with such depth
        def walk2(node):
            nonlocal result

            if node.left:
                walk2(node.left)

            if node.right:
                walk2(node.right)

            if node.left and node.right:
                if max_subtree_depth[node.left] == deepest and max_subtree_depth[node.right] == deepest:
                    result = node
            elif node.left or node.right:
                # if we have only left or only right it is never an answer as we can just go level down
                pass
            else:
                if max_subtree_depth[node] == deepest:
                    result = node

        walk2(root)

        return result


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
