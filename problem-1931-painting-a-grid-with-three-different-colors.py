import functools

colors = [0, 1, 2]

# generates a list of "columns" where no two tiles have the same color
@functools.cache
def gen(m) -> list[tuple]:
    if m == 1:
        return [tuple([color]) for color in colors]
    else:
        result = []
        for prev in gen(m - 1):
            for color in colors:
                if color == prev[-1]:
                    continue
                result.append(prev + (color, ))
        return result


@functools.cache
def is_valid_match(col1: tuple, col2: tuple):
    for c1, c2 in zip(col1, col2):
        if c1 == c2:
            return False
    return True


@functools.cache
def f(m, n):
    counts_map = {}  # col -> count
    for col in range(n):
        if col == 0:
            counts_map = {col: 1 for col in gen(m)}
        else:
            # other columns can be computed just using the previous state
            new_counts_map = {}
            for prev_col, prev_count in counts_map.items():
                for col in gen(m):
                    if not is_valid_match(prev_col, col):
                        continue
                    if col not in new_counts_map:
                        new_counts_map[col] = 0
                    new_counts_map[col] += prev_count
            counts_map = new_counts_map
    return counts_map


class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        m = f(m, n)
        q = 10 ** 9 + 7
        return sum(m.values()) % q


if __name__ == '__main__':
    x = Solution()
    print(x.colorTheGrid(1, 1))
    print(x.colorTheGrid(1, 2))
    print(x.colorTheGrid(2, 2))
    print(x.colorTheGrid(5, 5))
    print(x.colorTheGrid(5, 1000))
