# Set 1

"""
Problem 8: Find Itinerary

Understand:
- Given:
    - A list of boarding passes represented as tuples (departure_airport, arrival_airport).
    - There are no cycles; each airport is visited only once.
- Need to:
    - Reconstruct the itinerary in the correct order.
    - Find the starting airport and list all airports in order.
- Assumptions:
    - The starting airport departs but never arrives.
    - The final destination arrives but never departs.

Plan:
- Build a mapping from departure airports to arrival airports.
- Create sets of all departures and all arrivals.
- Find the starting airport:
    - Starting airport = departures - arrivals.
- Initialize the itinerary list with the starting airport.
- While the current airport has a next destination:
    - Append the current airport to the itinerary.
    - Move to the next airport using the mapping.
- Append the final destination to the itinerary.
- Return the itinerary list.
- Complexities:
    - Time Complexity: O(n), where n is the number of boarding passes.
    - Space Complexity: O(n), for storing mappings and the itinerary.
"""

def find_itinerary(boarding_passes):
    departures_to_arrivals = {dep: arr for dep, arr in boarding_passes}
    departures = set(departures_to_arrivals.keys())
    arrivals = set(departures_to_arrivals.values())
    # Find the starting airport
    starting_airports = departures - arrivals
    if not starting_airports:
        return []  # No valid itinerary
    start = starting_airports.pop()
    itinerary = []
    current = start
    while current in departures_to_arrivals:
        itinerary.append(current)
        current = departures_to_arrivals[current]
    itinerary.append(current)  # Append the final destination
    return itinerary

# Example Usage:

boarding_passes_1 = [
    ("JFK", "ATL"),
    ("SFO", "JFK"),
    ("ATL", "ORD"),
    ("LAX", "SFO")
]

boarding_passes_2 = [
    ("LAX", "DXB"),
    ("DFW", "JFK"),
    ("LHR", "DFW"),
    ("JFK", "LAX")
]

print(find_itinerary(boarding_passes_1))  # Output: ['LAX', 'SFO', 'JFK', 'ATL', 'ORD']
print(find_itinerary(boarding_passes_2))  # Output: ['LHR', 'DFW', 'JFK', 'LAX', 'DXB']

# Set 2

"""
Problem 8: Copying Seating Arrangements

Understand:
- Given:
    - A graph representing seating arrangements, where each Node has a value (celebrity's name) and a list of neighbors (adjacent seats).
- Need to:
    - Make a deep copy (clone) of the graph.
- Constraints:
    - Each Node is unique.
    - Need to copy both nodes and edges.
- Testing:
    - Provided a function `compare_graphs()` to test if the copy is correct.

Plan:
- Use DFS or BFS to traverse the graph.
- Maintain a mapping from original nodes to their copies to avoid cycles and duplicate nodes.
- For each node:
    - Create a copy of the node.
    - Recursively copy its neighbors.
- Return the copy of the starting node.
- Complexities:
    - Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
    - Space Complexity: O(N), for the mapping and recursion stack.
"""

class Node():
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Function to test if two seating arrangements (graphs) are identical
def compare_graphs(node1, node2, visited=None):
    if visited is None:
        visited = set()
    if node1.val != node2.val:
        return False
    visited.add(node1)
    if len(node1.neighbors) != len(node2.neighbors):
        return False
    for n1, n2 in zip(node1.neighbors, node2.neighbors):
        if n1 not in visited:
            if not compare_graphs(n1, n2, visited):
                return False
    return True

def copy_seating(seat):
    old_to_new = {}

    def clone(node):
        if node in old_to_new:
            return old_to_new[node]
        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(clone(neighbor))
        return copy

    return clone(seat)

# Example Usage:

# 'arrangement'

lily = Node("Lily Gladstone")
mark = Node("Mark Ruffalo")
cillian = Node("Cillian Murphy")
danielle = Node("Danielle Brooks")
lily.neighbors.extend([mark, danielle])
mark.neighbors.extend([lily, cillian])
cillian.neighbors.extend([danielle, mark])
danielle.neighbors.extend([lily, cillian])

copy = copy_seating(lily)
print(compare_graphs(lily, copy))  # Expected Output: True

# Advanced Set 1

"""
Problem 8: Number of Airline Regions

Understand:
- Given:
    - An n x n adjacency matrix `is_connected`, where `is_connected[i][j] = 1` if there is a direct flight between airports i and j.
- Need to:
    - Find the number of connected components (regions) in the graph.
- Assumptions:
    - The graph is undirected since flights are bidirectional.
    - Airports are labeled from 0 to n-1.

Plan:
- Use DFS or BFS to traverse the graph.
- Keep track of visited airports.
- For each airport:
    - If not visited, perform DFS/BFS starting from that airport.
    - Increment the count of regions.
- Complexities:
    - Time Complexity: O(n^2), since we might check each edge.
    - Space Complexity: O(n), for the visited array.
"""

def num_airline_regions(is_connected):
    n = len(is_connected)
    visited = [False] * n
    count = 0

    def dfs(i):
        for j in range(n):
            if is_connected[i][j] == 1 and not visited[j]:
                visited[j] = True
                dfs(j)

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1

    return count

# Example Usage:

is_connected1 = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]

is_connected2 = [
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 0],
    [1, 0, 0, 1]
]

print(num_airline_regions(is_connected1))  # Output: 2
print(num_airline_regions(is_connected2))  # Output: 2

