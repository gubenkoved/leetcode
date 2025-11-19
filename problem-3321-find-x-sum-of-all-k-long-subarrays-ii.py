from typing import List
from sortedcontainers import SortedList
from collections import defaultdict


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        # sorted list of (freq, num) inside the window
        # separately tracking values for top x vs other so that we can
        # easier calculate the sum over the top x
        win_other = SortedList()
        win_top_x = SortedList()

        # frequency of the given num in the window
        freq_map = defaultdict(lambda: 0)

        # populate first window
        for num in nums[:k]:
            freq_map[num] += 1

        for num, freq in freq_map.items():
            win_other.add((freq, num))

        while len(win_top_x) < x and win_other:
            freq, num = win_other.pop(-1)
            win_top_x.add((freq, num))

        x_sum = sum(freq * num for (freq, num) in win_top_x)

        result = [x_sum]

        # drops element from window; when dropped from "top x" part, updates
        # x sum as well
        def evict(elem_freq, elem):
            nonlocal x_sum
            if (elem_freq, elem) in win_top_x:
                win_top_x.discard((elem_freq, elem))
                x_sum -= elem_freq * elem
            elif (elem_freq, elem) in win_other:
                win_other.discard((elem_freq, elem))

        # now go over the whole array using sliding window with only O(logn)
        # worth of work per each item!
        for offset in range(len(nums) - k):
            out_elem = nums[offset]
            ins_elem = nums[offset + k]

            if out_elem != ins_elem:
                out_elem_freq = freq_map[out_elem]
                ins_elem_freq = freq_map[ins_elem]

                # evict out_elem from top x part if it was there,
                # as it might be replaced by another one (or re-added back)
                evict(out_elem_freq, out_elem)

                # same for ins_elem
                evict(ins_elem_freq, ins_elem)

                freq_map[out_elem] -= 1
                freq_map[ins_elem] += 1

                # put both into the "other" part first
                win_other.add((out_elem_freq - 1, out_elem))
                win_other.add((ins_elem_freq + 1, ins_elem))

                # also we might have outgrew the last in topx, so let's evict it as well
                if win_top_x:
                    elem_freq, elem = win_top_x[0]
                    evict(elem_freq, elem)
                    win_other.add((elem_freq, elem))

                # update "top x" part
                while len(win_top_x) < x and win_other:
                    elem_freq, elem = win_other.pop(-1)
                    win_top_x.add((elem_freq, elem))
                    x_sum += elem_freq * elem

            result.append(x_sum)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.findXSum([1,1,2,2,3,4,2,3], k = 6, x = 2), [6,10,12])
    # print(x.findXSum([3,8,7,8,7,5], k = 2, x = 2), [11,15,15,15,12])
    # print(x.findXSum([5, 1], k=1, x=1), [5, 1])
    # print(x.findXSum([7,10,8,9,10], 5, 5))
    print(x.findXSum([3,3,6,1,3,3,4,6,4,2,4], 3, 2), [12,9,9,7,10,10,14,10,10])