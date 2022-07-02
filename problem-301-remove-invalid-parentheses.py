from typing import List


def is_valid(s: str):
    stack = []

    for c in s:
        if c.isalpha():
            pass
        elif c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                return False

    return not stack


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        results = set()
        checked = set()
        max_len = 0

        def search(x: str):
            nonlocal max_len

            if x in checked:
                return

            checked.add(x)

            # print(f'{x}')

            if is_valid(x):
                if not results:
                    results.add(x)
                    max_len = len(x)
                else:
                    if len(x) >= max_len:
                        results.add(x)
                    max_len = max(max_len, len(x))

            if max_len is not None and len(s) <= max_len:
                return

            for idx in range(len(x)):
                search(x[:idx] + x[idx+1:])

        search(s)

        # print(f'max_len: {max_len}')

        return [x for x in results if len(x) == max_len]


if __name__ == '__main__':
    x = Solution()
    # print(x.removeInvalidParentheses('(a)())()'))
    # print(x.removeInvalidParentheses('()())()'))
    print(x.removeInvalidParentheses('())))()v(k'))
    # print(x.removeInvalidParentheses('()('))
    # print(is_valid('()'))
