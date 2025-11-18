from typing import List
from sortedcontainers import SortedList
import bisect

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [0] * n

        filled_at = {}  # lake -> day it was filled
        dry_days = SortedList()

        for day in range(n):
            if rains[day] == 0:
                dry_days.add(day)
            else:
                ans[day] = -1
                lake = rains[day]

                if lake not in filled_at:
                    filled_at[lake] = day
                else:
                    # okay, if we got there it means there would be overflow
                    # if we did not dry it, so we have to dry it, and we should
                    # greedily pick the EARLIEST day it could be dried

                    if not dry_days:
                        # no dry days left -> no possible
                        return []

                    lake_filled_at = filled_at[lake]

                    # find the first suitable dry day
                    dry_days_idx = bisect.bisect_left(dry_days, lake_filled_at)

                    if dry_days_idx == len(dry_days):
                        return []
                    else:
                        # found a dry day, update answer and drop it
                        dry_day = dry_days[dry_days_idx]
                        ans[dry_day] = lake
                        dry_days.discard(dry_day)
                        filled_at[lake] = day

        # replace unused dry days with any lake number
        while dry_days:
            day = dry_days.pop()
            ans[day] = 1

        return ans


if __name__ == '__main__':
    x = Solution()
    print(x.avoidFlood([1, 2, 0, 0, 2, 1]))
    print(x.avoidFlood([1, 2, 0, 0, 3, 2, 1]))
    print(x.avoidFlood([1, 2, 0, 0, 3, 2, 1, 0, 2]))
    print(x.avoidFlood([1, 2, 3, 0, 4, 5, 0, 0, 4, 5, 0, 1, 7]))
    print(x.avoidFlood([1, 2, 3, 4, 5, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5]))
    print(x.avoidFlood([1,0,2,3,0,1,2]), [-1,1,-1,-1,2,-1,-1])
    print(x.avoidFlood([1, 2, 0, 1, 2]), [])
    print(x.avoidFlood([1,0,2,0,3,0,2,0,0,0,1,2,3]), [-1,1,-1,2,-1,3,-1,2,1,1,-1,-1,-1])
