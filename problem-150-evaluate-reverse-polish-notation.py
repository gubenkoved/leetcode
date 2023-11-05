from typing import List
import math


def round_towards_zero(f):
    if f >= 0:
        return math.floor(f)
    else:
        return -1 * math.floor(-f)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b = stack.pop(-1)
                a = stack.pop(-1)

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(round_towards_zero(a / b))
            else:
                stack.append(int(token))

        assert len(stack) == 1

        return stack[0]


if __name__ == '__main__':
    x = Solution()
    # assert x.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert x.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
