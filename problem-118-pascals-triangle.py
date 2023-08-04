from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for row_num in range(1, numRows):
            row = []
            for idx in range(row_num + 1):
                if idx == 0 or idx == row_num:
                    row.append(1)
                else:
                    row.append(result[row_num - 1][idx - 1] + result[row_num - 1][idx])
            result.append(row)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.generate(5))
