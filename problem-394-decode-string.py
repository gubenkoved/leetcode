class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)

        def read_int(idx):
            result = ''

            while s[idx].isdigit():
                result += s[idx]
                idx += 1

            return int(result), idx

        def eval(idx):
            result = ''

            while idx < n:
                if s[idx].isdigit():
                    k, idx = read_int(idx)
                    assert s[idx] == '['
                    idx += 1
                    sub_result, idx = eval(idx)
                    assert s[idx] == ']'
                    idx += 1
                    result += sub_result * k
                elif s[idx] == ']':
                    break
                else:
                    result += s[idx]
                    idx += 1

            return result, idx

        result, _ = eval(0)

        return result


if __name__ == '__main__':
    x = Solution()
    print(x.decodeString('a2[c]'))
    print(x.decodeString('3[a2[c]]'))
