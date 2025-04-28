import math

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

# Manhattan heuristic function
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_fixed():
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]

    start = (0, 0)
    goal = (3, 3)

    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)

        if current_node == goal_node:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        neighbors = [(0, -1), (0, 1), (-1, 0), (1, 0),
                     (-1, -1), (-1, 1), (1, -1), (1, 1)]

        for move in neighbors:
            node_position = (current_node.position[0] + move[0],
                             current_node.position[1] + move[1])

            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                if grid[node_position[0]][node_position[1]] == 0:
                    successor = Node(node_position, current_node)

                    successor.g = current_node.g + 1
                    successor.h = heuristic(successor.position, goal_node.position)
                    successor.f = successor.g + successor.h

                    if any(open_node for open_node in open_list if successor == open_node and successor.f >= open_node.f):
                        continue
                    if any(closed_node for closed_node in closed_list if successor == closed_node and successor.f >= closed_node.f):
                        continue

                    open_list.append(successor)

        closed_list.append(current_node)

    return None

# Run it!
if __name__ == "__main__":
    path = astar_fixed()
    print("Found Path:", path)
