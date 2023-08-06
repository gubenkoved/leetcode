from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        data = []

        cur = head
        while cur:
            data.append(cur.val)
            cur = cur.next

        n = len(data)
        for idx in range(0, n // 2):
            if data[idx] != data[n - 1 - idx]:
                return False
        return True
