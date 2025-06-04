from typing import List

class Solution:
    def maxCandies(
            self, status: List[int], candies: List[int], keys: List[List[int]],
            containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:

        result = 0
        accessible = set(initialBoxes)
        acquired_keys = set()

        while accessible:
            progressed = False

            for box in list(accessible):
                if status[box] == 1 or box in acquired_keys:
                    result += candies[box]
                    acquired_keys.update(keys[box])
                    accessible.update(containedBoxes[box])
                    accessible.discard(box)
                    progressed = True

            if not progressed:
                break

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.maxCandies(status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]))
    print(x.maxCandies(status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]))
