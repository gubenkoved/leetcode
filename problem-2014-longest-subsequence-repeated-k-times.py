import itertools


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        max_len = n // k

        # compose freq dict for each index freqs[i] would need freq dict
        # for substricng from i-th index (incl) till the end

        freqs = [None] * n
        next_idxs = [None] * n

        freq = {}
        next_idx = {}
        for idx in range(n - 1, -1, -1):
            c = s[idx]
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
            next_idx[c] = idx

            freqs[idx] = freq.copy()
            next_idxs[idx] = next_idx.copy()

        def verify(sub, start_idx, k):
            idx = start_idx
            for c in sub:
                if idx >= n:
                    return False
                next_idx_map = next_idxs[idx]
                if c not in next_idx_map:
                    return False
                # optional cut-off check
                if freqs[idx][c] < k:
                    return False
                idx = next_idx_map[c] + 1  # go to next char

            if k == 1:
                return True

            return verify(sub, idx, k - 1)

        candidates = ''

        # NOTE: same char may be included multiple times in resulting substring
        for c, f in freqs[0].items():
            candidates += c * (f // k)

        # try all the permutations up to max_len size here
        for l in range(max_len, 0, -1):
            for sub in sorted(itertools.permutations(candidates, l), reverse=True):
                if verify(sub, 0, k):
                    return ''.join(sub)

        return ''


if __name__ == '__main__':
    x = Solution()
    print(x.longestSubsequenceRepeatedK(s = "letsleetcode", k = 2))
    print(x.longestSubsequenceRepeatedK(s = "bb", k = 2))
    print(x.longestSubsequenceRepeatedK(s = "ab", k = 2))
    print(x.longestSubsequenceRepeatedK(s = "bbabbabbbbabaababab", k=3))
