class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        num_min = int(num.replace(num[0], '0'))

        for c in num:
            if c != '9':
                num_max = int(num.replace(c, '9'))
                break
        else:
            num_max = int(num)

        return num_max - num_min


if __name__ == '__main__':
    x = Solution()
    x.minMaxDifference(99999)
