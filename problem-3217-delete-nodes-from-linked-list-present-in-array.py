from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)

        result_head = None
        result_tail = None

        cur = head

        while cur is not None:
            if cur.val not in nums:

                if result_head is None:
                    result_head = ListNode(cur.val)
                    result_tail = result_head
                else:
                    result_tail.next = ListNode(cur.val)
                    result_tail = result_tail.next

            cur = cur.next

        return result_head
