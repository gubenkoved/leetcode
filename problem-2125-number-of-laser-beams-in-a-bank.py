from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev_count = 0
        for row in bank:
            laser_count = sum(1 for c in row if c == '1')
            if laser_count:
                beams += laser_count * prev_count
                prev_count = laser_count
        return beams
