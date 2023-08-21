from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        k = len(words[0])

        def rolling_hash(s):
            result = 0
            for c in s:
                result ^= ord(c)
            return result

        def norm(s):
            result = []
            for idx in range(len(s) // k):
                result.append(s[idx * k:idx * k + k])
            return ''.join(sorted(result))

        target = ''.join(sorted(words))
        target_hash = rolling_hash(target)

        window_hash = 0
        for idx in range(len(target) - 1):
            window_hash ^= ord(s[idx])

        result = []
        for idx in range(len(s) - len(target) + 1):
            if idx > 0:
                window_hash ^= ord(s[idx - 1])
            window_hash ^= ord(s[idx + len(target) - 1])

            if window_hash == target_hash:
                if norm(s[idx:idx + len(target)]) == target:
                    result.append(idx)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.findSubstring(s="barfoothefoobarman", words=["foo", "bar"]))
    print(x.findSubstring(s="wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
