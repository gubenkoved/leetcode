from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return '<ListNode val=%s>' % self.val


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        prev = head
        cur = head.next
        idx = 1

        reverse_first = None
        reverse_before_first = None
        reverse_last = None
        reverse_after_last = None

        while cur is not None:
            # save pointers so that we can mess with them
            prev_next = cur
            cur_next = cur.next

            if idx == left:
                reverse_first = prev
            elif idx == left - 1:
                reverse_before_first = prev

            if idx == right - 1:
                reverse_last = cur
                reverse_after_last = cur.next

            if idx >= left and idx < right:
                cur.next = prev

            prev, cur = prev_next, cur_next
            idx += 1

        # wire up last pointers
        reverse_first.next = reverse_after_last

        if reverse_before_first is not None:
            reverse_before_first.next = reverse_last
            return head
        else:
            assert left == 1
            return reverse_last


if __name__ == '__main__':
    def create_list(a):
        head = ListNode(a[0])
        cur = head

        for val in a[1:]:
            cur.next = ListNode(val)
            cur = cur.next

        return head

    def print_list(head):
        cur = head

        while cur is not None:
            print('%s -> ' % cur.val, end='')
            cur = cur.next

        print('NIL')

    def case(array, left, right):
        x = Solution()
        head = create_list(array)
        print_list(head)
        head2 = x.reverseBetween(head, left, right)
        print_list(head2)

    # case([1, 2, 3, 4, 5], 2, 4)
    # case([1, 2, 3, 4, 5], 1, 5)
    # case([1, 2, 3], 1, 3)
    # case([1, 2], 1, 2)
    case([5], 1, 1)
