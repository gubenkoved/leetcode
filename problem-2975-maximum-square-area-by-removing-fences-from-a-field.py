from typing import List

M = 10 ** 9 + 7

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.append(1)
        hFences.append(m)
        vFences.append(1)
        vFences.append(n)

        # find the distances between fences possible to achieve
        hDistances = set()
        for idx in range(len(hFences)):
            for idx2 in range(idx + 1, len(hFences)):
                hDistances.add(abs(hFences[idx] - hFences[idx2]))

        # same for vertical
        vDistances = set()
        for idx in range(len(vFences)):
            for idx2 in range(idx + 1, len(vFences)):
                vDistances.add(abs(vFences[idx] - vFences[idx2]))

        # now find the biggest distance which is in both
        for d in sorted(hDistances, reverse=True):
            if d == 0:
                continue

            if d in vDistances:
                return (d * d) % M

        return -1


if __name__ == '__main__':
    x = Solution()
    print(x.maximizeSquareArea(6, 7, [2], [4]), -1)
