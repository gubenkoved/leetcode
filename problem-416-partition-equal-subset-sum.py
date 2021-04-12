from typing import List


# that's interesting -- when I came with this "solution" I was almost 100%
# sure it's not going to be functionally correct, and even now after getting
# "accepted" by LeetCode I'm still not sure why it's working...
class Solution:
    def __init__(self):
        self.seen = set()

    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False

        return self.canPartitionImpl(nums, set(), target // 2)

    def canPartitionImpl(self, nums, taken, target: int) -> bool:
        if target < 0:
            return False

        if target in self.seen:
            return False

        for idx, num in enumerate(nums):
            if idx in taken:
                continue

            if num == target:
                return True

            taken.add(idx)

            if self.canPartitionImpl(nums, taken, target - num):
                return True

            taken.remove(idx)

        self.seen.add(target)

        return False


s = Solution()
assert s.canPartition([15, 5, 20, 10, 35, 15, 10])
assert not s.canPartition([4,4,4,4,4,4,4,4,8,8,8,8,8,8,8,8,12,12,12,12,12,12,12,12,16,16,16,16,16,16,16,16,20,20,20,20,20,20,20,20,24,24,24,24,24,24,24,24,28,28,28,28,28,28,28,28,32,32,32,32,32,32,32,32,36,36,36,36,36,36,36,36,40,40,40,40,40,40,40,40,44,44,44,44,44,44,44,44,48,48,48,48,48,48,48,48,52,52,52,52,52,52,52,52,56,56,56,56,56,56,56,56,60,60,60,60,60,60,60,60,64,64,64,64,64,64,64,64,68,68,68,68,68,68,68,68,72,72,72,72,72,72,72,72,76,76,76,76,76,76,76,76,80,80,80,80,80,80,80,80,84,84,84,84,84,84,84,84,88,88,88,88,88,88,88,88,92,92,92,92,92,92,92,92,96,96,96,96,96,96,96,96,97,99])
