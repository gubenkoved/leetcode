class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = left

        for bit in range(32):
            if left == 0 and right == 0:
                break

            zero_out = right - left != 0

            if zero_out:
                result &= ~(2 ** bit)

            left = left // 2
            right = right // 2

        return result

if __name__ == '__main__':
    x = Solution()
    print(x.rangeBitwiseAnd(5, 7))
    print(x.rangeBitwiseAnd(2, 2))
    print(x.rangeBitwiseAnd(4, 5))
