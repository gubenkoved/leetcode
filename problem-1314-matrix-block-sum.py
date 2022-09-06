# return matrix m[r][c] where m[r][c] is a sum of source[i][j] where:
#  r - k <= i <= r + k
#  c - k <= j <= c + k

class Solution:
    def matrixBlockSum(self, matrix, k):
        # compute partial sum where sum[i][j] will be the sum of all the cells
        # from the cell [0][0] till [i][j] including
        rows, cols = len(matrix), len(matrix[0])
        sums = [[None] * cols for _ in range(rows)]

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def val_at(mat, r, c, default=0):
            if not is_valid(r, c):
                return default
            return mat[r][c]

        for i in range(rows):
            for j in range(cols):
                sums[i][j] = (
                    matrix[i][j] +
                    val_at(sums, i - 1, j) +
                    val_at(sums, i, j - 1) -
                    val_at(sums, i - 1, j - 1)
                )

        # compose an answer
        answer = [[None] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                r_lo, r_hi = (i - k, i + k)
                c_lo, c_hi = (j - k, j + k)

                # limit to good coordinates
                r_lo, r_hi = (max(0, r_lo), min(rows - 1, r_hi))
                c_lo, c_hi = (max(0, c_lo), min(cols - 1, c_hi))

                answer[i][j] = (
                    sums[r_hi][c_hi] -
                    val_at(sums, r_lo - 1, c_hi, 0) -
                    val_at(sums, r_hi, c_lo - 1) +
                    val_at(sums, r_lo - 1, c_lo - 1)
                )

        return answer


if __name__ == '__main__':
    x = Solution()
    print(x.matrixBlockSum(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], k=1
    ))

    print(x.matrixBlockSum(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]], k=2
    ))
