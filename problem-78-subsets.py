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


# TODO: solution that tracks "available" elements on each recursive call to solve
#  uniqueness issue more efficiently


print([list(x) for x in set(subsets([1, 2, 3]))])
