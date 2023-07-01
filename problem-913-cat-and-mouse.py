from typing import List


# A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.
#
# The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.
#
# The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.
#
# During each player's turn, they must travel along one edge of the graph that meets where they are.
# For example, if the Mouse is at node 1, it must travel to any node in graph[1].
#
# Additionally, it is not allowed for the Cat to travel to the Hole (node 0.)
#
# Then, the game can end in three ways:
#
# If ever the Cat occupies the same node as the Mouse, the Cat wins.
# If ever the Mouse reaches the Hole, the Mouse wins.
# If ever a position is repeated (i.e., the players are in the same position as a
# previous turn, and it is the same player's turn to move), the game is a draw.
# Given a graph, and assuming both players play optimally, return
#
# 1 if the mouse wins the game,
# 2 if the cat wins the game, or
# 0 if the game is a draw.


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        history = set()

        def trace(depth, message):
            if depth <= 3:
                print('%s%s' % ('  ' * depth, message))

        analyzed = dict()

        def f(mouse_turn, mouse_position, cat_position, depth) -> int:
            cur_key = (mouse_turn, mouse_position, cat_position)

            if cur_key in analyzed:
                trace(depth, 'FAST -> %s' % analyzed[cur_key])
                return analyzed[cur_key]

            if cur_key in history:
                analyzed[cur_key] = 0
                return 0  # draw game as position repeated

            # TODO: add cut off based on the current depth
            #  is that true that if mouse can win it should win in N steps if N is
            #  distance to the hole?

            history.add(cur_key)

            possible = graph[mouse_position if mouse_turn else cat_position]
            best_result = None

            if mouse_turn:
                if depth != 0:
                    trace(depth, 'cat went to %s' % cat_position)
                else:
                    trace(depth, 'start position')
            else:
                trace(depth, 'mouse went to %s' % mouse_position)

            if mouse_turn:
                for pos in possible:
                    trace(depth, 'trying %s' % pos)
                    if pos == 0:
                        result = 1  # mouse wins
                    elif pos == cat_position:
                        result = -1  # cat wins
                    else:
                        result = f(not mouse_turn, pos, cat_position, depth + 1)

                    # update best result
                    if best_result is None:
                        best_result = result
                    else:
                        best_result = max(best_result, result)

                    # stop if we can not get any better
                    if best_result == 1:
                        break
            else:  # cat's turn
                for pos in possible:
                    if pos == 0:
                        continue

                    trace(depth, 'trying %s' % pos)

                    if pos == mouse_position:
                        result = -1  # cat wins
                    else:
                        result = f(not mouse_turn, mouse_position, pos, depth + 1)

                    # update best result
                    if best_result is None:
                        best_result = result
                    else:
                        best_result = min(best_result, result)

                    # stop if we can not get any better
                    if best_result == -1:
                        break

            assert best_result is not None
            trace(depth, '  >> best for %s is %s' % ('mouse' if mouse_turn else 'cat', best_result))

            history.discard(cur_key)

            # if best_result != 0:
            analyzed[cur_key] = best_result

            return best_result

        overall_result = f(True, 1, 2, 0)
        overall_result = 2 if overall_result == -1 else overall_result
        print('RESULT: %s' % overall_result)
        return overall_result


if __name__ == '__main__':
    x = Solution()
    assert x.catMouseGame([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]) == 0
    assert x.catMouseGame([[1, 3], [0], [3], [0, 2]]) == 1
    assert x.catMouseGame([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]]) == 1
    assert x.catMouseGame([[2, 6], [2, 4, 5, 6], [0, 1, 3, 5, 6], [2], [1, 5, 6], [1, 2, 4], [0, 1, 2, 4]]) == 2
    assert x.catMouseGame(
        [[3, 4, 6, 7, 9, 15, 16, 18], [4, 5, 8, 19], [3, 4, 6, 9, 17, 18], [0, 2, 11, 15], [0, 1, 10, 6, 2, 12, 14, 16],
         [1, 10, 7, 9, 15, 17, 18], [0, 10, 4, 7, 9, 2, 11, 12, 13, 14, 15, 17, 19], [0, 10, 5, 6, 9, 16, 17],
         [1, 9, 14, 15, 16, 19], [0, 10, 5, 6, 7, 8, 2, 11, 13, 15, 16, 17, 18], [4, 5, 6, 7, 9, 18], [3, 6, 9, 12, 19],
         [4, 6, 11, 15, 17, 19], [6, 9, 15, 17, 18, 19], [4, 6, 8, 15, 19], [0, 3, 5, 6, 8, 9, 12, 13, 14, 16, 19],
         [0, 4, 7, 8, 9, 15, 17, 18, 19], [5, 6, 7, 9, 2, 12, 13, 16], [0, 10, 5, 9, 2, 13, 16],
         [1, 6, 8, 11, 12, 13, 14, 15, 16]]) == 0
    assert x.catMouseGame(
        [[5, 21, 28], [6, 8, 9, 13, 23, 24, 30], [9, 10, 22, 24], [24, 30], [5, 6, 8, 9, 13, 18, 19, 20, 24],
         [0, 4, 9, 10, 11, 12, 22, 27], [1, 4, 9, 11, 16, 19, 25, 30], [8, 9, 13, 19, 25, 26], [1, 4, 7, 9, 29],
         [1, 2, 4, 5, 6, 7, 8, 13, 18, 19, 24, 26, 28, 29], [2, 5, 15, 22, 27, 30], [5, 6, 12, 24], [5, 11, 20, 22, 23],
         [1, 4, 7, 9, 29, 30], [19, 24, 27], [10, 16, 19], [6, 15, 27], [20, 22, 24, 29], [4, 9, 21],
         [4, 6, 7, 9, 14, 15, 20, 26, 28, 30], [4, 12, 17, 19, 21], [0, 18, 20, 27], [2, 5, 10, 12, 17],
         [1, 12, 26, 30], [1, 2, 3, 4, 9, 11, 14, 17, 27, 29], [6, 7, 26, 27, 29], [7, 9, 19, 23, 25],
         [5, 10, 14, 16, 21, 24, 25], [0, 9, 19, 30], [8, 9, 13, 17, 24, 25], [1, 3, 6, 10, 13, 19, 23, 28]]) == 0
    assert x.catMouseGame([[5, 6], [3, 4], [6], [1, 4, 5], [1, 3, 5], [0, 3, 4, 6], [0, 2, 5]]) == 2  # WA on 58 test
