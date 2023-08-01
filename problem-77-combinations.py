from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        items = list(range(1, n + 1))

        result = []
        current = []

        # picks the next item starting at specific index w/o going to the left
        # part
        def pick(idx):
            leftover_count = k - len(current)

            # end case
            if leftover_count == 0:
                result.append(list(current))
                return

            # recursion step
            for next_idx in range(idx, n - leftover_count + 1):
                current.append(items[next_idx])
                pick(next_idx + 1)
                current.pop(-1)

        for start_idx in range(n - k + 1):
            current.append(items[start_idx])
            pick(start_idx + 1)
            current.pop(-1)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.combine(4, 2))
