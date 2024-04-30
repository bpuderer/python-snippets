from stack import Stack
from search_helpers import offsets, is_legal_pos, read_matrix, print_matrix, is_square


def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}

    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None

def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path





if __name__== "__main__":
    my_matrix = read_matrix('./matrix.txt')
    print_matrix(my_matrix)
    if is_square(my_matrix):
        print(dfs(my_matrix, (0,0), (3,3)))
