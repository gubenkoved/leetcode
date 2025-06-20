class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        move = {
            'N': (+1, 0),
            'S': (-1, 0),
            'E': (0, -1),
            'W': (0, +1),
        }

        counts = {c: 0 for c in 'NSEW'}

        d = 0
        x, y = 0, 0
        for c in s:
            dx, dy = move[c]
            x, y = x + dx, y + dy
            cd = abs(x) + abs(y)
            counts[c] += 1

            # how much I can replace at this given step?
            if x >= 0:
                repl_count = min(k, counts['S'])
            else:
                repl_count = min(k, counts['N'])

            if y >= 0:
                repl_count += min(k - repl_count, counts['E'])
            else:
                repl_count += min(k - repl_count, counts['W'])

            # 2x because when I replace I char with the opposite one I negate
            # its effect and gain same effect in other direction
            d = max(d, cd + 2 * repl_count)

        return d


if __name__ == '__main__':
    x = Solution()
    print(x.maxDistance("NWSE", k = 1))
