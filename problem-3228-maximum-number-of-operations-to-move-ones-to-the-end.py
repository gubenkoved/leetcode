class Solution:
    def maxOperations(self, s: str) -> int:
        # looks like for each "1" we need to calculate amount of
        # ranges of consecutive zeros to the right
        result = 0
        zero_ranges_count = 0
        for idx in range(len(s) - 1, -1, -1):
            if s[idx] == '0':
                if idx == len(s) - 1 or s[idx + 1] == '1':
                    zero_ranges_count += 1
            else:
                result += zero_ranges_count
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxOperations('1001101'), 4)

    print(x.maxOperations('10101'), 3)

    # 10101
    # 01101
    # 01011
    # 00111

    print(x.maxOperations('1010101'), 6)

    # 1010101
    # 0110101
    # 0101101
    # 0011101
    # 0011011
    # 0010111
    # 0001111

    print(x.maxOperations('1110'), 3)

    # 1110
    # 1101
    # 1011
    # 0111
