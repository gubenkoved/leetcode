class Solution:
    def bestClosingTime(self, customers: str) -> int:
        customers += 'N'

        best_time = None
        best_penalty = None

        customers_to_the_left = 0
        customers_to_the_right = sum(1 for c in customers if c == 'Y')
        for t in range(len(customers)):
            penalty = t - customers_to_the_left
            penalty += customers_to_the_right

            if best_penalty is None or penalty < best_penalty:
                best_time = t
                best_penalty = penalty

            # update the counters
            if customers[t] == 'Y':
                customers_to_the_right -= 1
                customers_to_the_left += 1
        return best_time

