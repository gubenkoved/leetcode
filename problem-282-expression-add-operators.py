# Given a string num that contains only digits and an integer target,
# return all possibilities to insert the binary operators '+', '-', and/or '*'
# between the digits of num so that the resultant expression evaluates to the target value.
#
# Note that operands in the returned expressions should not contain leading zeros.

from typing import List
from functools import lru_cache


class Solution:
    # if n is len of the number string, then there are n-1 places to stick
    # any of 4 operators or an empty space
    # n is up to 10 characters, so there are up to 5^9 or about 2M strings to handle
    def addOperators_bruteforce(self, num: str, target: int) -> List[str]:
        n = len(num)
        found = set()
        operators = [''] * n

        def combine():
            chars = []
            for idx, d in enumerate(num):
                chars.append(d)
                chars.append(operators[idx])
            return ''.join(chars)

        def find(idx=0):
            if idx < n - 1:
                for operator in ['+', '-', '*', '/', '']:
                    operators[idx] = operator
                    find(idx + 1)
            else:
                expr = combine()
                try:
                    if eval(expr) == target:
                        found.add(expr)
                except ZeroDivisionError:
                    pass

        find()

        return list(found)

    # idea is good, but it does not account for the "*" and "/" operators order properly
    def addOperators_wa(self, num: str, target: int) -> List[str]:
        # returns iterable with all possible ways to reach the given target
        def find(s, t):
            ways = []

            if int(s) == t:
                ways.append(s)

            for insert_at in range(1, len(s)):
                # left number
                left = s[:insert_at]
                left_num = int(left)
                right = s[insert_at:]

                for way in find(right, t - left_num):
                    ways.append(left + '+' + way)

                for way in find(right, t + left_num):
                    ways.append(left + '-' + way)

                # FIXME: this does not handle order of operations properly for "*" and "/"
                for way in find(right, t / left_num):
                    ways.append(left + '*' + way)

                for way in find(right, left_num / t):
                    ways.append(left + '/' + way)

            return ways

        return find(num, target)

    def addOperators(self, num: str, target: int) -> List[str]:
        found = set()

        def find(s: str, idx: int, current_result: int, last_term: int, prev_operator: str):
            # idx points to the first char which is "mutable" (all to the left of it is not)
            if idx >= len(s):
                if current_result == target:
                    found.add(s)
                return

            for op_idx in range(idx + 1, len(s) + 1):
                operand = s[idx:op_idx]

                if len(operand) > 1 and operand[0] == '0':
                    continue

                operand_num = int(operand)
                left = s[:op_idx]
                right = s[op_idx:]

                new_result = current_result
                new_last_term = 0
                if prev_operator == '+':
                    new_last_term = operand_num
                    new_result += operand_num
                elif prev_operator == '-':
                    new_last_term = -operand_num
                    new_result -= operand_num
                elif prev_operator == '*':
                    new_result -= last_term
                    new_result += last_term * operand_num
                    new_last_term = last_term * operand_num

                if right:
                    find(left + '+' + right, op_idx + 1, new_result, new_last_term, '+')
                    find(left + '-' + right, op_idx + 1, new_result, new_last_term, '-')
                    find(left + '*' + right, op_idx + 1, new_result, new_last_term, '*')
                else:  # end case, last operator
                    find(left, op_idx, new_result, operand_num, prev_operator)

        find(num, 0, 0, 0, '+')

        return list(found)


if __name__ == '__main__':
    x = Solution()
    print(x.addOperators("123", 6))
    print(x.addOperators("232", 8))
    print(x.addOperators("105", 5))
    print(x.addOperators("3456237490", 9191))  # no answer
