import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n1 + n2 != n3:
            return False

        @functools.lru_cache(maxsize=None)
        def check(idx1, idx2, idx3):
            if idx1 == n1:
                return s2[idx2:] == s3[idx3:]

            if idx2 == n2:
                return s1[idx1:] == s3[idx3:]

            wanted = s3[idx3]

            if idx1 != n1 and s1[idx1] == wanted:
                if check(idx1 + 1, idx2, idx3 + 1):
                    return True

            if idx2 != n2 and s2[idx2] == wanted:
                if check(idx1, idx2 + 1, idx3 + 1):
                    return True

            return False

        return check(0, 0, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(x.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
