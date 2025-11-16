class Solution:
    def numSub(self, s: str) -> int:
        result = 0
        ones_counter = 0
        for c in s + '0':
            if c == '1':
                ones_counter += 1

            else:
                # for string of len N we have
                # N substrings of len 1
                # N - 1 substrings of len 2
                # ...
                # 1 substring of len N
                # total is 1 + 2 + .. + N which is arithmetic
                # progression of N values with average (N + 1) / 2
                result += (ones_counter * (ones_counter + 1)) // 2
                ones_counter = 0
        return result % (10 ** 9 + 7)
