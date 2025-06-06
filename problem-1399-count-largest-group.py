class Solution:
    def countLargestGroup(self, n: int) -> int:
        counter = {}
        for idx in range(1, n + 1):
            group_key = sum(int(d) for d in str(idx))
            if group_key not in counter:
                counter[group_key] = 0
            counter[group_key] += 1
        max_size = max(counter.values())
        return sum(1 for gv in counter.values() if gv == max_size)
