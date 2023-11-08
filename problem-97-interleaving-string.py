import functools


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        @functools.lru_cache(maxsize=None)
        def check(s1, s2, s3):
            if len(s1) + len(s2) != len(s3):
                return False

            if not s1:
                return s2 == s3

            if not s2:
                return s1 == s3

            wanted = s3[0]

            if s1 and s1[0] == wanted:
                if check(s1[1:], s2, s3[1:]):
                    return True

            if s2 and s2[0] == wanted:
                if check(s1, s2[1:], s3[1:]):
                    return True

            return False

        return check(s1, s2, s3)


if __name__ == '__main__':
    x = Solution()
    print(x.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(x.isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
