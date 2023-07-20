from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head

        for _ in range(n):
            r = r.next

        while r and r.next:
            l = l.next
            r = r.next

        if r is None:
            return head.next

        l.next = l.next.next
        return head
