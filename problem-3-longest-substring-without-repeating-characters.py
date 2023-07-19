class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left, right = 0, 0
        result = 1
        freq = {}  # char -> freq
        n = len(s)

        freq[s[0]] = 1

        while True:
            # total end condition
            if right == n - 1:
                break

            duplicate = False

            # move right pointer until we hit the first duplicate
            while True:
                if right < n - 1:
                    right += 1
                else:  # can not go any further
                    break

                added = s[right]

                if added not in freq:
                    freq[added] = 1
                else:
                    freq[added] += 1

                if freq[added] == 1:
                    # no duplicates
                    result = max(result, right - left + 1)
                    duplicate = False
                else:
                    duplicate = True
                    break

            # move left pointer until we got rid of duplicate
            if duplicate:
                while True:
                    if left < n - 1:
                        left += 1

                    removed = s[left - 1]
                    freq[removed] -= 1
                    if freq[removed] == 1:
                        result = max(result, right - left + 1)
                        break

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.lengthOfLongestSubstring('abcd'))
    print(x.lengthOfLongestSubstring('abcabcbb'))
    print(x.lengthOfLongestSubstring('bbbbb'))
    print(x.lengthOfLongestSubstring('pwwkew'))
    print(x.lengthOfLongestSubstring(''))