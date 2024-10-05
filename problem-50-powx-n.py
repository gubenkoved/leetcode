class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)

        result = 1
        rolling = x
        while n != 0:
            if n % 2 == 1:
                result *= rolling
            n = n // 2
            rolling *= rolling
        return result
