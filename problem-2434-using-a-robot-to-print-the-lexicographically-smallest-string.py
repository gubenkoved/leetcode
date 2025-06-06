class Solution:
    def robotWithString(self, s: str) -> str:
        # smallest from the right
        n = len(s)
        sr = [None] * n

        rolling_smallest = s[-1]
        for idx in range(n - 1, -1, -1):
            rolling_smallest = min(rolling_smallest, s[idx])
            sr[idx] = rolling_smallest


        result = []
        idx = 0
        stack = []

        while True:
            if idx < n and (not stack or sr[idx] < stack[-1]):
                stack.append(s[idx])
                idx += 1
            else:
                if not stack:
                    break
                result.append(stack.pop(-1))

        return ''.join(result)


if __name__ == '__main__':
    x = Solution()
    print(x.robotWithString('qwebaqwea'))  # aaewqbewq
