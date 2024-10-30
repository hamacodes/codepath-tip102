"""
Set 1

Understand:
- We are given a 2D matrix of rooms
- each room has a value
- we are to write a function find_treasure() to find the treasure in the matrix
- we return the coordinates of the treasure
- the matrix is sorted in ascending order
- the matrix is a square matrix
- the treasure is a single value
- the matrix is a 2D list
- the treasure is an integer
- the coordinates are a tuple
- the coordinates are 0-indexed
- we are to use binary search to find the treasure

Plan:
- check if the submatrix is out of bounds
- find the middle of the current search area
- if the middle value is the treasure, return the coordinates
- if the middle value is less than the treasure, explore the bottom-right submatrix, bottom submatrix, and right submatrix
- if the middle value is greater than the treasure, explore the top-left submatrix, top submatrix, and left submatrix
- return
"""
# Implement:
def find_treasure(matrix, treasure):
    def search(start_row, end_row, start_col, end_col):
        # Base case: If the submatrix is out of bounds
        if start_row > end_row or start_col > end_col:
            return -1, -1
        
        # Find the middle of the current search area
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        mid_value = matrix[mid_row][mid_col]
        
        if mid_value == treasure:
            return mid_row, mid_col  # Treasure found
        elif mid_value < treasure:
            # Explore bottom-right submatrix, bottom submatrix, and right submatrix
            result = search(mid_row + 1, end_row, start_col, end_col)  # Bottom half
            if result != (-1, -1):
                return result
            result = search(start_row, end_row, mid_col + 1, end_col)  # Right half
            if result != (-1, -1):
                return result
        else:
            # Explore top-left submatrix, top submatrix, and left submatrix
            result = search(start_row, mid_row - 1, start_col, end_col)  # Top half
            if result != (-1, -1):
                return result
            result = search(start_row, end_row, start_col, mid_col - 1)  # Left half
            if result != (-1, -1):
                return result
        
        return -1, -1

    # Start the search from the entire matrix
    return search(0, len(matrix) - 1, 0, len(matrix[0]) - 1)

# Example Usage
rooms = [
    [1, 4, 7, 11],
    [8, 9, 10, 20],
    [11, 12, 17, 30],
    [18, 21, 23, 40]
]

print(find_treasure(rooms, 17))  # Expected: (2, 2)
print(find_treasure(rooms, 5))   # Expected: (-1, -1)


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

