from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # can be solved greedily in the following way:
        # the best token to gain score is the one with the lowest value
        # the best token to gain power is the token with the largest value
        # so we will play as follows:
        # 1. sort tokens by value
        # 2. initialize left and right pointers
        # 3. from the left: if you can play "face-up" (score at least 1) and current power is not less than the token -> do!
        # 4. otherwise play "face-down" the token from the right

        tokens = sorted(tokens)
        l, r = 0, len(tokens) - 1
        score = 0
        best_score = score

        while l <= r:
            if power >= tokens[l]:
                score += 1
                power -= tokens[l]
                l += 1
            elif score > 0:
                power += tokens[r]
                r -= 1
                score -= 1
            else:
                # can not do anything at al!
                break
            best_score = max(best_score, score)
        return best_score


if __name__ == '__main__':
    x = Solution()
    assert x.bagOfTokensScore([200, 100], 150) == 1
    assert x.bagOfTokensScore([100,200,300,400], 200) == 2
