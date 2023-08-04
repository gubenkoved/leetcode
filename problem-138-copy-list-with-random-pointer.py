from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        # construct new list w/o random pointer
        new_head = Node(head.val)
        old_cur = head.next
        new_prev = new_head

        old_to_new_map = {}
        old_to_new_map[head] = new_head

        while old_cur is not None:
            new_node = Node(old_cur.val)
            new_prev.next = new_node
            new_prev = new_node
            old_to_new_map[old_cur] = new_node
            old_cur = old_cur.next

        # now init the random pointer
        cur = head
        while cur is not None:
            if cur.random:
                new_node = old_to_new_map[cur]
                new_node.random = old_to_new_map[cur.random]
            cur = cur.next

        return new_head
