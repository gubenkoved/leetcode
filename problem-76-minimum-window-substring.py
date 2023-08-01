class Solution:
    def minWindow(self, s: str, t: str) -> str:
        debt = {}
        for x in t:
            if x not in debt:
                debt[x] = 0
            debt[x] += 1

        left = 0
        right = 0
        n = len(s)

        precious = set(t)

        if s[0] in precious:
            debt[s[0]] -= 1

        result = ''

        while True:
            # move the right pointer until we acquire all the characters we need
            cur_debt = {c: balance for c, balance in debt.items() if balance > 0}

            while cur_debt:
                right += 1
                if right == n:
                    return result
                if s[right] in cur_debt:
                    cur_debt[s[right]] -= 1
                    if cur_debt[s[right]] == 0:
                        del cur_debt[s[right]]
                if s[right] in precious:
                    debt[s[right]] -= 1

            if not result or (right - left + 1) < len(result):
                result = s[left:right + 1]

            # now move the left pointer until we lose precious
            while left <= right:
                left += 1
                lost_char = s[left - 1]
                if lost_char in precious:
                    if lost_char not in debt:
                        debt[lost_char] = 0
                    debt[lost_char] += 1

                    if debt[lost_char] > 0:
                        break

                # update the result!
                if (right - left + 1) < len(result):
                    result = s[left:right + 1]

        assert False, 'should not be there'


if __name__ == '__main__':
    x = Solution()
    print(x.minWindow(s='aaabbbccc', t='acb'))
    print(x.minWindow(s='ADOBECODEBANC', t='ABC'))
    print(x.minWindow(s='a', t='aa'))
    print(x.minWindow(s='a', t='a'))
