import time
from collections import deque
from copy import deepcopy
from typing import List

print_ = print
started_at = time.time()


def print(text):
    offset = time.time() - started_at
    print_('[%0.5fs] %s' % (offset, text))


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        global started_at
        started_at = time.time()

        grid = deepcopy(grid)
        m, n = len(grid), len(grid[0])
        result = []

        # start the BFS on the hit point
        # for each of 4 possible start cells, assign the separate label or "color"
        # maintain an information whether we reach the top row for each "color"
        # optimize as follows:
        # 1. note that if N start cells are available, then at least one of them
        #    leads to the top row, so if there are two ways and we found that 1 way
        #    is not leading to the top row and so unstable, then the second way
        #    MUST be stable, otherwise this very cell we hit would be also unstable
        # 2. If all the rays/ways intersect it automatically means that we can halt
        #    the search as at least one of the ways is leading to the top row
        #    (this is especially important for the cases where the whole grid is
        #    filled with the bricks -- we do not want to BFS WHOLE grid on each hit)

        def is_valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def neighbors(row, col):
            return [
                (row - 1, col),
                (row + 1, col),
                (row, col - 1),
                (row, col + 1)
            ]

        def populate_transitive_adjacency(color_adjacency):
            for color in list(color_adjacency):
                for adjacent_color in list(color_adjacency[color]):
                    color_adjacency[color].update(color_adjacency[adjacent_color])

        for hit_num, hit in enumerate(hits):
            hit_row, hit_col = hit

            # print('processing hit #%s' % hit_num)

            if grid[hit_row][hit_col] == 0:
                # print('  empty cell!')
                result.append(0)
                continue

            grid[hit_row][hit_col] = 0

            # contains ((row, col), color) tuples
            queue = deque()
            # color to amount of bricks of given color in queue
            # this is needed to detect that given color is fully processed
            queue_color_counts = dict()
            color_gen = iter(num for num in range(4))
            color_stability = {}  # color -> bool if detected stable
            color_to_bricks = dict()  # map from color to all the bricks of that color
            brick_to_color = dict()
            color_adjacency = dict()  # color -> adjacent colors
            visited = set()
            color_count = 0  # total colors in this round

            # add initial neighbor bricks to the queue
            for neighbor_row, neighbor_col in neighbors(hit_row, hit_col):
                if not is_valid(neighbor_row, neighbor_col):
                    continue
                if not grid[neighbor_row][neighbor_col]:
                    continue
                neighbor = (neighbor_row, neighbor_col)
                color = next(color_gen)
                color_stability[color] = None  # meaning unknown
                color_to_bricks[color] = {neighbor}
                brick_to_color[neighbor] = color
                color_adjacency[color] = {color}
                queue.append((neighbor, color))
                queue_color_counts[color] = 1
                color_count += 1

            # to be able to control results from within the loop
            # (optimizations cases)
            handled = False

            # run the BFS maintaining colors and handling intersections
            while queue:
                brick, color = queue.popleft()
                queue_color_counts[color] -= 1

                if brick in visited:
                    continue

                # if color is known to be stable, no need to check it anymore
                if color_stability[color]:
                    continue

                visited.add(brick)

                if brick[0] == 0:
                    color_stability[color] = True

                for neighbor in neighbors(*brick):
                    if not is_valid(*neighbor):
                        continue

                    if not grid[neighbor[0]][neighbor[1]]:
                        continue

                    if neighbor in brick_to_color:
                        # already colored -> update adjacency
                        neighbor_color = brick_to_color[neighbor]

                        if neighbor_color not in color_adjacency[color]:
                            color_adjacency[color].add(neighbor_color)
                            color_adjacency[neighbor_color].add(color)
                            populate_transitive_adjacency(color_adjacency)
                    else:
                        # color uncolored
                        color_to_bricks[color].add(neighbor)
                        brick_to_color[neighbor] = color
                        neighbor_color = color

                    queue.append((neighbor, neighbor_color))
                    queue_color_counts[neighbor_color] += 1

                # optimization: detect the case where color tracing is completed
                # if there are N colors and N-1 are detected to be unstable then
                # the leftover color can be deduced stable
                if queue_color_counts[color] == 0 and color_stability[color] is None:
                    adjacent_colors = color_adjacency[color] - {color}  # without self

                    if any(
                            color_stability[adjacent_color] is None or color_stability[adjacent_color] == True
                            for adjacent_color in adjacent_colors):
                        # unable to deduce in this case
                        continue

                    # print(' color %s is unstable!' % color)
                    color_stability[color] = False
                    unstable_colors = set(
                        color for color in color_stability if color_stability[color] is False)
                    if len(unstable_colors) == color_count - 1:
                        deduced_stable = next(iter(set(color_stability) - unstable_colors))
                        # print('leftover color %s deduced stable', deduced_stable)
                        color_stability[deduced_stable] = True

                # optimization (big fill factor):
                # if all colors are adjacent it means that there are no unstable colors
                # because at least one color is stable
                # IMPORTANT: this optimization only applies there are more than
                # one "colors
                if color_count > 1 and len(color_adjacency[0]) == color_count:
                    # print('early full stability detection! visited: %s' % len(visited))
                    result.append(0)
                    handled = True
                    break

            # print('  visited: %s' % len(visited))

            if handled:
                continue

            # remove all the bricks which correspond to unstable colors
            # (considering adjacency)
            fallen = 0
            for color in color_stability:
                is_stable = (
                    any(color_stability[adjacent_color]
                    for adjacent_color in color_adjacency[color]))

                if not is_stable:
                    for brick in color_to_bricks[color]:
                        grid[brick[0]][brick[1]] = 0
                        fallen += 1

            result.append(fallen)

        return result


if __name__ == '__main__':
    x = Solution()
    # print(x.hitBricks([[1, 0, 0, 0], [1, 1, 1, 0]], hits=[[1, 0]]))
    # print(x.hitBricks([[1, 0, 0, 0], [1, 1, 0, 0]], hits=[[1, 1], [1, 0]]))
    # print(x.hitBricks([[1], [1], [1], [1], [1]], [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]))
    # print(x.hitBricks([[1, 0, 1], [1, 1, 1]], [[0, 0], [0, 2], [1, 1]]))
    # print(x.hitBricks([[0, 1, 1, 1, 1],   # 0
    #                    [1, 1, 1, 1, 0],   # 1
    #                    [1, 1, 1, 1, 0],   # 2
    #                    [0, 0, 1, 1, 0],   # 3
    #                    [0, 0, 1, 0, 0],   # 4
    #                    [0, 0, 1, 0, 0],   # 5
    #                    [0, 0, 0, 0, 0],   # 6
    #                    [0, 0, 0, 0, 0],   # 7
    #                    [0, 0, 0, 0, 0]],  # 8
    #                   hits=[[6, 0], [1, 0], [4, 3], [1, 2], [7, 1], [6, 3], [5, 2], [5, 1], [2, 4], [4, 4], [7, 3]]))
    # print(x.hitBricks([[1, 0, 1],
    #                    [1, 1, 1]],
    #                   hits=[[0, 0], [0, 2], [1, 1]]))

    with open('input2.txt') as f:
        bricks = eval(f.readline())
        hits = eval(f.readline())
        print(x.hitBricks(bricks, hits))
