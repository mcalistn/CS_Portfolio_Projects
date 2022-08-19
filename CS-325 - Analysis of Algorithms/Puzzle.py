# Nathan McAlister
# Due Date - 8/1/22
# Homework 6 - Given a 2-D puzzle of size MxN, that has N rows and M column
#              (M and N can be different), find the shortest distance between
#              two specified coordinates (source and destination),
#              using BFS, DFS, or MST to solve the problem.


# Imports
import heapq


# Outlines the shortest path between the source node and the destination
# node, in both coordinate and string format
# Inputs: previous_hop - contains a map of how to reach each node from the
#                        source node.
#         src - source node
#         dest - destination node
# Outputs: result - shortest path between the source node and the destination
#                   node, in both coordinate and string format
# Description: Takes the Dijkstra's algorithm output (shortest path from the
#              source node to all other nodes) and distills the information
#              to the only include from the source node to the destination
#              node. Returns the pathway as both a collection of coordinates
#              and as a [left (L), right (R), up (U), down (D)] string
def define_path(previous_hop, src, dest):
    cord_path = [dest]
    direction = ''

    # Traverse the previous_hop dictionary find the coordinate pathway from
    # the destination node to the source node.
    while cord_path[-1] != src:
        cord_path.append(previous_hop[str(cord_path[-1])])

    # Convert coordinates from a string to a tuple
    for i in range(len(cord_path)):
        cord_path[i] = tuple(map(int, cord_path[i][1:-1].split(', ')))

    # Reverse coordinates
    cord_path = cord_path[::-1]

    # Convert coordinates to string representation of the path
    for j in range(1, len(cord_path)):
        if cord_path[j - 1][0] - cord_path[j][0] > 0:
            direction += 'U'
        if cord_path[j - 1][0] - cord_path[j][0] < 0:
            direction += 'D'
        if cord_path[j - 1][1] - cord_path[j][1] > 0:
            direction += 'L'
        if cord_path[j - 1][1] - cord_path[j][1] < 0:
            direction += 'R'

    result = (cord_path, direction)
    return result


# Calculates the shortest path to each node using Dijkstra's algorithm
# Inputs: graph - graphical representation of the puzzle
#         src - source node
#         dest - destination node
# Outputs: previous_hop - contains a map of how to reach each node from the
#                         source node.
# Description: Uses Dijkstra's algorithm to find the shortest path between 
#              the source node and the current node. For the current 
#              node, records the location of the node that brought the 
#              shortest path to the current node. 
def calculate_Dijkstra(graph, src, dest):
    distances = {node: float('infinity') for node in graph}
    distances[src] = 0
    pq = [(0, src)]
    previous_hop = {}

    while len(pq) > 0:
        current_distance, current_node = heapq.heappop(pq)
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time, or after we remove it from the
        # priority queue.
        if current_distance > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                # Records the location of the neighbor that has the shortest
                # path to the current node.
                previous_hop[neighbor] = current_node

    # No path exists between source and destination nodes
    if distances[dest] == float('infinity'):
        return None
    return previous_hop


# Converts the puzzle to a graph 
# Inputs: board - puzzle to be converted to a graph
# Outputs: graph - graphical representation of the puzzle
# Description: The graph is represented as a nested dictionary, in which the
#              keys are the coordinates of the current node and the values are 
#              another dictionary that contains the allowable neighbor nodes. 
def convert_puzzle_to_graph(board):
    rows = len(board)
    cols = len(board[0])
    graph = {}
    for y in range(rows):
        for x in range(cols):
            # Convert puzzle pieces with '-' to graphical nodes
            if board[y][x] == '-':
                graph["(" + str(y) + ", " + str(x) + ")"] = {}
                # Valid left neighbor
                if x - 1 >= 0 and board[y][x - 1] != "#":
                    graph["(" + str(y) + ", " + str(x) + ")"] \
                         ["(" + str(y) + ", " + str(x - 1) + ")"] = 1
                # Valid right neighbor
                if x + 1 < cols and board[y][x + 1] != "#":
                    graph["(" + str(y) + ", " + str(x) + ")"] \
                         ["(" + str(y) + ", " + str(x + 1) + ")"] = 1
                # Valid down neighbor
                if y - 1 >= 0 and board[y - 1][x] != "#":
                    graph["(" + str(y) + ", " + str(x) + ")"] \
                         ["(" + str(y - 1) + ", " + str(x) + ")"] = 1
                # Valid up neighbor
                if y + 1 < rows and board[y + 1][x] != "#":
                    graph["(" + str(y) + ", " + str(x) + ")"] \
                         ["(" + str(y + 1) + ", " + str(x) + ")"] = 1
    return graph


def solve_puzzle(board, src, dest):
    graph = convert_puzzle_to_graph(board)
    previous_hop = calculate_Dijkstra(graph, str(src), str(dest))
    # No path exists between source and destination nodes
    if previous_hop is None:
        return None
    return define_path(previous_hop, str(src), str(dest))


if __name__ == '__main__':

    src = (0, 2)    # Source coordinate (row, col)
    dest = (2, 2)   # Destination coordinate (row, col)

    Puzzle = [['-', '-', '-', '-', '-'],
              ['-', '-', '#', '-', '-'],
              ['-', '-', '-', '-', '-'],
              ['#', '-', '#', '#', '-'],
              ['-', '#', '-', '-', '-']]

    print("\nOutput:", solve_puzzle(Puzzle, src, dest))


# References - The Dijkstra's algorithm was taken from the exploration
#              module exercise
