# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# we can not use simple set because we need ability to
# index the items so that we can get random item just by generating
# random index, so instead we can store data in both array and hashmap
# to be both fast to lookup and fast to access by index

import random


class RandomizedSetNode:
    def __init__(self, value):
        self.value = value


class RandomizedSet:
    def __init__(self):
        self.array = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        node = RandomizedSetNode(val)
        self.array.append(val)
        self.map[val] = node
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        self.map.pop(val)

        array_fill_factor = len(self.map) / len(self.array)

        if array_fill_factor < 0.5:
            self.array = list(self.map)

    def getRandom(self) -> int:
        assert len(self.map) > 0

        while True:
            idx = random.randint(0, len(self.array) - 1)

            if self.array[idx] not in self.map:
                continue

            return self.array[idx]
