from priority_queue import PriorityQueue
from search_helpers import offsets, is_legal_pos, read_matrix, print_matrix, is_square


def manhattan_distance(a, b):
    """
    Calculates Manhattan distance used to calculate f-value for priority
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def astar(maze, start, goal):
    pq = PriorityQueue()
    # priority does not matter when only item on pq. this will always be returned with first get
    pq.put(start, 0)
    g_vals = {start: 0}
    predecessors = {start: None}

    while not pq.is_empty():
        current_cell = pq.get()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbor) and neighbor not in predecessors:
                # neighbor is always 1 away from current so don't need to calculate using heuristic function
                # can only assume that because it's a unweighted graph
                g_val = g_vals[current_cell] + 1
                g_vals[neighbor] = g_val
                f_val = g_val + manhattan_distance(neighbor, goal)
                pq.put(neighbor, f_val)
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
        print(astar(my_matrix, (0,0), (3,3)))
