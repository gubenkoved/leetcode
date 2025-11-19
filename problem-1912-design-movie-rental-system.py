from typing import List
import heapq


# TODO: extract SmarterHeap that will support marking elements removed
#  with elimination on traversal, also it will support topN1


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

        # NOTE: we can not efficiently drop from heap, so it will have stale
        # entries, consult with set inside shop_to_available_movies map!
        self.movie_to_availability_heap: dict[int, list] = {}
        self.shop_to_available_movies: dict[int, set] = {}

        # IMMUTABLE: (shop, movie) -> price map
        self.prices_map: dict[tuple[int, int], int] = {}

        for shop, movie, price in entries:
            if movie not in self.movie_to_availability_heap:
                self.movie_to_availability_heap[movie] = []

            if shop not in self.shop_to_available_movies:
                self.shop_to_available_movies[shop] = set()

            heap = self.movie_to_availability_heap[movie]
            heapq.heappush(heap, (price, shop))

            self.shop_to_available_movies[shop].add(movie)

            self.prices_map[(shop, movie)] = price

        # min heap of (price, shop, movie)
        # same: consult with rental set as this heap will contain stale entries
        self.rental_heap = []

        # tracks rented (shop, movie) pairs (always up to date)
        self.rental_set = set()

    # top5 the cheapest shops where given movie is available
    def search(self, movie: int) -> List[int]:
        heap = self.movie_to_availability_heap.get(movie, [])

        # pop top 5
        result = []
        popped = set()

        while heap and len(result) < 5:
            (price, shop) = heapq.heappop(heap)

            # filter out if movie is no longer available
            # (we do not need to put it back into heap)
            if movie not in self.shop_to_available_movies[shop]:
                continue

            # it is also possible we will have multiple records for the same
            # shop in the heap, we need to drop these too
            if (price, shop) in popped:
                continue

            popped.add((price, shop))
            result.append(shop)

        # put the top5 back!
        for item in popped:
            heapq.heappush(heap, item)

        return result

    def rent(self, shop: int, movie: int) -> None:
        self.shop_to_available_movies[shop].discard(movie)

        price = self.prices_map[(shop, movie)]
        heapq.heappush(self.rental_heap, (price, shop, movie))

        self.rental_set.add(
            (shop, movie)
        )

    def drop(self, shop: int, movie: int) -> None:
        heap = self.movie_to_availability_heap[movie]
        price = self.prices_map[(shop, movie)]
        heapq.heappush(heap, (price, shop))

        self.shop_to_available_movies[shop].add(movie)

        self.rental_set.discard((shop, movie))

    # top5 the cheapest rented
    def report(self) -> List[List[int]]:

        result = []
        popped = set()

        while self.rental_heap and len(result) < 5:
            price, shop, movie = heapq.heappop(self.rental_heap)

            # no longer rented, skip!
            if (shop, movie) not in self.rental_set:
                continue

            # drop duplicates
            if (price, shop, movie) in popped:
                continue

            popped.add((price, shop, movie))
            result.append([shop, movie])

        # put the things back!
        for element in popped:
            heapq.heappush(self.rental_heap, element)

        return result

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
