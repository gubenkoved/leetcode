# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII.
# Instead, the number four is written as IV. Because the one is before
# the five we subtract it making four. The same principle applies to the
# number nine, which is written as IX. There are six instances where
# subtraction is used:
#
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        n = len(s)
        result = 0
        idx = 0
        while idx < n:
            cur = s[idx]
            next_ = None

            if idx < n - 1:
                next_ = s[idx + 1]

            if (cur == 'I' and next_ in ['V', 'X'] or
                    cur == 'X' and next_ in ['L', 'C'] or
                    cur == 'C' and next_ in ['D', 'M']):
                result += m[next_] - m[cur]
                idx += 1
            else:
                result += m[cur]

            idx += 1
        return result


if __name__ == '__main__':
    x = Solution()
    assert x.romanToInt('III') == 3
    assert x.romanToInt('LVIII') == 58
    assert x.romanToInt('MCMXCIV') == 1994
