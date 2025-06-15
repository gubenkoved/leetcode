class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)

        for idx, c in enumerate(num):
            if idx == 0:
                if c != '1':
                    num_min = int(num.replace(c, '1'))
                    break
            else:
                if c != '0' and c != num[0]:
                    num_min = int(num.replace(c, '0'))
                    break
        else:
            num_min = int(num)

        for c in num:
            if c != '9':
                num_max = int(num.replace(c, '9'))
                break
        else:
            num_max = int(num)

        return num_max - num_min

if __name__ == '__main__':
    x = Solution()
    print(x.maxDiff(111))
