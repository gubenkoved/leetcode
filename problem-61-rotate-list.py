from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None:
            return None

        def list_len(h):
            cur = h
            count = 0
            while cur is not None:
                cur = cur.next
                count += 1
            return count

        n = list_len(head)
        k = k % n

        if k == 0 or n == 1:
            return head

        left = head
        right = head

        for _ in range(k):
            right = right.next

        # now rewind to the end
        while right.next is not None:
            left = left.next
            right = right.next

        result = left.next
        left.next = None

        assert right.next is None
        right.next = head

        return result


if __name__ == '__main__':
    x = Solution()

    def print_list(head):
        cur = head

        while cur is not None:
            print('%s -> ' % cur.val, end='')

        print('NIL')

    print_list(x.rotateRight(ListNode(1, ListNode(2)), k=2))
