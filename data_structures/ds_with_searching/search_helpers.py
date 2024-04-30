offsets = {
    "up": (-1, 0),
    "right": (0, 1),
    "down": (1, 0),
    "left": (0, -1),
}

BLOCKED_SQUARE_VAL = 'X'

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != BLOCKED_SQUARE_VAL

def read_matrix(filename):
    with open('./matrix.txt') as f:
        # does not handle line that just has \n
        matrix = [[ch for ch in line.strip('\n')] for line in f]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(''.join(row))

def is_square(matrix):
    top_row_length = len(matrix[0])
    for row in matrix:
        if len(row) != top_row_length:
            return False
    return True

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path
