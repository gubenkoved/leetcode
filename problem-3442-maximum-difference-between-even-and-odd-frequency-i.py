from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        counts = Counter(s)
        min_even_freq = float('inf')
        max_odd_freq = 0
        for freq in counts.values():
            if freq % 2 == 0:
                min_even_freq = min(min_even_freq, freq)
            else:
                max_odd_freq = max(max_odd_freq, freq)
        return max_odd_freq - min_even_freq


if __name__ == '__main__':
    x = Solution()
    print(x.maxDifference('aaaaabbc'))
