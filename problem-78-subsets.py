# slow solution, but it worked...
def subsets(a, k=None):
    k = len(a) if k is None else k

    if k == 1:
        yield frozenset([])
        for el in a:
            yield frozenset([el])
    else:
        for combination in subsets(a, k - 1):
            yield combination
            if len(combination) != k - 1:
                continue
            for el in a[k-1:]:
                if el not in combination:
                    yield frozenset(list(combination) + [el])


def combinations_no_repetitions(items, k):
    n = len(items)
    result = []
    cur = []

    def gen(last_idx):
        l = k - len(cur)
        for idx in range(last_idx+1, n-l+1):
            cur.append(items[idx])

            if len(cur) == k:
                result.append(list(cur))
            else:
                gen(idx)

            cur.pop(-1)

    gen(-1)
    return result


def combinations_no_repetitions_v2(items, k):
    n = len(items)
    result = []
    cur = [None] * k
    cur_ptr = 0

    def gen(last_idx):
        nonlocal cur_ptr
        l = k - cur_ptr
        for idx in range(last_idx+1, n-l+1):
            cur[cur_ptr] = items[idx]
            cur_ptr += 1

            if cur_ptr == k:
                result.append(list(cur))
            else:
                gen(idx)

            cur_ptr -= 1

    gen(-1)
    return result


def powerset(items):
    result = [[]]
    for k in range(1, len(items) + 1):
        # result.extend(combinations_no_repetitions(items, k))
        result.extend(combinations_no_repetitions_v2(items, k))
    return result


# print([list(x) for x in set(subsets([1, 2, 3]))])
# print(combinations_no_repetitions([1, 2, 3, 4], k=2))
# print(powerset([1, 2, 3]))
print(powerset([1, 2, 3, 4]))