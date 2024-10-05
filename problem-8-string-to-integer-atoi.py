class Solution:
    def cleanup(self, s: str) -> str:
        s = s.strip()
        result = ''
        for idx in range(len(s)):
            is_digit = s[idx].isdigit()
            if idx == 0:
                is_sign = s[0] in ('-', '+')
                if not is_sign and not is_digit:
                    break
                result += s[0]
            else:  # non-first character
                if not is_digit:
                    break
                result += s[idx]
        return result

    def myAtoi(self, s: str) -> int:
        s = self.cleanup(s)

        if not s:
            return 0

        def convert(s):
            if not s:
                return 0
            v = ord(s[-1]) - ord('0')
            if len(s) == 1:
                return v
            return v + 10 * convert(s[:-1])

        if s[0] == '-':
            result = -convert(s[1:])
        elif s[0] == '+':
            result = convert(s[1:])
        else:
            result = convert(s)

        return min(max(result, -(2 ** 31)), 2 ** 31 - 1)


if __name__ == '__main__':
    x = Solution()
    print(x.myAtoi('.1'))
