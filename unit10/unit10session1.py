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

"""
Set 2

Understand:


Plan:

"""
# Implement:


"""
Advanced Set 1

Understand:


Plan:

"""
# Implement:

"""
Advanced Set 2

Understand:


Plan:

"""
# Implement:

