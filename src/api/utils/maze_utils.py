from collections import deque


def mario_save_princess(N, grid):

    # make sure input is valid
    if not is_valid_input(N, grid):
        return {'error_flag': True, 'paths':[]}

    # parse input
    grid_matrix = [list(sub) for sub in grid]

    # extract locations of mario and princess
    mario = [(index, row.index('m')) for index, row in enumerate(grid_matrix) if 'm' in row][0]
    princess = [(index, row.index('p')) for index, row in enumerate(grid_matrix) if 'p' in row][0]

    # search for paths
    paths = find_paths(grid_matrix, N, mario,princess)
    return {'error_flag': False, 'paths': paths}


def is_valid_input(N, grid):
    # check there is N rows
    if len(grid) != N:
        return False
    # check each row is length of N
    for s in grid:
        if len(s) != N:
            return False
    grid_string = ''.join(grid)
    allowed = '-mxp'
    # check there is only allowed chars
    if not all(c in allowed for c in grid_string):
        return False
    # check there is exactly one mario and one princess
    if grid_string.count('m') != 1 or grid_string.count('p') != 1:
        return False
    return True


def find_paths(grid_matrix, N, mario, princess):

    directions = {(1, 0): 'DOWN', (0, 1): 'RIGHT', (0, -1): 'LEFT', (-1, 0): 'UP'}

    q = deque()
    q.append((mario[0], mario[1], 0, []))  # x, y, distance, path
    visited = set()
    all_paths = []

    while len(q) > 0:
        x, y, dist, path = q.popleft()
        if x == princess[0] and y == princess[1]:
            all_paths.append(path)

        if grid_matrix[x][y] == 'x': # obstacle
            continue

        for direction in directions.keys():
            # move in one of the directions
            nx, ny = x + direction[0], y + direction[1]
            # check it is a non-visited cell inside the grid
            if 0 <= nx < N and 0 <= ny < N and (nx, ny) not in visited:
                q.append((nx, ny, dist + 1, path + [directions.get(direction)]))
                visited.add((x, y))
    return all_paths


def test():

    # grid = ['--m','-x-','-p-']
    # N = 3
    # grid = ['---m','----','-x--', '-px-']
    grid = ['---m', '----', '--x-', '--px']
    N=4
    res = mario_save_princess(N, grid)
    print(res)


# [['DOWN', 'LEFT', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
# ['LEFT', 'DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
# ['LEFT', 'LEFT', 'DOWN', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
# ['LEFT', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT']]

# ['DOWN', 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'],
# ['LEFT', 'DOWN', 'LEFT', 'DOWN', 'DOWN', 'RIGHT'], [
# 'LEFT', 'LEFT', 'DOWN', 'DOWN', 'DOWN', 'RIGHT']]

