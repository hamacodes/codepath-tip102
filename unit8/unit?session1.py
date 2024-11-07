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

