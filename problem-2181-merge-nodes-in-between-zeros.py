from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        result_tail = None

        cur = head.next  # skip the first one
        sum_ = 0
        while cur is not None:
            if cur.val == 0:
                if result_tail is None:
                    result_head = ListNode(sum_)
                    result_tail = result_head
                else:
                    result_tail.next = ListNode(sum_)
                    result_tail = result_tail.next
                sum_ = 0
            else:
                sum_ += cur.val

            cur = cur.next

        return result_head
