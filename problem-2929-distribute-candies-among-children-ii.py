def dist_2(n, limit):
    # one gets a, then second one gets n - b and both should be under the limit
    if n > limit:
        # [n - limit, limit]
        min_candies = n - limit
        max_candies = limit
        if min_candies > max_candies:
            return 0
        choices = max_candies - min_candies + 1
        return choices
    else:  # n <= limit
        # for 0 candies we still have 1 way, for 1 candy it is two ways, etc
        return n + 1


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for q in range(max(0, n - 2 * limit), min(n, limit) + 1):
            result += dist_2(n - q, limit)
        return result


if __name__ == '__main__':
    x = Solution()
    print(x.distributeCandies(5, 2))
    print(x.distributeCandies(3, 3))
    print(x.distributeCandies(10001, 20002))
    print(x.distributeCandies(10 ** 6, 10 ** 6))
