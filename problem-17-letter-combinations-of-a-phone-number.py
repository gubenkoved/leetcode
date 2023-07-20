from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
         '2': ['a', 'b', 'c'],
         '3': ['d', 'e', 'f'],
         '4': ['g', 'h', 'i'],
         '5': ['j', 'k', 'l'],
         '6': ['m', 'n', 'o'],
         '7': ['p', 'q', 'r', 's'],
         '8': ['t', 'u', 'v'],
         '9': ['w', 'x', 'y', 'z'],
        }

        if len(digits) == 0:
            return []

        def pick(s):
            if len(s) == 1:
                return m[s[0]]

            cur_result = []
            inner = pick(s[1:])
            for c in m[s[0]]:
                for inner_cur in inner:
                    cur_result.append(c + inner_cur)
            return cur_result

        return pick(digits)


if __name__ == '__main__':
    x = Solution()
    print(x.letterCombinations('23'))
    print(x.letterCombinations(''))
