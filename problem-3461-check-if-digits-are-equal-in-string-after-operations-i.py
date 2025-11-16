def step(digits):
    next_digits = []
    for idx in range(len(digits) - 1):
        next_digits.append((digits[idx] + digits[idx + 1]) % 10)
    return next_digits


class Solution:
    def hasSameDigits(self, s: str) -> bool:
        def calc(digits):
            if len(digits) == 2:
                return digits[0] == digits[1]
            return calc(step(digits))
        return calc([int(x) for x in s])

if __name__ == '__main__':
    x = Solution()
    print(x.hasSameDigits('323'), True)
