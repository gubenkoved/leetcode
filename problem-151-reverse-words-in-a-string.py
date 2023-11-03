class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed([w for w in s.split(' ') if w]))


if __name__ == '__main__':
    x = Solution()
    print(x.reverseWords('   a good   example '))
