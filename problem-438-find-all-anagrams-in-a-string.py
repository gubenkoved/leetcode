from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def rolling_hash(x):
            result = 0
            for c in x:
                result ^= ord(c)
            return result

        def normalize(x):
            return ''.join(sorted(x))

        def equal_at(start_idx):
            return normalize(s[start_idx:start_idx+len(p)]) == p

        p = normalize(p)
        window_hash = rolling_hash(s[:len(p)])
        target_hash = rolling_hash(p)
        result = []
        prev_passed = False

        for idx in range(len(s) - len(p) + 1):

            if idx != 0:
                window_hash ^= ord(s[idx - 1])
                window_hash ^= ord(s[idx + len(p) - 1])

            if window_hash == target_hash:
                if prev_passed and s[idx - 1] == s[idx + len(p) - 1] or equal_at(idx):
                    result.append(idx)
                    prev_passed = True
                    continue

            prev_passed = False

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.findAnagrams("cbaebabacd", p="abc"))
    # print(x.findAnagrams("abab", p="ab"))
    print(x.findAnagrams("aaaaa", p="aa"))
