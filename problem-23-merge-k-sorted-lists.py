from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cursors_ptrs = list(lists)
        cursors = [(cursor.val, idx) for idx, cursor in enumerate(cursors_ptrs)
                   if cursor is not None]

        heapq.heapify(cursors)

        # find node with min value and advances the cursor
        def advance():
            if not cursors:
                return None

            min_val, cursor_idx = heapq.heappop(cursors)
            cursor = cursors_ptrs[cursor_idx]

            # advance the cursor
            if cursor.next is not None:
                cursors_ptrs[cursor_idx] = cursor.next
                heapq.heappush(cursors, (cursor.next.val, cursor_idx))

            return min_val

        head = None
        cur = None

        while True:
            next_val = advance()

            if next_val is None:
                break

            node = ListNode(next_val)

            if cur is not None:
                cur.next = node
            else:
                head = node

            cur = node

        return head


def to_linked_list(lst):
    head = ListNode(lst[0])
    cur = head

    for val in lst[1:]:
        node = ListNode(val)
        cur.next = node
        cur = node

    return head


def enumerate_linked_list(head: ListNode):
    cur = head

    while cur:
        yield cur.val
        cur = cur.next


if __name__ == '__main__':
    x = Solution()
    # print(list(enumerate_linked_list(
    #     x.mergeKLists([
    #         to_linked_list([1, 4, 5]),
    #         to_linked_list([1, 3, 4]),
    #         to_linked_list([2, 6]),
    #     ])
    # )))
    # print(list(enumerate_linked_list(
    #     x.mergeKLists([None])
    # )))
    pass
