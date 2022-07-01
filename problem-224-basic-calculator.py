class Reader:
    def __init__(self, s):
        self.s = s
        self.idx = 0

    def peek(self) -> str:
        if self.idx >= len(self.s):
            return None
        return self.s[self.idx]

    def next(self) -> str:
        self.idx += 1
        return self.peek()

# EXPRESSION := EXPRESSION + EXPRESSION
# EXPRESSION := EXPRESSION - EXPRESSION
# EXPRESSION := TERM
# TERM := number
# TERM := ( EXPRESSION )
# TERM := - TERM


def expression(reader: Reader):
    result = term(reader)

    while True:
        c = reader.peek()

        if c is None:
            break

        if c == '+':
            reader.next()
            result += term(reader)
        elif c == '-':
            reader.next()
            result -= term(reader)
        elif c == ')':
            break
        else:
            assert False, 'unexpected: %s' % c

    return result


def term(reader: Reader):
    c = reader.peek()

    if c == '(':
        reader.next()
        v = expression(reader)
        assert reader.peek() == ')', 'closing bracket expected'
        reader.next()
        return v
    elif c == '-':
        reader.next()
        return -term(reader)
    else:
        num = reader.peek()
        while True:
            c = reader.next()
            if c is not None and c.isdigit():
                num += c
            else:
                break
        return int(num)


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        return expression(Reader(s))


if __name__ == '__main__':
    x = Solution()
    # print(x.calculate('(1+(4+5+2)-3)+(6+8)'))
