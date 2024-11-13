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

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

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


# Set 2

"""
Problem 6: Kth Spookiest Room in the Hotel

Understand:
- Given a BST where keys represent spookiness levels (1 is most spooky).
- Need to find the value (room number) of the kth spookiest room.
- Since it's a BST, in-order traversal visits nodes in ascending order of keys.

Plan:
- Perform an in-order traversal.
- Use a counter to track nodes visited.
- When counter equals k, return the current node's value.
- Time Complexity: O(n) worst-case, but average O(k + h).
- Space Complexity: O(h), where h is the tree height.
"""

def kth_spookiest(root, k):
    stack = []
    current = root
    count = 0
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        count += 1
        if count == k:
            return current.val
        current = current.right
    return None

# Tests
# Example Usage:

"""
    (3, Lobby) 
   /         \
(1, 101)   (4, 102)
     \
     (2, 201)
"""

rooms = [(3, "Lobby"), (1, 101), (4, 102), None, (2, 201)]
hotel1 = build_tree(rooms)
print(kth_spookiest(hotel1, 1))  # Expected: 101

"""
            (5, Lobby) 
            /         \
        (3, 101)   (6, 102)
        /      \
    (2, 201)  (4, 202)
    /
(1, 301)
"""

rooms = [(5, 'Lobby'), (3, 101), (6, 102), (2, 201), (4, 202), None, None, (1, 301)]
hotel2 = build_tree(rooms)
print(kth_spookiest(hotel2, 3))  # Expected: 201


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

