
"""
Set 1

Problem 6: Find Next Order to Fulfill Today

Understand:
- We have a binary tree where each node represents an order.
- Each level represents a different day's orders.
- Given a node `order`, we need to find the next node to fulfill on the same level.
- If `order` is the last node on its level (rightmost node), return None.

Plan:
- Perform a level-order traversal (BFS) to keep track of nodes at each level.
- While traversing, compare each node with the target `order`.
- When we find the target, the next node in the queue (if it's on the same level) is the next order.
- Time Complexity: O(n), where n is the number of nodes.
- Space Complexity: O(n), due to the queue used for BFS.
"""

from collections import deque

class TreeNode():
     def __init__(self, order, left=None, right=None):
        self.val = order
        self.left = left
        self.right = right

def find_next_order(order_tree, order):
    if not order_tree:
        return None
    
    queue = deque()
    queue.append(order_tree)
    
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if node == order:
                if i == level_size - 1:
                    return None  # Last node on this level
                else:
                    return queue[0]  # Next node on the same level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return None

# Tests
# Example Usage:

"""
        Cupcakes
       /       \ 
   Macaron     Cookies      
        \      /      \
      Cake   Eclair   Croissant
"""

cupcakes = TreeNode("Cupcakes")
macaron = TreeNode("Macaron")
cookies = TreeNode("Cookies")
cake = TreeNode("Cake")
eclair = TreeNode("Eclair")
croissant = TreeNode("Croissant")

cupcakes.left, cupcakes.right = macaron, cookies
macaron.right = cake
cookies.left, cookies.right = eclair, croissant

next_order1 = find_next_order(cupcakes, cake)
next_order2 = find_next_order(cupcakes, cookies)

print(next_order1.val if next_order1 else None)  # Expected: Eclair
print(next_order2.val if next_order2 else None)  # Expected: None

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

