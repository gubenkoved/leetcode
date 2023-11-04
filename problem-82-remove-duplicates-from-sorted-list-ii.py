from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        result_head = None
        result_tail = None
        prev = head
        cur = head.next

        while prev is not None:
            if cur is not None and cur.val == prev.val:
                # non unique
                while cur is not None and cur.val == prev.val:
                    cur = cur.next

                prev = cur
                cur = cur.next if cur is not None else None
            else:
                # node under "prev" is unique
                node = ListNode(prev.val)

                if result_head is None:
                    result_head = node
                    result_tail = node
                else:
                    result_tail.next = node
                    result_tail = node

                prev = cur
                cur = cur.next if cur is not None else None

        return result_head
