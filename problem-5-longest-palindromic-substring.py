# size of the string is limited by the 1000
class Solution:
    # this is O(n^3) which TLE
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        n = len(s)
        result = ''
        for right in range(0, n):
            for left in range(0, right + 1):
                # check if palindrome
                i, j = left, right
                bad = False
                while i < j:
                    if s[i] != s[j]:
                        bad = True
                        break
                    i += 1
                    j -= 1
                if not bad:
                    if len(result) < right - left + 1:
                        result = s[left:right + 1]
        return result

    # this is O(n^2)
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        result = ''

        for center in range(n):
            # odd len case
            left, right = center, center

            if not result:
                result = s[left:right+1]

            while left > 0 and right < n - 1:
                left -= 1
                right += 1

                if s[left] != s[right]:
                    break

                if len(result) < right - left + 1:
                    result = s[left:right + 1]

            # even len case
            if center < n - 1:
                left, right = center, center + 1

                if s[left] == s[right]:
                    if len(result) < 2:
                        result = s[left:right + 1]
                else:
                    continue  # do not even start expansion phase

                while left > 0 and right < n - 1:
                    left -= 1
                    right += 1

                    if s[left] != s[right]:
                        break

                    if len(result) < right - left + 1:
                        result = s[left:right + 1]

        return result


if __name__ == '__main__':
    x = Solution()

    def p(result):
        print('RESULT IS OF LEN %d: "%s"' % (len(result), result))

    # p(x.longestPalindrome('babad'))
    # p(x.longestPalindrome('cbbd'))
    # p(x.longestPalindrome('aacabdkacaa'))
    # p(x.longestPalindrome(''))
    # p(x.longestPalindrome('a'))
    p(x.longestPalindrome('aaaa'))
    # p(x.longestPalindrome('a' * 100))
    # p(x.longestPalindrome('a' * 1000))
