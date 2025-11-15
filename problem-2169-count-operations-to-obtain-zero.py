class Solution:
    def countOperations(self, num1: int, num2: int) -> int:

        def f(x, y):
            if x == 0 or y == 0:
                return 0

            # ensure x >= y
            if y > x:
                return f(y, x)

            # basically Euclid GCD on steroids
            return x // y + f(x % y, y)

        return f(num1, num2)


if __name__ == '__main__':
    x = Solution()
    print(x.countOperations(2, 3), 3)
    print(x.countOperations(10, 10), 1)
