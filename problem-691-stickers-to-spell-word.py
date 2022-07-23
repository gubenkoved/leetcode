from typing import List
from collections import Counter


def overlap_count(x, y):
    x_counter = Counter(x)
    y_counter = Counter(y)
    total_count = 0
    for key in x_counter.keys():
        total_count += min(x_counter[key], y_counter[key])
    return total_count


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # sanitize the input -- remove all the stickers letters which are not in
        # the target word
        def sanitize(sticker, target):
            return ''.join([c for c in sticker if c in target])

        stickers = [sanitize(sticker, target) for sticker in stickers]
        stickers = [x for x in stickers if x]
        # stickers = sorted(stickers, key=lambda x: overlap_count(x, target),
        #                   reverse=True)

        # see if it is even possible to solve
        if set(target) - set(''.join(stickers)):
            return -1

        # worst case -- sticker gives a single letter each time
        best_count = len(target)

        def search(current_count: int, target: str):
            nonlocal best_count

            # no need to continue searching
            if current_count >= best_count:
                return

            if not target:
                best_count = current_count
                return

            # sanitize stickers
            # stickers = [sanitize(sticker, target) for sticker in stickers]
            # stickers = [x for x in stickers if x]
            # stickers = sorted(stickers, key=lambda x: overlap_count(x, target), reverse=True)

            for sticker in stickers:
                new_target = target
                for char in sticker:
                    char_idx = new_target.find(char)
                    if char_idx != -1:
                        new_target = new_target[:char_idx] + new_target[char_idx+1:]
                search(1 + current_count, new_target)

        search(0, target)

        return best_count


if __name__ == '__main__':
    x = Solution()
    # print(x.minStickers(["with", "example", "science"], target="thehat"))
    # print(x.minStickers(["these","guess","about","garden","him"], target="atomher"))
    print(x.minStickers(["seven","old","stream","century","energy","period","an","proper","together","sight","carry","milk","appear","winter","field","rather","caught","danger","lake","shall","machine","few","other","test","got","wing","map","finish","though","observe","log","they","foot","path","eat","glad","must","bar","did","of","clear","work","rule","quotient","produce","clean","wild","grass","example","left"], "weresurprise"))
