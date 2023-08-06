from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        cur = head.next

        head.next = None

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        return prev

