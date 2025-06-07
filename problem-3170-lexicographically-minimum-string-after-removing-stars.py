import heapq


class Solution:
    def clearStars(self, s: str) -> str:
        heap = []
        removed_idx = set()
        for idx in range(len(s)):
            c = s[idx]
            if c != '*':
                heapq.heappush(heap, (c, -idx))
            else:
                # remove the smallest and with the biggest distance
                # from the start
                _, minus_idx = heapq.heappop(heap)
                removed_idx.add(-minus_idx)

        result = []
        for idx in range(len(s)):
            if idx in removed_idx:
                continue
            if s[idx] == '*':
                continue
            result.append(s[idx])
        return ''.join(result)


if __name__ == '__main__':
    x = Solution()
    print(x.clearStars("aaba*"))
