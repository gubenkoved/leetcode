def generate():
    for d in range(1, 10):
        yield d

    l = 1
    while True:
        for d in range(10 ** (l - 1), 10 ** l):
            d_str = str(d)
            d_rev = d_str[::-1]
            yield int(d_str + d_rev)

        for d in range(10 ** (l - 1), 10 ** l):
            d_str = str(d)
            d_rev = d_str[::-1]
            for d2 in range(10):
                yield int(d_str + str(d2) + d_rev)
        l += 1


def to_k_base(x: int, k: int) -> str:
    result = []
    while x != 0:
        rem = x % k
        result.append(str(rem))
        x //= k
    return ''.join(reversed(result))


def is_palindrome(x: str) -> bool:
    return x == x[::-1]


class Solution:
    def kMirror(self, k: int, n: int) -> int:
        nums = []
        generator = generate()
        while len(nums) < n:
            x = next(generator)
            x_k = to_k_base(x, k)
            if is_palindrome(x_k):
                nums.append(x)
        return sum(nums)


if __name__ == '__main__':
    x = Solution()
    print(x.kMirror(2, 5))
    print(x.kMirror(3, 7))
    print(x.kMirror(4, 5))
