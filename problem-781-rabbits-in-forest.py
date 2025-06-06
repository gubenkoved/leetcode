import math
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        c = {}
        for ans in answers:
            ans2 = ans + 1
            if ans2 not in c:
                c[ans2] = 0
            c[ans2] += 1
        result = 0

        # greedily process the groups
        while c:
            key, count = c.popitem()

            if key == count:
                # consider we polled whole group
                result += count
            elif key > count:
                # consider we polled part of the group
                result += key
            else:
                # there are multiple groups there
                result += key * math.ceil(count / key)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.numRabbits([1,1,2]))
    print(x.numRabbits([0,0,1,1,1]))
