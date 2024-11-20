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

