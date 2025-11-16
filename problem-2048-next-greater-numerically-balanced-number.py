class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # using 1, 2, 3, 4 we already can get numbers more than we need
        # e.g. 1223334444, so we can just generate all the numbers that are
        # composed of various combinations;
        # however given the limits it should be possible with a simple bruteforce
        # too...

        def is_beautiful(x):
            counts = [0] * 10

            while x != 0:
                d = x % 10
                x = x // 10
                counts[d] += 1

            for idx in range(10):
                if counts[idx] != 0 and idx != counts[idx]:
                    return False

            return True

        while True:
            n += 1
            if is_beautiful(n):
                return n


if __name__ == '__main__':
    x = Solution()
    print(x.nextBeautifulNumber(1), 22)
