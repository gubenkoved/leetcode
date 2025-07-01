class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        rolling = 1
        prev = word[0]
        for c in word[1:] + '_':
            if c != prev:
                result += rolling - 1
                rolling = 0
            rolling += 1
            prev = c
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.possibleStringCount('abbcccc'))
