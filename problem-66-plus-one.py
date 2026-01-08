from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = list(reversed(digits))
        carryover = 1
        for idx in range(len(digits)):
            if carryover:
                result[idx] += carryover
                carryover = 0
                if result[idx] >= 10:
                    carryover = result[idx] // 10
                    result[idx] -= 10

        if carryover:
            result.append(carryover)

        return list(reversed(result))


if __name__ == '__main__':
    x = Solution()
    print(x.plusOne([1,1,1,1]))
    print(x.plusOne([9]))
    print(x.plusOne([9, 9, 9]))
