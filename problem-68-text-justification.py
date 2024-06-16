from typing import List
from math import ceil


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        def justify(words) -> str:
            result = ''
            words_len = sum(len(x) for x in words)

            for idx, word in enumerate(words):
                spaces_count_left = len(words) - idx - 1
                extra_space_left = maxWidth - words_len - len(result)
                result += word
                if idx != len(words) - 1:
                    result += ' ' * ceil(extra_space_left / spaces_count_left)
                words_len -= len(word)

            # edge case with end spaces
            if len(result) < maxWidth:
                result += ' ' * (maxWidth - len(result))

            return result

        def left_justify(words) -> str:
            result = ' '.join(words)
            return result + ' ' * (maxWidth - len(result))

        def min_len(line_words_len, line_words_count, extra_word):
            if line_words_count == 0:
                return len(extra_word)
            return line_words_len + line_words_count + len(extra_word)

        line = []
        line_words_len = 0
        for word in words:
            if min_len(line_words_len, len(line), word) <= maxWidth:
                line.append(word)
                line_words_len += len(word)
            else:
                lines.append(line)
                line = [word]
                line_words_len = len(word)

        if line:
            lines.append(line)

        result = []
        for idx, line in enumerate(lines):
            if idx < len(lines) - 1:
                result.append(justify(line))
            else:
                result.append(left_justify(line))

        return result


if __name__ == '__main__':
    x = Solution()

    def case(words, maxWidth):
        result = x.fullJustify(words, maxWidth)
        for line in result:
            print('"%s"' % line)
        print('***')

    case(["This", "is", "an", "example", "of", "text", "justification."], maxWidth=16)
    case(["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
    case(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth=20)
    case(["Listen","to","many,","speak","to","a","few."], 6)
