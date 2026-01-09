import collections


class Solution:
    def numOfWays(self, n: int) -> int:
        alphabet = ['R', 'Y', 'B']

        def gen(k: int, prev: str) -> list[str]:
            result = []
            for x in alphabet:
                if x == prev:
                    continue
                if k == 1:
                    result.append(x)
                else:
                    for inner in gen(k - 1, x):
                        result.append(x + inner)
            return result

        # gen all triples
        all_possible = gen(3, '')
        M = 10 ** 9 + 7

        def compatible(prev, cur):
            for idx in range(len(prev)):
                if prev[idx] == cur[idx]:
                    return False
            return True

        # target -> list of compatible targets
        compatible_targets = collections.defaultdict(list)

        for x in all_possible:
            for y in all_possible:
                if not compatible(x, y):
                    continue
                compatible_targets[x].append(y)

        counts = {}

        for x in all_possible:
            counts[x] = 1

        for _ in range(n - 1):
            next_counts = collections.defaultdict(int)
            for x in all_possible:
                for y in compatible_targets[x]:
                    next_counts[x] += counts[y]
                    next_counts[x] = next_counts[x] % M
            counts = next_counts

        return sum(counts.values()) % M

if __name__ == "__main__":
    x = Solution()
    print(x.numOfWays(1), 12)
    print(x.numOfWays(2), '??')
    print(x.numOfWays(5000), 30228214)
