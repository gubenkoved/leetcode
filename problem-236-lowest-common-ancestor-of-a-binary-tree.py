class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lcd = None

        def walk(cur):
            nonlocal lcd

            p_found, q_found = 0, 0

            if cur.left:
                p_found2, q_found2 = walk(cur.left)
                p_found = max(p_found, p_found2)
                q_found = max(q_found, q_found2)

            if cur.right:
                p_found2, q_found2 = walk(cur.right)
                p_found = max(p_found, p_found2)
                q_found = max(q_found, q_found2)

            if cur is p:
                p_found = 1
            if cur is q:
                q_found = 1

            if p_found and q_found and lcd is None:
                lcd = cur

            return p_found, q_found

        walk(root)

        return lcd
