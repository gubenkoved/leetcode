from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, val):
        node = ListNode(val)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # go via list and move nodes which are more than or equal to "x" to another
        # list, then merge the result

        cur = head

        part1 = LinkedList()
        part2 = LinkedList()

        while cur is not None:
            if cur.val >= x:
                part2.append(cur.val)
            else:
                part1.append(cur.val)

            # go to next one
            cur = cur.next

        # merge result
        if part1.head is None:
            return part2.head

        part1.tail.next = part2.head

        return part1.head


if __name__ == '__main__':
    def create_list(a):
        if not a:
            return None

        head = ListNode(a[0])
        tail = head

        for val in a[1:]:
            node = ListNode(val)
            tail.next = node
            tail = node

        return head


    def print_list(a):
        cur = a

        while cur is not None:
            print('%s -> ' % cur.val, end='')
            cur = cur.next

        print('NIL')


    solution = Solution()

    def case(a, x):
        head = create_list(a)
        print_list(head)
        result = solution.partition(head, x)
        print_list(result)


    case([1, 4, 3, 2, 5, 2], 3)
