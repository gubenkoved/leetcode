class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_path = []
        q_path = []

        def walk(cur, path):
            nonlocal p_path
            nonlocal q_path

            if cur.left:
                walk(cur.left, path + [cur])

            if cur.right:
                walk(cur.right, path + [cur])

            if cur is p:
                p_path = path + [cur]

            if cur is q:
                q_path = path + [cur]

        walk(root, [])

        lcd = root

        for idx in range(len(p_path)):
            if idx >= len(q_path) or p_path[idx] is not q_path[idx]:
                break
            lcd = p_path[idx]

        return lcd
