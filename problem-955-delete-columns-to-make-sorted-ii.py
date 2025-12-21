from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        k = len(strs[0])
        dropped_cols = set()

        # returns columns to be deleted for items in range [i, j]
        # considering chars at "col" onwards
        def f(i, j, col):
            # if there is wrong ordering in this column -> it has to be
            # dropped;
            # if there is no unordering, and no groups that have same char
            # at position -> exit with 0 as we already have a good order
            # otherwise for all the groups where char is the same at given
            # position we need to recursively check next char

            # single row is always "ordered"
            if j - i <= 0:
                return

            # out of string
            if col == k:
                return

            # if this column was already dropped -> check the next one
            if col in dropped_cols:
                f(i, j, col + 1)
                return

            out_of_order = False

            for row in range(i+1, j + 1):
                if strs[row][col] < strs[row-1][col]:
                    out_of_order = True
                    break

            # we have to drop this column
            if out_of_order:
                dropped_cols.add(col)
                f(i, j, col + 1)
                return

            # recursion step for cases with same values
            group_start = i
            for row in range(i, j + 1):
                if strs[row][col] != strs[group_start][col]:
                    f(group_start, row - 1, col + 1)
                    group_start = row

            # last group
            f(group_start, j, col + 1)

        # ugly processing for the case that after deleting in one "branch"
        # we might have messed up the order for another "branch"
        while True:
            dropped_before = len(dropped_cols)
            f(0, n-1, 0)
            if len(dropped_cols) == dropped_before:
                break

        return len(dropped_cols)


if __name__ == '__main__':
    x = Solution()
    # print(x.minDeletionSize(["ca","bb","ac"]), 1)
    # print(x.minDeletionSize(["xga","xfb","yfa"]), 1)
    # print(x.minDeletionSize(["zyx","wvu","tsr"]), 3)
    # print(x.minDeletionSize(["abx","agz","bgc","bfc"]), 1)
    print(x.minDeletionSize(["vdy","vei","zvc","zld"]), 2)
