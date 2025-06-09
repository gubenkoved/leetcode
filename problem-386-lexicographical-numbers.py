from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        idx = 1
        result = []
        while True:
            result.append(idx)
            if len(result) == n:
                break
            if idx * 10 <= n:
                idx *= 10
            elif idx + 1 <= n and idx % 10 != 9:
                idx += 1
            else:
                while idx + 1 > n or idx % 10 == 9:
                    idx = idx // 10
                idx += 1
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.lexicalOrder(300))
    print([int(x) for x in sorted(str(x) for x in range(1, 300 + 1))])


# 1 10 100 101 .. 109 110 .. 189 190 .. 199 .. 2 20 200
