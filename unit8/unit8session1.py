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
- We are given two binary trees and need to check if they have identical structures and values.
- Identical trees have:
  - The same value at the corresponding nodes.
  - The same structure, meaning that each left and right child pair is mirrored between the two trees.
- If any difference in structure or value is found, we return False; otherwise, return True.

Plan:
1. Recursive Comparison:
   - For each node pair (one from each tree), check if both nodes are None. If so, they're identical at this level.
   - If only one node is None, the trees are not identical.
   - If both nodes exist, check if their values are the same.
   - Recursively compare the left and right children of each node pair.
2. Base Cases:
   - If both nodes are None, they match, so return True.
   - If one node is None and the other is not, return False.
   - If node values differ, return False.
3. Recursive Calls:
   - Call the function recursively on left and right children, combining the results with logical "and".

Time Complexity:
- Each node in each tree is visited once, so the time complexity is O(n), where n is the number of nodes in the trees.

Space Complexity:
- Since recursion reaches the depth of the tree, the space complexity is O(h), where h is the height of the tree.
- In a balanced binary tree, h is O(log n).

"""
# Implement:
def is_identical(root1, root2):
    # Base cases
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    
    # Recursive case: check left and right subtrees
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

# Example usage
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))  # Expected output: True
print(is_identical(root3, root4))  # Expected output: False

"""
Advanced Set 2

Understand:
- We are given a binary tree and need to check if it is symmetric around its center.
- A tree is symmetric if its left and right subtrees are mirror images of each other.
- To be symmetric:
  - The root's left and right subtrees must have the same structure and node values, but mirrored.
  - Each subtree's left child should match the other subtree's right child, and vice versa.

Plan:
1. Define a helper function `is_mirror` to recursively compare two subtrees for mirror symmetry.
2. For each pair of nodes (one from each subtree):
   - If both nodes are None, they are symmetric at this level.
   - If only one node is None, they are not symmetric.
   - If both nodes exist, check if their values are the same.
   - Recursively check if:
     - The left child of one subtree is symmetric to the right child of the other.
     - The right child of one subtree is symmetric to the left child of the other.
3. Call `is_mirror` on the root's left and right children to check symmetry.

Time Complexity:
- We visit each node once, so the time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The recursion depth is O(h), where h is the height of the tree. For a balanced tree, h is O(log n).

"""
# Implement:
def is_symmetric(root):
    # Helper function to check if two subtrees are mirrors of each other
    def is_mirror(left, right):
        # Base case: both nodes are None
        if left is None and right is None:
            return True
        # If only one node is None, they aren't symmetric
        if left is None or right is None:
            return False
        # Check if current nodes are equal and their children are mirrors of each other
        return (left.val == right.val 
                and is_mirror(left.left, right.right) 
                and is_mirror(left.right, right.left))
    
    # Start recursion with the left and right children of the root
    return is_mirror(root.left, root.right) if root else True

# Example usage
coral1 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                  TreeNode('B', TreeNode('D'), TreeNode('C')))

coral2 = TreeNode('A', 
                  TreeNode('B', TreeNode('C'), TreeNode('D')), 
                  TreeNode('B', TreeNode('C'), TreeNode('D')))

print(is_symmetric(coral1))  # Expected output: True
print(is_symmetric(coral2))  # Expected output: False
