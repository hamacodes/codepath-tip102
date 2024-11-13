# Set 1

"""
Problem 6: Icing Cupcakes in Zigzag Order

Understand:
- You have a binary tree representing cupcakes.
- Need to traverse the tree in zigzag (left to right, then right to left) order.
- Return a list of cupcake flavors in the order they are iced.

Plan:
- Use a modified breadth-first search (BFS) traversal.
- Use a deque to efficiently add nodes from both ends.
- Use a flag `left_to_right` to alternate traversal direction at each level.
- Collect node values at each level accordingly.
- Time Complexity: O(n), where n is the number of nodes.
- Space Complexity: O(n), due to the deque and result list.
"""

from collections import deque

def zigzag_icing_order(cupcakes):
    if not cupcakes:
        return []
    
    result = []
    queue = deque()
    queue.append(cupcakes)
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        level_nodes = deque()
        
        for _ in range(level_size):
            node = queue.popleft()
            if left_to_right:
                level_nodes.append(node.val)
            else:
                level_nodes.appendleft(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.extend(level_nodes)
        left_to_right = not left_to_right
    
    return result

# Tests
# Example Usage:

"""
            Chocolate
           /         \
        Vanilla       Lemon
       /              /    \
    Strawberry   Hazelnut   Red Velvet   
"""

# Assuming build_tree() function is defined to build the tree
flavors = ["Chocolate", "Vanilla", "Lemon", "Strawberry", None, "Hazelnut", "Red Velvet"]
cupcakes = build_tree(flavors)
print(zigzag_icing_order(cupcakes))  # Expected: ['Chocolate', 'Lemon', 'Vanilla', 'Strawberry', 'Hazelnut', 'Red Velvet']


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

