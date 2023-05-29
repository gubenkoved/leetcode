from typing import List


class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:

        n, k = len(target), len(stamp)
        matched = [False] * n

        def search(matched_count: int) -> List[int]:

            # try to match stamp completely
            for offset in range(0, n - k + 1):
                is_match = True
                new_matches_count = 0

                for idx in range(k):

                    if stamp[idx] != target[offset + idx] and not matched[offset + idx]:
                        is_match = False
                        break

                    if not matched[offset + idx]:
                        new_matches_count += 1

                if new_matches_count and is_match:
                    for idx in range(k):
                        matched[idx + offset] = True

                    inner_result = search(matched_count + new_matches_count)

                    if not inner_result and (matched_count + new_matches_count) != n:
                        return []

                    return [offset] + inner_result

            return []

        return list(reversed(search(0)))


if __name__ == '__main__':
    x = Solution()
    print(x.movesToStamp('abc', 'ababc'))
    print(x.movesToStamp("abca", "aabcaca"))
    print(x.movesToStamp('oz', 'ooozz'))
    print(x.movesToStamp('cab', 'cabbb'))
    print(x.movesToStamp('oz', 'ooz'))
    print(x.movesToStamp('mda', 'mdadddaaaa'))
