from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # less than 2 nodes?
        if head is None or head.next is None:
            return head

        result_head = head.next

        def swap(c1, c2, c3):
            tmp = c3.next
            if c1 is not None:
                c1.next = c3
            c3.next = c2
            c2.next = tmp

        cur1, cur2, cur3 = None, head, head.next
        while cur3 is not None:
            swap(cur1, cur2, cur3)

            cur1 = cur2
            cur2 = cur1.next
            cur3 = cur2.next if cur2 is not None else None

        return result_head


if __name__ == '__main__':

    def create(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        cur = head
        for x in arr[1:]:
            cur.next = ListNode(x)
            cur = cur.next
        return head


    def print_(head):
        cur = head
        while cur is not None:
            print('%s -> ' % cur.val, end='')
            cur = cur.next
        print('NIL')


    x = Solution()
    print_(x.swapPairs(create([])))
    print_(x.swapPairs(create([1])))
    print_(x.swapPairs(create([1, 2])))
    print_(x.swapPairs(create([1, 2, 3])))
    print_(x.swapPairs(create([1, 2, 3, 4])))
