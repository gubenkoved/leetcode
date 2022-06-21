from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'Node[{self.val}]'


def ahead(cur, k):
    steps = 0
    while k != 0 and cur:
        steps += 1
        cur = cur.next
        k -= 1
    return cur, steps


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        new_head = None
        prev_group_first_cursor = None

        while True:
            group_start_cursor = cur
            next_group_cursor, stepped = ahead(cur, k)
            is_group_full = stepped == k

            # so that first element "next" pointer points to the leftover part
            # (handles last non-full chunk as well)
            prev = next_group_cursor

            # make k steps inverting "next" ptr
            # only invert if the group is full
            if is_group_full:
                for _ in range(k):
                    tmp = cur.next
                    cur.next = prev
                    prev = cur
                    cur = tmp

            # after inverting first group we can update new head pointer
            if new_head is None:
                new_head = prev  # << group head after reverse

            if prev_group_first_cursor and is_group_full:
                # wire up previous group first item (last after reverse) to the
                # last item in the current group (first after reverse)
                prev_group_first_cursor.next = prev

            prev_group_first_cursor = group_start_cursor

            if next_group_cursor is None:
                break

        # new_head can be None if list is shorter than k
        return new_head or head


def to_linked_list(lst):
    head = ListNode(lst[0])
    cur = head

    for val in lst[1:]:
        node = ListNode(val)
        cur.next = node
        cur = node

    return head


def to_list(head):
    def walk():
        cur = head
        while cur:
            yield cur.val
            cur = cur.next
    return list(walk())


if __name__ == '__main__':
    x = Solution()
    print(to_list(x.reverseKGroup(to_linked_list([1, 2, 3, 4, 5]), 2)))
    print(to_list(x.reverseKGroup(to_linked_list([1, 2, 3, 4, 5]), 3)))
    print(to_list(x.reverseKGroup(to_linked_list([1, 2]), 2)))
