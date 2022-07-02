from typing import List, Optional


class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node[{self.value}]'


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def remove(self, node: Node):
        if node is self.head:
            self.head = node.next

            if self.head:
                self.head.prev = None

            if self.tail is node:
                self.tail = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            assert False, 'not supported yet'

    def insert_tail(self, value):
        node = Node(value)

        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            node.next = None
            self.tail = node
        else:
            self.head = node
            self.tail = node


class Solution:
    def maxSlidingWindow_v1(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        print(f'n={n}')
        result = []
        for idx in range(k, n + 1):
            window = sorted(nums[idx - k:idx])
            result.append(max(window))
        return result

    # O(n) where n is len of "nums" because every number goes into the "window" and out only once
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # window in a linked list where head is the biggest element in window
        # when we add element into the window we start from the tail and remove
        # all the items less than such element as they will never become the max
        # when we calculate the max in the window we look at the head of the list
        # and remove the element if it's out of scope already (keep the index
        # as part of the node itself, or in a separate hash map)
        # i've recalled this solution from the past
        window = LinkedList()

        def add_value(idx):
            val = nums[idx]

            while True:
                node = window.tail

                if node is None:
                    break

                node_val, node_idx = node.value
                if node_val >= val:
                    break
                window.remove(node)

            # insert at tail here
            window.insert_tail((val, idx))

        # initial window population
        for idx in range(k):
            add_value(idx)

        result = [window.head.value[0]]

        for idx in range(k, len(nums)):
            add_value(idx)

            max_val = None
            while True:
                max_val, max_val_idx = window.head.value
                if max_val_idx > idx - k:
                    break
                window.remove(window.head)

            assert max_val is not None

            result.append(max_val)
        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
    # print(x.maxSlidingWindow([1, -1], k=1))
    # f = open('input.txt')
    # a = [int(x) for x in f.read().replace('[', '').replace(']', '').split(',')]
    # a = eval(f.read())
    # print(x.maxSlidingWindow(a, k=50000))
