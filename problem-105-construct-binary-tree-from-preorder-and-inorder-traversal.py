from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def construct(cur_preorder, cur_inorder):
            if not cur_preorder:
                return None

            cur = TreeNode(cur_preorder[0])

            if len(cur_preorder) == 1:
                return cur

            cur_idx = cur_inorder.index(cur.val)

            in_order_left = cur_inorder[:cur_idx]
            in_order_right = cur_inorder[cur_idx + 1:]

            preorder_left = cur_preorder[1:cur_idx + 1]
            preorder_right = cur_preorder[cur_idx + 1:]

            if in_order_left:
                cur.left = construct(preorder_left, in_order_left)

            if in_order_right:
                cur.right = construct(preorder_right, in_order_right)

            return cur

        return construct(preorder, inorder)


if __name__ == '__main__':
    x = Solution()
    x.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
