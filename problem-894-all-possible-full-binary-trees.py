from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n == 1:
            return [TreeNode(0)]

        if n % 2 == 0:
            return []

        results = []

        for left_count in range(1, n, 2):
            left_subtrees = self.allPossibleFBT(left_count)
            right_subtrees = self.allPossibleFBT(n - left_count - 1)

            for left_subtree_root in left_subtrees:
                for right_subtree_root in right_subtrees:
                    root = TreeNode(0)
                    root.left = left_subtree_root
                    root.right = right_subtree_root
                    results.append(root)

        return results


if __name__ == '__main__':
    x = Solution()

    def case(m):
        result = x.allPossibleFBT(m)
        print('found %d trees' % len(result))

    case(1)
    case(2)
    case(3)
    case(4)
    case(5)
