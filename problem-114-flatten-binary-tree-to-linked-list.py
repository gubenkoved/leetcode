from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        rightmost = root

        while rightmost.right:
            rightmost = rightmost.right

        cutover = None
        last = None

        def walk(cur: TreeNode):
            nonlocal rightmost
            nonlocal cutover
            nonlocal last

            # first node after the root on pre-order traversal is where we are
            # going to stop
            if not cutover and cur is not root:
                cutover = cur
            elif cutover is cur:
                return

            last = cur

            # wire and update the rightmost node
            if cur is not root:
                rightmost.right = cur
                rightmost = cur

            cur_left = cur.left
            cur_right = cur.right

            if cur_left:
                walk(cur_left)

            if cur_right:
                walk(cur_right)

            # children are all walked
            cur.left = None

        walk(root)

        root.right = cutover
        last.right = None


if __name__ == '__main__':
    x = Solution()

    def case(root):
        x.flatten(root)
        pass

    # case(
    #     TreeNode(
    #         1,
    #         TreeNode(
    #             2,
    #             TreeNode(3),
    #             TreeNode(4),
    #         ),
    #         TreeNode(
    #             5,
    #             None,
    #             TreeNode(6)
    #         )
    #     )
    # )

    # case(
    #     TreeNode(
    #         1,
    #         TreeNode(2),
    #         None,
    #     )
    # )

    case(
        TreeNode(
            1,
            TreeNode(2),
            TreeNode(3),
        )
    )
