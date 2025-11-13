from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # sort by 0 dimension increasing (use 1st dimension to break the tie)
        envelopes.sort(key=lambda x: (x[0], x[1]))

        n = len(envelopes)
        result = [0] * n

        for idx in range(n):
            w, h = envelopes[idx]
            cur = 0
            for idx2 in range(idx):
                w2, h2 = envelopes[idx2]
                if w > w2 and h > h2:
                    cur = max(cur, 1 + result[idx2])
            result[idx] = cur

        return max(result) + 1


if __name__ == '__main__':
    x = Solution()
    print(x.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]), 3)
