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
- We are given a list of integers
- we are to write a function merge_sort_playlist() to sort the list
- we return the sorted list
- we are to use the merge sort algorithm

Plan:
- we define a helper function that takes two lists as arguments
- we iterate through the lists using pointers
- we compare the elements at the pointers
- we add the smaller element to the merged list
- we increment the pointer of the list with the smaller element
- we add the remaining elements from
- we return the merged list
"""
# Implement:
def merge_sort_helper(left_arr, right_arr):
    merged = []
    i = j = 0
    
    # Use pointers to iterate through left_arr and right_arr
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
    
    # Add any remaining elements from the left and right halves
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])
    
    return merged

def merge_sort_playlist(playlist):
    # Base Case: If the list has 1 or 0 elements, it's already sorted
    if len(playlist) <= 1:
        return playlist
    
    # Recursive Cases: Divide the list into two halves
    mid = len(playlist) // 2
    left_half = merge_sort_playlist(playlist[:mid])
    right_half = merge_sort_playlist(playlist[mid:])
    
    # Use the helper to merge the sorted halves
    return merge_sort_helper(left_half, right_half)

# Example Usage
print(merge_sort_playlist(["Formation", "Crazy in Love", "Halo"]))  
# Expected: ['Crazy in Love', 'Formation', 'Halo']

print(merge_sort_playlist(["Single Ladies", "Love on Top", "Irreplaceable"]))  
# Expected: ['Irreplaceable', 'Love on Top', 'Single Ladies']


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

