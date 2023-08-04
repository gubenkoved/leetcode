from typing import List
from functools import lru_cache


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        @lru_cache()
        def is_palindrome(s):
            n = len(s)
            for idx in range(n // 2):
                if s[idx] != s[n - idx - 1]:
                    return False
            return True

        current = []

        def fn_partition(s):
            if s == '':
                result.append(list(current))
                return

            for idx in range(1, len(s) + 1):
                left = s[:idx]

                if is_palindrome(left):
                    right = s[idx:]
                    current.append(left)
                    fn_partition(right)
                    current.pop(-1)

        fn_partition(s)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.partition("aab"))
