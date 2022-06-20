from typing import List, Optional


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return f'Node[{self.value}]'


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur
            cur = cur.next

    def remove(self, node):
        if node.prev:
            node.prev.next = node.next

            if node.next:
                node.next.prev = node.prev
        else:  # no previous
            self.head = node.next

            if node.next:
                node.next.prev = None

    def insert(self, after, value):
        # insert at first position
        if after is None:
            if self.head is not None:
                node = Node(value)
                node.next = self.head
                self.head.prev = node
                self.head = node
            else:  # empty list
                self.head = Node(value)
        else:  # insert after some existing node
            node = Node(value)
            node.next = after.next
            node.prev = after
            if after.next:
                after.next.prev = node
            after.next = node


class SummaryRanges:
    def __init__(self):
        self.intervals = LinkedList()

    def addNum(self, val: int) -> None:
        node = None
        for node in self.intervals:
            interval = node.value
            if interval[0] <= val <= interval[1]:
                # within the interval already -- could that happen?
                break  # do nothing
            elif val == interval[0] - 1:
                # grow left
                interval[0] -= 1

                # merge with previous
                if node.prev is not None and node.prev.value[1] + 1 == interval[0]:
                    interval[0] = node.prev.value[0]
                    self.intervals.remove(node.prev)
                break
            elif val == interval[1] + 1:
                # grow right
                interval[1] += 1
                # merge with next
                if node.next and node.next.value[0] - 1 == interval[1]:
                    interval[1] = node.next.value[1]
                    self.intervals.remove(node.next)
                break
            elif (node.prev is None or node.prev.value[1] < val - 1) and (
                node.value[0] > val + 1
            ):
                # insert new interval
                self.intervals.insert(after=node.prev, value=[val, val])
                break
        else:
            # add new interval at the very end
            self.intervals.insert(after=node, value=[val, val])

    def getIntervals(self) -> List[List[int]]:
        # print([x.value for x in self.intervals])
        return [x.value for x in self.intervals]


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()


if __name__ == '__main__':
    x = SummaryRanges()
    x.addNum(6)
    x.addNum(6)
    x.getIntervals()
    x.addNum(0)
    x.getIntervals()
    x.addNum(4)
    x.getIntervals()
    x.addNum(8)
    x.addNum(7)
    x.getIntervals()
    x.addNum(6)
    x.addNum(4)
    x.getIntervals()
    x.addNum(7)
    x.getIntervals()
    x.addNum(5)
    x.getIntervals()
