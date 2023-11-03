class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]

        row = 0
        d = 1  # going down

        for c in s:
            rows[row].append(c)

            row += d

            # reverse direction
            if row == 0 or row == numRows - 1:
                d *= -1

        return ''.join(''.join(row) for row in rows)


if __name__ == '__main__':
    x = Solution()
    assert x.convert('PAYPALISHIRING', numRows=3) == 'PAHNAPLSIIGYIR'
    assert x.convert('PAYPALISHIRING', numRows=4) == 'PINALSIGYAHRPI'
    assert x.convert('A', numRows=1) == 'A'
