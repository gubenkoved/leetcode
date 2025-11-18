from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        potions_count = len(mana)
        magicians_count = len(skill)

        # tracking time each magician freed up
        freed_time = [0] * magicians_count

        # solve for all potions one by one assuming previous potion was
        # brewed by all the magicians;
        # note: the first potion can go full speed, as all the magicians
        # start non-busy;
        # also note: we only need to know when the first magician can start
        # working on the potion, as we HAVE TO process immediately after each
        # magician is done with the potion

        # handle the first potion as a base case
        t = 0
        for magician in range(magicians_count):
            time_needed = skill[magician] * mana[0]
            t += time_needed
            freed_time[magician] = t

        # handle all the other potions
        for potion in range(1, potions_count):
            # backward pass
            start_time = freed_time[-1]
            for magician in range(magicians_count - 2, -1, -1):
                time_needed = skill[magician] * mana[potion]
                start_time = start_time - time_needed
                # make sure we do not start EARLIER than we freed up
                start_time = max(start_time, freed_time[magician])

            # now we know start time for the 1st magician for the given potion!

            # forward pass, fill the freed_time for all the magicians given
            # known start time for the first one
            t = start_time
            for magician in range(magicians_count):
                time_needed = skill[magician] * mana[potion]
                t += time_needed
                freed_time[magician] = t

        return freed_time[-1]


if __name__ == '__main__':
    x = Solution()
    print(x.minTime(skill = [1,5,2,4], mana = [5,1,4,2]), 110)
