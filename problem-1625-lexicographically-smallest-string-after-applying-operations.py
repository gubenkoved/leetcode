class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        stack = [s]

        def add(s):
            chars = list(s)
            for idx in range(1, len(s), 2):
                chars[idx] = str((int(chars[idx]) + a) % 10)
            return ''.join(chars)

        def rot(s):
            return s[b:] + s[:b]

        while stack:
            s = stack.pop(-1)
            if s in visited:
                continue
            visited.add(s)
            for s2 in [add(s), rot(s)]:
                if s2 not in visited:
                    stack.append(s2)

        return min(visited)


if __name__ == '__main__':
    x = Solution()
    print(x.findLexSmallestString('5525', 9, 2))
