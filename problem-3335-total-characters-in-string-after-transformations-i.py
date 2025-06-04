class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        n = 26

        # array with counts for every letter
        counts = [0] * n

        # index where counts actually start with "a" and continue, needed due
        # to mechanics of the transformation where "a" is turned into "b",
        # "b" into "c", etc which is equivalent to offset going back really...
        offset = 0

        def at(idx):
            return counts[(idx + offset) % n]

        def set(idx, val):
            counts[(idx + offset) % n] = val

        # init counts with the original string
        for c in s:
            char_idx = ord(c) - ord('a')
            counts[char_idx] += 1

        for _ in range(t):
            # "z" goes to "ab", other chars just grow bigger 1 step
            z_count = at(25)
            set(25, 0)

            # simulate a processing step
            offset -= 1

            # update the a/b counts using the z counts we had on that step
            set(0, at(0) + z_count)
            set(1, at(1) + z_count)

        return sum(counts) % (10 ** 9 + 7)


if __name__ == '__main__':
    x = Solution()
    print(x.lengthAfterTransformations("abcyy", 2))
