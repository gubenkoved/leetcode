class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        # compress into array showing amount of repetitions
        rep = []
        prev = word[0]
        count = 1
        for c in word[1:]:
            if c != prev:
                rep.append(count)
                count = 1
            else:
                count += 1
            prev = c
        rep.append(count)

        # rolling multiplication
        rolling_mult = [1] * len(rep)
        tmp = 1
        for idx in range(len(rep) - 1, -1, -1):
            tmp *= rep[idx]
            rolling_mult[idx] = tmp

        rolling_sum = [0] * len(rep)
        tmp = 0
        for idx in range(len(rep) - 1, -1, -1):
            tmp += rep[idx]
            rolling_sum[idx] = tmp

        # now we operate purely on the level of repetition counts

        def f(start_idx, at_least):
            #print('f(%s, %s)' % (start_idx, at_least))
            if start_idx == len(rep):
                if at_least <= 0:
                    #print('f(%s, %s) -> %s' % (start_idx, at_least, 1))
                    return 1
                else:
                    #print('f(%s, %s) -> %s' % (start_idx, at_least, 0))
                    return 0

            if at_least <= 0:
                return rolling_mult[start_idx]

            left_over_at_most = rolling_sum[start_idx + 1] if start_idx + 1 < len(rolling_sum) else 0

            result = 0
            for rc in range(max(1, at_least - left_over_at_most), rep[start_idx] + 1):
                result += f(start_idx + 1, at_least - rc)
            #print('f(%s, %s) -> %s' % (start_idx, at_least, result))
            return result

        return f(0, k)


if __name__ == '__main__':
    x = Solution()
    print(x.possibleStringCount('dd', 1))
    print(x.possibleStringCount('ccdd', 3))
    print(x.possibleStringCount('bbccdd', 5))
    print(x.possibleStringCount("aabbccdd", k = 7))
    print(x.possibleStringCount("bbbbbyyyyyyyyyyccccccccyyyqqqqhffffhhhhhhhhsswwwwvvvvvlllldddddddddnnnnnnvr", 69))
