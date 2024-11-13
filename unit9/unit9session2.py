
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

Problem 6: Sectioning Off Cursed Zones

Understand:
- Given a binary tree `hotel`, where nodes represent rooms.
- Need to find the smallest subtree that contains all the deepest nodes.
- Deepest nodes are those with the maximum depth.
- Return the root of the smallest subtree containing all deepest nodes.

Plan:
- Use recursion to find the depth of each node.
- For each node, keep track of:
  - Its depth.
  - If its left and right subtrees contain the deepest nodes.
- The current node is the LCA (Lowest Common Ancestor) of deepest nodes if left and right depths are equal and maximum.
- Time Complexity: O(n), where n is the number of nodes.
- Space Complexity: O(h), due to recursion stack, where h is the height of the tree.
"""

def smallest_subtree_with_deepest_rooms(hotel):
    def helper(node):
        if not node:
            return (0, None)
        left_depth, left_subtree = helper(node.left)
        right_depth, right_subtree = helper(node.right)
        
        if left_depth > right_depth:
            return (left_depth + 1, left_subtree)
        elif right_depth > left_depth:
            return (right_depth + 1, right_subtree)
        else:
            return (left_depth + 1, node)
    
    return helper(hotel)[1]

# Tests
# Example Usage:

"""
         Lobby
        /     \
       /       \
      101      102
     /   \    /   \
   201  202  203  204
        /  \ 
      😱   👻
"""

rooms1 = TreeNode("Lobby")
rooms1.left = TreeNode(101)
rooms1.right = TreeNode(102)
rooms1.left.left = TreeNode(201)
rooms1.left.right = TreeNode(202)
rooms1.right.left = TreeNode(203)
rooms1.right.right = TreeNode(204)
rooms1.left.right.left = TreeNode("😱")
rooms1.left.right.right = TreeNode("👻")

"""
      Lobby
     /     \
   101     102
     \
     💀
"""

rooms2 = TreeNode("Lobby")
rooms2.left = TreeNode(101)
rooms2.right = TreeNode(102)
rooms2.left.right = TreeNode("💀")

def print_tree(root):
    # Simple BFS traversal to print tree values
    if not root:
        print([])
        return
    from collections import deque
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    print(result)

print_tree(smallest_subtree_with_deepest_rooms(rooms1))  # Expected: [202, '😱', '👻']
print_tree(smallest_subtree_with_deepest_rooms(rooms2))  # Expected: ['💀']


"""
Advanced Set 1

Problem 6: Vertical Bakery Display

Understand:
- Given a binary tree representing bakery items.
- Need to perform vertical order traversal.
- Items in the same column are grouped together.
- If items are in the same row and column, they are listed from left to right.

Plan:
- Use BFS traversal to assign coordinates to each node:
  - Horizontal distance (hd): column index.
  - Level: row index.
- Use a dictionary to map hd to list of (level, value).
- After traversal, sort the dictionary keys (columns), and for each column, sort the items by level and left-to-right order.
- Time Complexity:
  - O(n log n) due to sorting columns and items within columns.
- Space Complexity:
  - O(n), storing all nodes.
- For balanced and unbalanced trees:
  - Time and space complexities remain the same, but the height affects the maximum depth of recursion.
"""

def vertical_inventory_display(root):
    from collections import defaultdict, deque
    
    if not root:
        return []
    
    node_dict = defaultdict(list)
    queue = deque([(root, 0, 0)])  # Node, hd, level
    
    while queue:
        node, hd, level = queue.popleft()
        node_dict[hd].append((level, node.val))
        
        if node.left:
            queue.append((node.left, hd - 1, level + 1))
        if node.right:
            queue.append((node.right, hd + 1, level + 1))
    
    result = []
    for hd in sorted(node_dict.keys()):
        # Sort items by level and left-to-right order
        column = [val for level, val in sorted(node_dict[hd], key=lambda x: (x[0]))]
        result.append(column)
    
    return result

# Tests
# Example Usage 1:

"""
         Bread
       /       \
   Croissant    Donut
                /   \
             Bagel Tart
"""

inventory_items = ["Bread", "Croissant", "Donut", None, None, "Bagel", "Tart"]
inventory1 = build_tree(inventory_items)

print(vertical_inventory_display(inventory1))  
# Expected: [['Croissant'], ['Bread', 'Bagel'], ['Donut'], ['Tart']]

# Example Usage 2:

"""
         Bread
       /       \
   Croissant    Donut
   /    \        /   \
Muffin  Scone Bagel Tart
        /       \
      Pie     Cake
"""

inventory_items = ["Bread", "Croissant", "Donut", "Muffin", "Scone", "Bagel", "Tart", None, None, "Pie", None, "Cake"]
inventory2 = build_tree(inventory_items)

print(vertical_inventory_display(inventory2))  
# Expected: [['Muffin'], ['Croissant', 'Pie'], ['Bread', 'Scone', 'Bagel'], ['Donut', 'Cake'], ['Tart']]

"""
Advanced Set 2

Understand:


Plan:

"""
# Implement:

