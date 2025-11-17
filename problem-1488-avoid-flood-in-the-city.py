from typing import List


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = []
        full = set()
        for idx in range(n):
            if rains[idx] == 0:
                cursor = idx + 1
                while cursor < n:
                    if rains[cursor] != 0 and rains[cursor] in full:
                        break
                    cursor += 1
                if cursor == n:
                    ans.append(1)  # whatever
                else:
                    ans.append(rains[cursor])
                    full.discard(rains[cursor])
            else:
                ans.append(-1)
                if rains[idx] in full:
                    return []
                full.add(rains[idx])
        return ans


if __name__ == '__main__':
    x = Solution()
    print(x.avoidFlood([1,2,0,0,2,1]))
