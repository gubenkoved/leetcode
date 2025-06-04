import collections


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)

        active = set()

        for idx, domino in enumerate(dominoes):
            if domino != '.':
                active.add(idx)

        n = len(dominoes)

        while active:
            # idx -> int (-1 for fall from the right, +1 from the left)
            forces = collections.defaultdict(lambda: 0)

            for idx in active:
                if dominoes[idx] == 'L':
                    if idx > 0 and dominoes[idx - 1] == '.':
                        forces[idx - 1] += -1
                elif dominoes[idx] == 'R':
                    if idx < n - 1 and dominoes[idx + 1] == '.':
                        forces[idx + 1] += +1
                else:
                    assert False, 'unexpected'

            active = set()

            # update the dominos that are forced upon
            for idx, force in forces.items():
                if force == -1:
                    dominoes[idx] = 'L'
                    active.add(idx)
                elif force == +1:
                    dominoes[idx] = 'R'
                    active.add(idx)

        return ''.join(dominoes)


if __name__ == '__main__':
    x = Solution()
    print(x.pushDominoes("RR.L"))
    print(x.pushDominoes(".L.R...LR..L.."))
