from functools import lru_cache


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        @lru_cache(maxsize=None)
        def total(row, glass) -> float:
            assert glass <= row

            if row == 0:
                return poured

            result = 0.0

            if glass > 0:
                result += max(0.0, (total(row - 1, glass - 1) - 1) / 2.0)

            if glass != row:
                result += max(0.0, (total(row - 1, glass) - 1) / 2.0)

            return result

        return min(1, total(query_row, query_glass))


if __name__ == '__main__':
    x = Solution()
    # print(x.champagneTower(poured=1, query_row=1, query_glass=1))
    print(x.champagneTower(poured=2, query_row=1, query_glass=1))
    # print(x.champagneTower(poured=100000009, query_row=33, query_glass=17))
    # print(x.champagneTower(poured=25, query_row=6, query_glass=1))
    # print(x.champagneTower(poured=1, query_row=0, query_glass=0))
