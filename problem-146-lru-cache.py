class ListNode:
    __slots__ = ['next', 'prev', 'value']

    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, node: ListNode):
        if node is not self.head:
            if node is self.tail:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
        else:
            if self.tail is node:
                self.head = None
                self.tail = None
                return

            self.head = self.head.next
            self.head.prev = None

    def add_tail(self, value) -> ListNode:
        node = ListNode(value)
        self.add_tail_node(node)
        return node

    def add_tail_node(self, node) -> None:
        if self.tail is not None:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            assert self.head is None
            self.head = node
            self.tail = node


class LRUCache:
    def __init__(self, capacity: int):
        self.m = {}  # key -> Container dequeue
        self.linked_list = LinkedList()
        self.size = 0
        self.capacity = capacity

    def _update_lru(self, key):
        node = self.m.get(key)
        self.linked_list.remove(node)
        self.linked_list.add_tail_node(node)

    def _evict(self):
        node = self.linked_list.head
        key, v_ = node.value
        self.linked_list.remove(node)
        self.m.pop(key)

    def get(self, key: int) -> int:
        if key not in self.m:
            return -1
        self._update_lru(key)
        return self.m.get(key).value[1]

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            self.m[key].value = (key, value)
            self._update_lru(key)
        else:
            node = self.linked_list.add_tail((key, value))

            self.m[key] = node

            self.size += 1

            # evict if needed
            if self.size > self.capacity:
                self._evict()


if __name__ == '__main__':
    x = LRUCache(capacity=3)
    x.put(1, 1)
    x.put(2, 2)
    x.put(3, 3)

    print(x.get(2))

    x.put(4, 4)
    x.put(5, 5)

    print(x.get(1))
    print(x.get(2))
    print(x.get(3))
