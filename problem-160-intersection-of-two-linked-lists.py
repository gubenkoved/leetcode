from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def get_len(head):
            cur = head
            result = 0
            while cur:
                result += 1
                cur = cur.next
            return result

        def step(cur, n):
            result = cur
            k = n
            while k > 0 and result:
                result = result.next
                k -= 1
            return result

        a_len = get_len(headA)
        b_len = get_len(headB)

        a_ptr = headA
        b_ptr = headB

        if a_len > b_len:
            a_ptr = step(a_ptr, a_len - b_len)
        elif b_len > a_len:
            b_ptr = step(b_ptr, b_len - a_len)

        # now step with both pointers
        while a_ptr:
            if a_ptr is b_ptr:
                return a_ptr
            a_ptr = a_ptr.next
            b_ptr = b_ptr.next

        return None
