from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # see problem 287 for the best solution with O(1) memory
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        seen = set()

        while cur is not None:
            if cur in seen:
                return cur

            seen.add(cur)
            cur = cur.next

        return None
