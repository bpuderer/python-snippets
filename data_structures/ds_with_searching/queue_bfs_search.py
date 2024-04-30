from my_queue import Queue
from search_helpers import offsets, is_legal_pos, read_matrix, print_matrix, is_square, get_path


def bfs(maze, start, goal):
    # goes up, right, down, left...clockwise when discovering neighbors
    q = Queue()
    q.enqueue(start)
    predecessors = {start: None}

    while not q.is_empty():
        current_cell = q.dequeue()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                # if within boundaries of maze, not a blocked position and not already discovered
                q.enqueue(neighbor)
                predecessors[neighbor] = current_cell
    return None


if __name__== "__main__":
    my_matrix = read_matrix('./matrix.txt')
    print_matrix(my_matrix)
    if is_square(my_matrix):
        print(bfs(my_matrix, (0,0), (3,3)))
