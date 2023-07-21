from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        elif n == 1:
            return ['()']
        else:
            prev = self.generateParenthesis(n - 1)
            prev_size = 2 * (n - 1)
            result = set()
            # try to insert '(' at any location:
            for left_idx in range(0, prev_size + 1):
                for right_idx in range(left_idx + 1, prev_size + 2):
                    for prev_str in prev:
                        new_item = prev_str[:left_idx] + '(' + prev_str[left_idx:right_idx] + ')' + prev_str[right_idx:]
                        result.add(new_item)
            return list(result)


if __name__ == '__main__':
    x = Solution()
    print(x.generateParenthesis(1))
    print(x.generateParenthesis(2))
    print(x.generateParenthesis(3))
    print(x.generateParenthesis(8))