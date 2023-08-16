from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        next_chars = [None] * n
        rolling_next = {}

        # backwards pass
        for idx in range(n - 1, -1, -1):
            next_chars[idx] = dict(rolling_next)
            rolling_next[s[idx]] = idx

        # go greedy!
        def find_partition_end(start_at):
            idx = start_at
            stop_at = idx

            while idx != n:
                char = s[idx]
                next_char_idx = next_chars[idx].get(char, None)
                if next_char_idx is not None:
                    stop_at = max(stop_at, next_char_idx)
                if idx >= stop_at:
                    break
                idx += 1

            return idx

        parts = []

        idx = 0
        while idx != n:
            end_idx = find_partition_end(idx)
            parts.append(s[idx:end_idx + 1])
            idx = end_idx + 1

        return [len(p) for p in parts]


if __name__ == '__main__':
    x = Solution()
    print(x.partitionLabels('ababcbacadefegdehijhklij'))
