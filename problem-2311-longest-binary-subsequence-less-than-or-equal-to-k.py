class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # start from the right side and extend the resulting sequence while
        # it still less than k greedily
        idx = len(s)
        r_num = 0
        bit_idx = 0

        while idx > 0:
            # see if we can move idx to the left w/o crossing the threshold
            b = 1 if s[idx - 1] == '1' else 0
            r_num_next = r_num + (b << bit_idx)

            if r_num_next > k:
                break

            r_num = r_num_next
            bit_idx += 1
            idx -= 1

        # and then add all the zeros from the left side
        result = len(s) - idx

        idx -= 1

        while idx >= 0:
            result += 1 if s[idx] == '0' else 0
            idx -= 1

        return result

if __name__ == '__main__':
    x = Solution()
    print(x.longestSubsequence("1001010", k = 5))
    print(x.longestSubsequence("00101001", k = 1))
    print(x.longestSubsequence("1001111101", k = 999999999))
