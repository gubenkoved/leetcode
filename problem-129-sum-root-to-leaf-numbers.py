from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        result = 0

        def walk(cur: TreeNode, root_path: List[int]):
            nonlocal result

            if cur.left is None and cur.right is None:
                numbers = root_path + [cur.val]
                number = int(''.join(str(n) for n in numbers))
                result += number
            else:
                if cur.left:
                    walk(cur.left, root_path + [cur.val])

                if cur.right:
                    walk(cur.right, root_path + [cur.val])

        if root:
            walk(root, [])

        return result
