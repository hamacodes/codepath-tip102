# Set 1

"""
Problem 8: Get Flight Itinerary

Understand:
- Given:
    - An adjacency dictionary `flights` where each key is an airport, and its value is a list of airports directly reachable from it.
    - A `source` airport and a `dest` airport.
- Need to:
    - Find any flight path from `source` to `dest`.
    - Return the path as a list of airports.
- Constraints:
    - There may be cycles in the graph.
    - Multiple paths may exist; any valid path is acceptable.

Plan:
- Use BFS (Breadth-First Search):
    - BFS helps find the shortest path in an unweighted graph.
- Path Reconstruction:
    - Keep track of each airport's parent to reconstruct the path once `dest` is found.
- Algorithm Steps:
    - Initialize a queue and add the `source` airport.
    - Use a `visited` set to keep track of visited airports.
    - Use a `parent` dictionary to remember each airport's parent.
    - While the queue is not empty:
        - Dequeue an airport `current`.
        - If `current` is `dest`, reconstruct the path using the `parent` dictionary.
        - For each neighbor of `current`:
            - If the neighbor has not been visited:
                - Mark it as visited.
                - Set its parent to `current`.
                - Enqueue the neighbor.
- Complexities:
    - Time Complexity: O(N + E), where N is the number of airports and E is the number of flights.
    - Space Complexity: O(N), for the queue, visited set, and parent dictionary.
"""

def get_itinerary(flights, source, dest):
    from collections import deque
    visited = set()
    parent = {}
    queue = deque([source])
    visited.add(source)
    
    while queue:
        current = queue.popleft()
        if current == dest:
            # Reconstruct the path from source to dest
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return path[::-1]
        for neighbor in flights.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    return []  # No path found

# Example Usage:

flights = {
    'LAX': ['SFO'],
    'SFO': ['LAX', 'ORD', 'ERW'],
    'ERW': ['SFO', 'ORD'],
    'ORD': ['ERW', 'SFO', 'MIA'],
    'MIA': ['ORD']
}

print(get_itinerary(flights, 'LAX', 'MIA'))  # Output: ['LAX', 'SFO', 'ORD', 'MIA'] or another valid path

# Set 2

"""
Problem 8: Celebrity Feuds

Understand:
- Given:
    - An integer `n` representing the number of celebrities labeled from 1 to n.
    - A list `dislikes`, where each element `[a, b]` indicates that celebrity `a` does not get along with celebrity `b`.
- Need to:
    - Determine if it's possible to split the celebrities into two groups such that no two celebrities in the same group dislike each other.
    - Return `True` if possible, `False` otherwise.
- Constraints:
    - The dislike relationship is mutual.
    - This is equivalent to checking if the graph is bipartite.

Plan:
- Graph Representation:
    - Build an undirected graph using an adjacency list.
- Use Graph Coloring:
    - Attempt to color the graph using two colors (0 and 1) without assigning the same color to adjacent nodes.
- Algorithm Steps:
    - Initialize an empty color dictionary.
    - For each celebrity from 1 to n:
        - If the celebrity is uncolored, perform BFS:
            - Assign a color to the celebrity.
            - For each neighbor:
                - If the neighbor is uncolored, assign the opposite color.
                - If the neighbor is colored and has the same color, return `False`.
    - If all celebrities can be colored without conflict, return `True`.
- Complexities:
    - Time Complexity: O(N + E), where N is the number of celebrities and E is the number of dislikes.
    - Space Complexity: O(N + E), for the adjacency list and color mapping.
"""

def can_split(n, dislikes):
    from collections import defaultdict, deque
    graph = defaultdict(list)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)  # Dislikes are mutual
    
    color = {}
    
    for celebrity in range(1, n + 1):
        if celebrity not in color:
            queue = deque([celebrity])
            color[celebrity] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True

# Example Usage:

dislikes_1 = [[1, 2], [1, 3], [2, 4]]
dislikes_2 = [[1, 2], [1, 3], [2, 3]]

print(can_split(4, dislikes_1))  # Output: True
print(can_split(3, dislikes_2))  # Output: False

