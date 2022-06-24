# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.


def is_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop(-1)
            else:
                return -2  # not fixable by continuation
    if stack:
        return -1  # fixable by continuation
    return 0


class Solution:
    # O(n^2) different ranges to try with O(n) check complexity
    # overall gives O(n^3) which is pretty shitty
    def longestValidParentheses_naive(self, s: str) -> int:
        result = 0
        for start_idx in range(0, len(s) - 1):
            for end_idx in range(start_idx + 1, len(s)):
                code = is_valid(s[start_idx:end_idx + 1])

                if code == 0:
                    if end_idx - start_idx + 1 > result:
                        result = end_idx - start_idx + 1
                elif code == -2:
                    break  # no need to try to continue expansion
        return result

    def longestValidParentheses(self, s: str) -> int:
        return self.longestValidParentheses_naive(s)


if __name__ == '__main__':
    x = Solution()
    # print(x.longestValidParentheses(')()())'))
