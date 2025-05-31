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
    # base case
    if n == 1:
        return {col: 1 for col in gen(m)}
    result = {}  # col -> counter
    prev_result = f(m, n - 1)
    for prev_col, prev_count in prev_result.items():
        for col in gen(m):
            if not is_valid_match(prev_col, col):
                continue
            if col not in result:
                result[col] = 0
            result[col] += prev_count
    return result


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
