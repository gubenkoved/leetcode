from typing import List
import random


def match_count(w1, w2):
    return sum(1 for c1, c2 in zip(w1, w2) if c1 == c2)


class Master:
    def __init__(self, secret, words):
        self.secret = secret
        self.words = words
        self.guess_count = 0

    def guess(self, word: str) -> int:
        self.guess_count += 1
        if word not in self.words:
            return -1
        return match_count(self.secret, word)


class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        possible = list(sorted(words))

        while True:
            word = random.choice(possible)
            result = master.guess(word)

            if result == 6:
                break

            possible = [w for w in possible if match_count(w, word) == result]


if __name__ == '__main__':
    def case(secret, words):
        master = Master(secret, words)
        x = Solution()
        x.findSecretWord(words, master)
        print('took %d tries' % master.guess_count)


    case("ccoyyo",
         ["wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt", "kmjmxr", "ihkovg", "trbzyb", "xqulhc",
          "bcsbfw", "rwzslk", "abpjhw", "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo", "awvqlr",
          "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru", "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad",
          "uslult", "rtjosi", "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw", "vunxdn", "jahhfn",
          "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk", "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa",
          "kqbttl", "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh", "wynohw", "lhqxvx", "kaadty",
          "dxxwut", "vjtskm", "yrdswc", "byzjxm", "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg",
          "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm", "xoaumd", "vbejda", "kaefne", "swcrkh",
          "reeyhj", "vmcwaf", "chxitv", "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv", "srxuus",
          "pydgmq"])

    case("azzzzz",
         ["abcdef", "acdefg", "adefgh", "aefghi", "afghij", "aghijk", "ahijkl", "aijklm", "ajklmn", "aklmno", "almnoz",
          "anopqr", "azzzzz"])
