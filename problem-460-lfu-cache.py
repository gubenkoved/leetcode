from typing import Any, Optional, TypeVar, Generic, Tuple


TKey = TypeVar('TKey')
TValue = TypeVar('TValue')
Missing = object()


class LinkedListItem(Generic[TValue]):
    def __init__(self, value: TValue, parent: 'LinkedList[TValue]'):
        self.value: TValue = value
        self.parent: LinkedList[TValue] = parent
        self.next: Optional[LinkedListItem[TValue]] = None
        self.prev: Optional[LinkedListItem[TValue]] = None

    def __repr__(self):
        return '<LinkedListItem value="%s">' % (self.value, )


class LinkedList(Generic[TValue]):
    def __init__(self):
        self.head: Optional[LinkedListItem[TValue]] = None
        self.tail: Optional[LinkedListItem[TValue]] = None

    def delete(self, item: LinkedListItem[TValue]) -> None:
        assert item.parent == self

        if item is self.head:
            return self.delete_head()

        if item is self.tail:
            return self.delete_tail()

        # item is in the middle (neither head nr tail)
        prev = item.prev
        next = item.next

        assert prev is not None
        assert next is not None

        prev.next = next
        next.prev = prev

    def delete_head(self):
        assert self.head is not None
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None

    def delete_tail(self):
        assert self.tail is not None
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None

    def insert_before(self, before: LinkedListItem[TValue], value: TValue) -> LinkedListItem[TValue]:
        prev = before.prev

        if prev is None:
            return self.insert_head(value)

        item = LinkedListItem(value, parent=self)
        prev.next = item
        before.prev = item
        item.prev = prev
        item.next = before
        return item

    def insert_tail(self, value: TValue) -> LinkedListItem[TValue]:
        item = LinkedListItem(value, parent=self)
        item.prev = self.tail
        if self.tail:
            self.tail.next = item
        self.tail = item
        if self.head is None:
            self.head = item
        return item

    def insert_head(self, value: TValue) -> LinkedListItem[TValue]:
        item = LinkedListItem(value, parent=self)
        item.next = self.head
        if self.head:
            self.head.prev = item
        self.head = item
        if self.tail is None:
            self.tail = item
        return item


class FreqList(LinkedList[Tuple[int, 'LRUBucket']]):
    def ensure_freq1_bucket(self) -> LinkedListItem[Tuple[int, 'LRUBucket']]:
        if self.tail is None or self.tail.value[0] != 1:
            # no buckets at all
            lru_bucket = LRUBucket()
            item = self.insert_tail((1, lru_bucket))
            lru_bucket.freq_list_item = item
        return self.tail

    def ensure_next_freq_bucket(self, freq_item: LinkedListItem[Tuple[int, 'LRUBucket']]):
        assert freq_item.parent == self

        next_frequency = freq_item.value[0] + 1

        if freq_item.prev is None or freq_item.prev.value[0] != next_frequency:
            lru_bucket = LRUBucket()
            new_freq_item = self.insert_before(freq_item, (next_frequency, lru_bucket))
            lru_bucket.freq_list_item = new_freq_item
            return new_freq_item

        assert freq_item.prev.value[0] == next_frequency

        return freq_item.prev


class LRUBucket(LinkedList[Tuple[TKey, TValue]]):
    def __init__(self):
        super().__init__()
        # each LRU bucket is associated with specific frequency
        self.freq_list_item: Optional[LinkedListItem[Tuple[int, 'LRUBucket']]] = None


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq_list = FreqList()
        # key -> LRUBucket item
        self.index = {}
        self.count = 0

    def _evict(self):
        freq_list_item: LinkedListItem = self.freq_list.tail
        lru_bucket: LRUBucket = freq_list_item.value[1]
        lru_bucket_item = lru_bucket.tail
        key, val = lru_bucket_item.value

        # update the index
        self.index.pop(key)

        lru_bucket.delete(lru_bucket_item)

        # remove whole LRU bucket is needed
        if lru_bucket.head is None:
            self.freq_list.delete(freq_list_item)

    def _promote(self, lru_bucket_item: LinkedListItem, update_value: Any = Missing):
        lru_bucket: LRUBucket = lru_bucket_item.parent
        freq_list_item = lru_bucket.freq_list_item
        freq_list: FreqList = freq_list_item.parent

        # remove item from the old LRU bucket since frequency increases!
        lru_bucket.delete(lru_bucket_item)

        new_freq_list_item = freq_list.ensure_next_freq_bucket(freq_list_item)

        _, new_lru_bucket = new_freq_list_item.value

        new_value = lru_bucket_item.value[1]

        if update_value is not Missing:
            new_value = update_value

        new_lru_bucket_item = new_lru_bucket.insert_head(
            value=(lru_bucket_item.value[0], new_value))

        # remove old LRU bucket completely if empty
        if lru_bucket.head is None:
            freq_list.delete(freq_list_item)

        return new_lru_bucket_item

    def get(self, key: int) -> int:
        lru_bucket_item: LinkedListItem = self.index.get(key)

        if lru_bucket_item is None:
            return -1

        new_lru_item = self._promote(lru_bucket_item)
        self.index[key] = new_lru_item

        _, value = lru_bucket_item.value

        return value

    def put(self, key: int, value: int) -> None:
        lru_bucket_item: LinkedListItem = self.index.get(key)

        if lru_bucket_item is None:
            # new item is being added

            if self.count + 1 > self.capacity:
                # evict if we will go over capacity first!
                self._evict()

            lfu_item = self.freq_list.ensure_freq1_bucket()
            _, lru_bucket = lfu_item.value
            lru_bucket_item = lru_bucket.insert_head((key, value))
            self.index[key] = lru_bucket_item
            self.count += 1
        else:
            # updating value for existing one
            new_lru_item = self._promote(lru_bucket_item, update_value=value)
            self.index[key] = new_lru_item


if __name__ == '__main__':
    x = LFUCache(capacity=2)

    x.put(1, 1)
    x.put(2, 2)
    assert x.get(1) == 1
    x.put(3, 3)
    assert x.get(2) == -1
    assert x.get(3) == 3
    x.put(4, 4)
    assert x.get(1) == -1
    assert x.get(3) == 3
    assert x.get(4) == 4
