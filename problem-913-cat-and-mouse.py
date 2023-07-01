from typing import List
from collections import defaultdict, deque
import sys

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


sys.setrecursionlimit(50 * 50 * 2 + 10)


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        # STAGE 1. Construct the state transition graph
        #  it should have no cycles because a path via state graph via cycle is
        #  a draw game, but we will only calculate for the cat or mouse wins
        #
        #  ADDITIONALLY,
        #  Fill the final outcomes mapping.

        # state is (mouse_position, cat_position, is_mouse_turn)
        visited = set()
        next_states_map = defaultdict(set)  # state -> next states
        prev_states_map = defaultdict(set)  # state -> prev states
        outcomes_map = {}
        active = deque()

        def construct(mouse, cat, is_mouse_turn):
            state = (mouse, cat, is_mouse_turn)

            if state in visited:
                return

            visited.add(state)
            outcome = None

            assert cat != 0, 'cat can not be on hole'

            if is_mouse_turn:  # cat just turned
                adjacent = graph[mouse]
                if mouse == cat:
                    outcome = 2
            else:  # cat's turn, mouse just turned
                adjacent = graph[cat]
                if mouse == 0:
                    outcome = 1
                elif mouse == cat:
                    outcome = 2

            # final state found, do not go any further
            if outcome is not None:
                # print('  > FINAL (%s, %s, %s) -> %s' % (mouse, cat, is_mouse_turn, outcome))
                outcomes_map[state] = outcome
                active.append(state)
                return

            for position in adjacent:
                if is_mouse_turn:
                    next_state = (position, cat, not is_mouse_turn)
                else:  # cat's turn
                    if position == 0:
                        continue  # cat can not go to the hole
                    next_state = (mouse, position, not is_mouse_turn)

                next_states_map[state].add(next_state)
                prev_states_map[next_state].add(state)

                construct(*next_state)

        construct(1, 2, True)

        print('  N: %d' % n)
        print('  STATES FOUND: %d' % len(visited))
        print('  LEAFS: %d' % len(outcomes_map))

        # STAGE 2. Propagate the known outcomes up by the state tree
        while active:
            state = active.popleft()
            mouse, cat, is_mouse_turn = state
            # print('  PROCESS (%s, %s, %s)' % (mouse, cat, is_mouse_turn))
            outcome = outcomes_map[state]

            for prev_state in prev_states_map[state]:
                if prev_state is outcomes_map:
                    continue

                prev_outcome = None

                if is_mouse_turn:
                    # prev move was by cat
                    if outcome == 2:
                        prev_outcome = 2
                else:
                    # prev move was by mouse
                    if outcome == 1:
                        prev_outcome = 1  # since mouse moves and "state" is win, mouse will pick it!

                # if outcome is not winning for the moving party, but it is the only
                # outcome possible from "prev_state" then mark it as such
                # note that we do not check the outcome value itself, but we can be
                # sure that it is NOT winning value as otherwise it would have been
                # propagated and prev_outcome would have been not None
                if prev_outcome is None:
                    prev_state_next_undefined_count = sum(
                        1 for x in next_states_map[prev_state]
                        if outcomes_map.get(x, None) is None)
                    if prev_state_next_undefined_count == 0:
                        # if all the outcomes from the prev are the same -> set it to the prev as inevitable!
                        if len(set(outcomes_map[x] for x in next_states_map[prev_state])) == 1:
                            prev_outcome = outcome

                if prev_outcome is not None and prev_state not in outcomes_map:
                    # print('    SET (%s, %s, %s) to %s' % (prev_state + (prev_outcome,)))
                    outcomes_map[prev_state] = prev_outcome
                    active.append(prev_state)

        return outcomes_map.get((1, 2, True), 0)


if __name__ == '__main__':
    x = Solution()


    def case(graph, expected):
        print('SOLVING %s' % graph)
        actual = x.catMouseGame(graph)
        if actual != expected:
            print('  WA: expected %s, but got %s' % (expected, actual))
        else:
            print('  OK! %s' % actual)


    case([[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]], 0)
    case([[1, 3], [0], [3], [0, 2]], 1)
    case([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]], 1)
    case([[2, 6], [2, 4, 5, 6], [0, 1, 3, 5, 6], [2], [1, 5, 6], [1, 2, 4], [0, 1, 2, 4]], 2)
    case(
        [[3, 4, 6, 7, 9, 15, 16, 18], [4, 5, 8, 19], [3, 4, 6, 9, 17, 18], [0, 2, 11, 15], [0, 1, 10, 6, 2, 12, 14, 16],
         [1, 10, 7, 9, 15, 17, 18], [0, 10, 4, 7, 9, 2, 11, 12, 13, 14, 15, 17, 19], [0, 10, 5, 6, 9, 16, 17],
         [1, 9, 14, 15, 16, 19], [0, 10, 5, 6, 7, 8, 2, 11, 13, 15, 16, 17, 18], [4, 5, 6, 7, 9, 18], [3, 6, 9, 12, 19],
         [4, 6, 11, 15, 17, 19], [6, 9, 15, 17, 18, 19], [4, 6, 8, 15, 19], [0, 3, 5, 6, 8, 9, 12, 13, 14, 16, 19],
         [0, 4, 7, 8, 9, 15, 17, 18, 19], [5, 6, 7, 9, 2, 12, 13, 16], [0, 10, 5, 9, 2, 13, 16],
         [1, 6, 8, 11, 12, 13, 14, 15, 16]], 1)
    case(
        [[5, 21, 28], [6, 8, 9, 13, 23, 24, 30], [9, 10, 22, 24], [24, 30], [5, 6, 8, 9, 13, 18, 19, 20, 24],
         [0, 4, 9, 10, 11, 12, 22, 27], [1, 4, 9, 11, 16, 19, 25, 30], [8, 9, 13, 19, 25, 26], [1, 4, 7, 9, 29],
         [1, 2, 4, 5, 6, 7, 8, 13, 18, 19, 24, 26, 28, 29], [2, 5, 15, 22, 27, 30], [5, 6, 12, 24], [5, 11, 20, 22, 23],
         [1, 4, 7, 9, 29, 30], [19, 24, 27], [10, 16, 19], [6, 15, 27], [20, 22, 24, 29], [4, 9, 21],
         [4, 6, 7, 9, 14, 15, 20, 26, 28, 30], [4, 12, 17, 19, 21], [0, 18, 20, 27], [2, 5, 10, 12, 17],
         [1, 12, 26, 30], [1, 2, 3, 4, 9, 11, 14, 17, 27, 29], [6, 7, 26, 27, 29], [7, 9, 19, 23, 25],
         [5, 10, 14, 16, 21, 24, 25], [0, 9, 19, 30], [8, 9, 13, 17, 24, 25], [1, 3, 6, 10, 13, 19, 23, 28]], 1)
    case([[5, 6], [3, 4], [6], [1, 4, 5], [1, 3, 5], [0, 3, 4, 6], [0, 2, 5]], 2)
    case([[2, 3, 4], [2, 4], [0, 1, 4], [0, 4], [0, 1, 2, 3]], 2)
