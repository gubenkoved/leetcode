class Solution:
    def partitionString(self, s: str) -> int:
        tracker = set()
        result = 0
        for c in s:
            if c not in tracker:
                tracker.add(c)
            else:
                tracker = set(c)
                result += 1
        return result + 1
