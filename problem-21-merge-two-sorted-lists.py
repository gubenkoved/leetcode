from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        result_cur = None

        cur1 = list1
        cur2 = list2

        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val < cur2.val:
                    node = ListNode(cur1.val)
                    cur1 = cur1.next
                else:
                    node = ListNode(cur2.val)
                    cur2 = cur2.next
            elif cur1:
                node = ListNode(cur1.val)
                cur1 = cur1.next
            else:
                node = ListNode(cur2.val)
                cur2 = cur2.next

            if result_cur is not None:
                result_cur.next = node
                result_cur = node
            else:
                result_cur = node
                result_head = node

        return result_head
