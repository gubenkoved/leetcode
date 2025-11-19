from typing import List
import heapq


# for now it only supports unique values (no duplicates present in the heap each moment),
# but can be further enhanced via tracking removed with counts map
# better alternative -- tree set (which does not exist in Python) or SortedList from sortedcontainers
class SmarterHeap:
    def __init__(self):
        self.heap = []
        self.set = set()

    def push(self, value):
        assert value not in self.set
        heapq.heappush(self.heap, value)
        self.set.add(value)

    def delete(self, value):
        assert value in self.set
        self.set.discard(value)

    def top_k(self, k):
        result = []
        result_set = set()  # so that we can drop duplicates!

        while self.heap and len(result) < k:
            element = heapq.heappop(self.heap)

            if element not in self.set:
                continue

            if element in result_set:
                continue

            result_set.add(element)
            result.append(element)

        # put values back
        for element in result:
            heapq.heappush(self.heap, element)

        return result


class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        # for search implementation we need a TreeSet, or SortedList in case
        # of Python for each movie that will capture (price, shop) tuples
        # where given movies is still available for rent; ... or heap can be
        # also used here

        # for report where we need to always be able to answer "top 5 cheapest
        # rented" we can maintain a heap of (price, shop, movies) for all
        # rented copies, or may be a SortedList as well...

        self.n = n

        self.movie_to_availability_heap: dict[int, SmarterHeap] = {}

        # IMMUTABLE: (shop, movie) -> price map
        self.prices_map: dict[tuple[int, int], int] = {}

        for shop, movie, price in entries:
            if movie not in self.movie_to_availability_heap:
                self.movie_to_availability_heap[movie] = SmarterHeap()
            self.movie_to_availability_heap[movie].push((price, shop))
            self.prices_map[(shop, movie)] = price

        # min heap of (price, shop, movie)
        self.rental_heap = SmarterHeap()

    # top5 the cheapest shops where given movie is available
    def search(self, movie: int) -> List[int]:
        if movie not in self.movie_to_availability_heap:
            return []
        return [shop for (price, shop) in self.movie_to_availability_heap[movie].top_k(5)]

    def rent(self, shop: int, movie: int) -> None:
        price = self.prices_map[(shop, movie)]
        self.movie_to_availability_heap[movie].delete((price, shop))
        self.rental_heap.push((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.prices_map[(shop, movie)]
        self.movie_to_availability_heap[movie].push((price, shop))
        self.rental_heap.delete((price, shop, movie))

    # top5 the cheapest rented
    def report(self) -> List[List[int]]:
        return [[shop, movie] for (price, shop, movie) in self.rental_heap.top_k(5)]

# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()

if __name__ == '__main__':
    # x = MovieRentingSystem(
    #     3,
    #     [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]],
    # )
    #
    # print(x.search(1))
    # print(x.rent(0, 1))
    # print(x.rent(1, 2))
    # print(x.report())
    # print(x.drop(1, 2))
    # print(x.search(2))

    # ["MovieRentingSystem", "search", "search", "rent", "search", "search", "report", "search", "drop"]
    x = MovieRentingSystem(
        10,
        [[0,418,3],[9,5144,46],[2,8986,29],[6,1446,28],[3,8215,97],[7,9105,34],[6,9105,30],[5,1722,94],[9,528,40],[3,850,77],[3,7069,40],[8,1997,42],[0,8215,28],[7,4050,80],[4,7100,97],[4,9686,32],[4,2566,93],[2,8320,12],[2,5495,56]])
    # [[7837],[5495],[4,7100],[9105],[1446],[],[9869],[4,7100]]

    print(x.search(7837))
    print(x.search(5495))
    print(x.rent(4, 7100))
    print(x.search(9105))
    print(x.search(1446))
    print(x.report())
    print(x.search(9869))
    print(x.drop(4, 7100))
