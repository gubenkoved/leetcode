from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = l1
        ptr2 = l2
        result_head = None
        result_ptr = None
        carryover = False

        while ptr1 or ptr2 or carryover:
            val = (ptr1.val if ptr1 else 0) + (ptr2.val if ptr2 else 0)

            # handle current carryover
            if carryover:
                val += 1

            # carryover for the next
            if val >= 10:
                carryover = True
                val -= 10
            else:
                carryover = False

            result_node = ListNode(val)

            if result_ptr:
                result_ptr.next = result_node

            result_ptr = result_node

            if result_head is None:
                result_head = result_ptr

            # go next
            if ptr1:
                ptr1 = ptr1.next

            if ptr2:
                ptr2 = ptr2.next

        # handle last carry over
        return result_head


if __name__ == '__main__':

    def c(arr):
        head = None
        prev = None

        for val in arr:
            node = ListNode(val)

            if prev:
                prev.next = node
                prev = node
            else:
                prev = node

            if head is None:
                head = prev

        return head


    def print_list(head):
        cur = head

        while cur:
            print('%d -> ' % cur.val, end='')
            cur = cur.next

        print('NIL')


    x = Solution()
    print_list(x.addTwoNumbers(c([1, 2, 3]), c([2, 3, 4])))
    print_list(x.addTwoNumbers(c([9, 9, 9]), c([9, 9, 9])))
    print_list(x.addTwoNumbers(c([9, 9, 9]), c([0])))
    print_list(x.addTwoNumbers(c([9, 9, 9]), c([0, 1])))
