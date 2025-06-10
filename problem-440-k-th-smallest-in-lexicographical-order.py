import math

def digits_count(x):
    return 1 + math.floor(math.log10(x))

def first_k_digits(q: int, k: int):
    """
    Converts number q into another number that has exactly "k" digits.
    When number has more than requested amount of digits we divide it by 10
    until we have needed amount of digits. If we have less than requested
    then we just add a trailing 0.
    """
    q_digits = digits_count(q)
    if q_digits > k:
        for _ in range(q_digits - k):
            q //= 10
    elif q_digits == k:
        return q
    else:
        for _ in range(k - q_digits):
            q *= 10
    return q

def count_lexicographically_smaller_than(q: int, up_to: int) -> int:
    up_to += 1
    range_start = 1
    count = 0
    q_digits = digits_count(q)
    while True:
        r_digits = digits_count(range_start)
        q2 = first_k_digits(q, r_digits)

        if r_digits < q_digits:
            count += min(q2, up_to) - range_start + 1
        else:
            count += min(q2, up_to) - range_start

        # advance to the next range
        range_start *= 10
        if range_start > up_to:
            break
    return count

def c2(q, up_to):
    return count_lexicographically_smaller_than(q, up_to) + 1


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # we can find the digits of answer one by one
        ans = 1

        while True:
            c = c2(ans, n)

            while ans % 10 != 9 and c2(ans + 1, n) <= k:
                ans += 1
                c = c2(ans, n)

            if c == k:
                return ans

            # go to the next digit
            ans *= 10

            assert ans <= n

        return ans


# let's suppose the answer is A, we need to be able to check it
# in O(logn) and then binary search the result;

# note that number can be lexicographically smaller but arbitrary bigger,
# e.g. 1000 is lexicographically smaller than 2


def check():
    n = 10000
    nums = [int(x) for x in sorted(str(x) for x in range(1, n + 1))]
    for idx, x in enumerate(nums):
        assert count_lexicographically_smaller_than(x, n) == idx

    sol = Solution()
    nums2 = [sol.findKthNumber(n, k) for k in range(n + 1)]
    assert nums2 == nums


if __name__ == '__main__':
    # check()

    print([int(x) for x in sorted(str(x) for x in range(1, 10 + 1))])
    print([int(x) for x in sorted(str(x) for x in range(1, 100 + 1))])

    x = Solution()
    assert x.findKthNumber(100, 6) == 13
    assert x.findKthNumber(10, 1) == 1
    assert x.findKthNumber(10, 9) == 8
    assert x.findKthNumber(10, 10) == 9
