import collections
import bisect


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counts = collections.Counter(word)

        # ascending sorted list of frequencies
        cl = sorted(counts.values())

        # ps[i] is a prefix sum for cl array in range [0; i]
        ps = [0] * len(cl)
        ps[0] = cl[0]
        for idx in range(1, len(cl)):
            ps[idx] = ps[idx - 1] + cl[idx]

        result = len(word)
        for idx in range(len(cl)):

            min_freq = cl[idx]
            max_freq = cl[idx] + k

            # find sum of frequencies which are outside if [min_freq, max_freq]
            min_idx = bisect.bisect_left(cl, min_freq)
            max_idx = bisect.bisect_right(cl, max_freq)

            if cl[min_idx] == min_freq:
                min_idx -= 1

            need_to_remove = 0

            if min_idx >= 0:
                need_to_remove += ps[min_idx]

            # higher frequencies do not need to be fully removed though, they
            # just need to be made max_freq
            hi_count = len(ps) - max_idx
            need_to_remove += (ps[-1] - ps[max_idx - 1]) - hi_count * max_freq

            result = min(result, need_to_remove)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.minimumDeletions("aabcaba", k = 0))
    print(x.minimumDeletions("dabdcbdcdcd", k = 2))
    print(x.minimumDeletions("aaabaaa", k = 2))
    print(x.minimumDeletions('x', 100000))
