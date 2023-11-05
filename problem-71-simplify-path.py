class Solution:
    def simplifyPath(self, path: str) -> str:
        components = [x for x in path.split('/') if x]
        result = []

        for component in components:
            if component == '.':
                pass
            elif component == '..':
                if result:
                    del result[-1]
            else:
                result.append(component)
        return '/' + '/'.join(result)


if __name__ == '__main__':
    x = Solution()
    # assert x.simplifyPath('/home/') == '/home'
    assert x.simplifyPath("/a/./b/../../c/") == '/c'
