import functools


class Solution:
    def numDecodings(self, s: str) -> int:
        m = {
            str(x): chr(ord('A') + x)
            for x in range(1, 26 + 1)
        }

        n = len(s)

        @functools.lru_cache(None)
        def f(left):
            if left == n - 1:
                return 1 if s[left] in m else 0
            result = 0
            if s[left] in m:
                result = f(left + 1)
            if s[left:left+2] in m:
                if left + 2 == n:
                    result += 1
                else:
                    result += f(left + 2)
            return result

        return f(0)


if __name__ == '__main__':
    x = Solution()
    print(x.numDecodings('11106'))
    print(x.numDecodings('1111111'))
