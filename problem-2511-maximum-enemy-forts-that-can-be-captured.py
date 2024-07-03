from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        result = 0

        # to cover reverse direction transparently (not efficient by memory)
        forts.append(2)  # just a special marker
        forts.extend(reversed(forts))

        n = len(forts)

        # forward direction only
        ptr = 0
        while ptr < n:
            # start at your fort
            while ptr < n and forts[ptr] != 1:
                ptr += 1

            ptr += 1

            # count enemy forts that are terminated by empty slot
            enemy_count = 0

            while ptr < n and forts[ptr] == 0:
                ptr += 1
                enemy_count += 1

            if ptr < n and forts[ptr] == -1:
                result = max(result, enemy_count)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.captureForts([1, 0, 0, -1, 0, 0, 0, 0, 1]))
    # print(x.captureForts([0, 0, 1, -1]))
    print(x.captureForts([-1, -1, -1, -1, 1, -1, 0, 1, 1, -1, 1, -1]))
