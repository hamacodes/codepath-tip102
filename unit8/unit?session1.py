"""
Set 1

Understand:
- We have a binary tree where each node represents a flower.
- We need to search for a specific flower in the tree and return True if it's found, and False if it's not.
- We should consider time complexity, assuming the tree is balanced.

Plan:
- We can use Depth-First Search (DFS), either recursively or iteratively, to traverse the tree.
- Check each node's value to see if it matches the target flower.
- If we find the flower, we return True immediately; otherwise, we continue searching.
- If we traverse the entire tree without finding the flower, return False.
"""
# Implement:
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_flower(root, flower):
    # Base case: if root is None, we've reached the end of a path without finding the flower
    if root is None:
        return False
    
    # If the current node's value matches the flower, return True
    if root.val == flower:
        return True
    
    # Recursively check left and right subtrees
    return find_flower(root.left, flower) or find_flower(root.right, flower)

# Example usage
flower_field = TreeNode("Rose", 
                        TreeNode("Lily", TreeNode("Orchid"), TreeNode("Lilac")),
                        TreeNode("Daisy", None, TreeNode("Dahlia")))

print(find_flower(flower_field, "Lilac"))  # Expected output: True
print(find_flower(flower_field, "Hibiscus"))  # Expected output: False

"""
Set 2

Understand:
- We are given a binary tree where each node represents a layer in the ocean.
- Our goal is to determine the depth (or height) of the tree, which is the longest path from the root to any leaf node.
- In this context, the depth is the number of nodes on the longest path from the root to a leaf node.

Plan:
- We can use a recursive approach to traverse the tree.
- For each node, calculate the depth of the left and right subtrees.
- The depth of the current node will be 1 (for the node itself) plus the maximum depth of its left or right subtree.
- The base case occurs when a node is None (no children), at which point we return 0.

Time Complexity:
- Since we visit each node once to calculate the maximum depth, the time complexity is O(n), where n is the number of nodes in the tree.
- For a balanced binary tree, the recursion depth will be O(log n) due to the logarithmic height of the tree.
"""
# Implement:
def ocean_depth(root):
    # Base case: if the node is None, it contributes 0 to the depth
    if root is None:
        return 0
    
    # Recursive call to calculate the depth of left and right subtrees
    left_depth = ocean_depth(root.left)
    right_depth = ocean_depth(root.right)
    
    # Current depth is 1 + max depth of left or right subtree
    return 1 + max(left_depth, right_depth)

# Example usage
ocean = TreeNode("Sunlight", 
                 TreeNode("Twilight", 
                          TreeNode("Abyss", 
                                   TreeNode("Trenches")), TreeNode("Anglerfish")),
                 TreeNode("Squid", TreeNode("Giant Squid")))

tidal_zones = TreeNode("Spray Zone", 
                       TreeNode("Beach"), 
                       TreeNode("High Tide", 
                                TreeNode("Middle Tide", None, TreeNode("Low Tide"))))

print(ocean_depth(ocean))        # Expected output: 4
print(ocean_depth(tidal_zones))  # Expected output: 4

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

