class DisjointSet:
    def __init__(self):
        self.parent = {}

    def ensure(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def union(self, a, b):
        self.ensure(a)
        self.ensure(b)

        pa = self.find(a)
        pb = self.find(b)

        if pa < pb:
            self.parent[pb] = pa
        else:
            self.parent[pa] = pb

    def find(self, x):
        if x not in self.parent:
            return None

        ptr = x
        while self.parent[ptr] != ptr:
            ptr = self.parent[ptr]

        # shortcut the calculation for the next time
        self.parent[x] = ptr

        return ptr


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        ds = DisjointSet()
        for c1, c2 in zip(s1, s2):
            ds.union(c1, c2)
        result = []
        for c in baseStr:
            result.append(ds.find(c) or c)
        return ''.join(result)


if __name__ == '__main__':
    x = Solution()
    # print(x.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
    print(x.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))
