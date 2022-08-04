from typing import List
from collections import Counter
from functools import lru_cache


def overlap_count(x, y):
    x_counter = Counter(x)
    y_counter = Counter(y)
    total_count = 0
    for key in x_counter.keys():
        total_count += min(x_counter[key], y_counter[key])
    return total_count


def is_dominated(dominator, dominated):
    # returns True if dominator has all the chars that dominated has
    # with either same or bigger amount
    dominator_counts = Counter(dominator)
    dominated_counts = Counter(dominated)

    for key in dominated_counts:
        if dominator_counts.get(key, 0) < dominated_counts[key]:
            return False

    return True


class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        # sanitize the input -- remove all the stickers letters which are not in
        # the target word
        def sanitize(sticker, target):
            return ''.join([c for c in sticker if c in target])

        stickers = [sanitize(sticker, target) for sticker in stickers]
        stickers = [''.join(sorted(x)) for x in stickers if x]
        stickers = list(set(stickers))

        # remove stickers which are "dominated" by another ones
        to_remove = set()
        for sticker_a in stickers:
            for sticker_b in stickers:
                if sticker_a != sticker_b and is_dominated(sticker_a, sticker_b):
                    print('%s dominated by %s' % (sticker_b, sticker_a))
                    to_remove.add(sticker_b)

        print('dominated stickers: %s' % to_remove)
        stickers = [x for x in stickers if x not in to_remove]

        # sort stickers by the amount of the matching chars
        # stickers = sorted(stickers, key=lambda x: overlap_count(x, target),
        #                   reverse=True)

        print('stickers left: %s' % stickers)

        # see if it is even possible to solve
        if set(target) - set(''.join(stickers)):
            return -1

        # worst case -- sticker gives a single letter each time
        best_count = len(target)

        @lru_cache(None)
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
    # print(x.minStickers(["seven","old","stream","century","energy","period","an","proper","together","sight","carry","milk","appear","winter","field","rather","caught","danger","lake","shall","machine","few","other","test","got","wing","map","finish","though","observe","log","they","foot","path","eat","glad","must","bar","did","of","clear","work","rule","quotient","produce","clean","wild","grass","example","left"], "weresurprise"))
    # print(x.minStickers(["final","figure","danger","fish","some","product","son","seed","crease","rail","even","death","end","sit","live","behind","start","enough","much","between","test","is","happy","we","north","complete","month","reach","excite","stay","job","fell","letter","noun","seat","exact","than","ago","protect","kept","this","plain","flow","face","bird","sand","rock","roll","root","fact"], "lakeblue"))
    print(x.minStickers(["indicate","why","finger","star","unit","board","sister","danger","deal","bit","phrase","caught","if","other","water","huge","general","read","gold","shall","master","men","lay","party","grow","view","if","pull","together","head","thank","street","natural","pull","raise","cost","spoke","race","new","race","liquid","me","please","clear","could","reply","often","huge","old","nor"], "fhhfiyfdcwbycma"))
