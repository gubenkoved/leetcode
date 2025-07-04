from typing import List


class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        # k, and char idx are 1-based (NOT ZERO)

        def f(idx, op_idx, char_offset):
            if op_idx == -1:
                return chr(ord('a') + (char_offset % 26))

            pl = 2 ** op_idx

            if pl >= idx:
                return f(idx, op_idx - 1, char_offset)

            if operations[op_idx] == 1:
                char_offset += 1

            return f(idx - pl, op_idx - 1, char_offset)

        n = len(operations)
        return f(k, n - 1, 0)


if __name__ == '__main__':
    x = Solution()
    print(x.kthCharacter(k = 5, operations = [0,0,0]))
    # a aa aabb aabbaabb aabbaabbbbccbbcc
    print(x.kthCharacter(k = 10, operations = [0,1,0,1]))
