# O(n) time, O(n) space
def rotate_array_simple_inplace(a, k):
    b = [None] * len(a)
    n = len(a)
    for idx in range(n):
        b[idx] = a[(idx - k) % n]
    for idx in range(n):
        a[idx] = b[idx]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


# O(n) time, O(1) space
def rotate_array_smart(a, k):
    n = len(a)
    k = k % n

    if k == 0:
        return

    cycle_len = lcm(n, k) // k
    assert cycle_len > 0
    passes = n // cycle_len
    for idx in range(passes):
        popped = a[idx]
        move_target = idx
        for step in range(cycle_len):
            move_target = (move_target + k + n) % n
            popped_next = a[move_target]
            a[move_target] = popped
            popped = popped_next


if __name__ == '__main__':
    # a = [1, 2, 3, 4, 5, 6, 7]
    a = [1, 2, 3, 4]

    # rotate_array_simple_inplace(a, 2)
    # rotate_array_smart(a, 6)
    rotate_array_smart(a, 2)

    print(a)
