class Solution:
    def totalMoney(self, n: int) -> int:
        money = 1
        prev_monday = 1
        prev_day = 1
        for day_idx in range(1, n):
            if day_idx % 7 != 0:
                money += prev_day + 1
                prev_day += 1
            else:  # Monday
                money += prev_monday + 1
                prev_monday += 1
                prev_day = prev_monday
        return money
