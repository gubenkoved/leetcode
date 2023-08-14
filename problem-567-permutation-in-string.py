from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def rolling_hash(s):
            result = 0
            for c in s:
                result ^= ord(c)
            return result

        s1 = ''.join(sorted(s1))
        s1_hash = rolling_hash(s1)
        s1_freq = Counter(s1)

        window_hash = rolling_hash(s2[:len(s1) - 1])

        k = len(s1)
        for idx in range(len(s2) - k + 1):
            # hash in new character
            window_hash ^= ord(s2[idx + k - 1])

            # hash out out-of-window character
            if idx > 0:
                window_hash ^= ord(s2[idx - 1])

            if window_hash == s1_hash:
                if Counter(s2[idx:idx + len(s1)]) == s1_freq:
                    return True

        return False


if __name__ == '__main__':
    x = Solution()
    print(x.checkInclusion(s1="ab", s2="aabb"))
    print(x.checkInclusion(s1="ab", s2="eidbaooo"))
    print(x.checkInclusion(s1="ab", s2="eidboaoo"))
