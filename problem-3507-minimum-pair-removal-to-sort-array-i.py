from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        tmp = list(nums)

        def is_sorted():
            for idx in range(1, len(tmp)):
                if tmp[idx] < tmp[idx - 1]:
                    return False
            return True

        operations = 0

        while not is_sorted():
            if len(tmp) == 2:
                operations += 1
                break

            operations += 1

            # pick the pair with the smallest sum
            smallest_sum_idx = 0
            smallest_pair_sum = tmp[0] + tmp[1]
            for idx in range(0, len(tmp) - 1):
                pair_sum = tmp[idx] + tmp[idx + 1]
                if pair_sum < smallest_pair_sum:
                    smallest_pair_sum = pair_sum
                    smallest_sum_idx = idx

            # replace with the sum!
            tmp.pop(smallest_sum_idx)
            tmp.pop(smallest_sum_idx)
            tmp.insert(smallest_sum_idx, smallest_pair_sum)

        return operations


if __name__ == '__main__':
    x = Solution()
    print(x.minimumPairRemoval([10, 1]), 1)
    print(x.minimumPairRemoval([5,2,3,1]), 2)
