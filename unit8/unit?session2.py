"""
Set 1

Understand:
- We are given a Binary Search Tree (BST) where each node represents a plant in a houseplant collection.
- Our task is to remove a node containing a specified plant name (value) and return the updated tree.
- Plants are stored alphabetically, so we can leverage the BST properties for efficient searching and removal.
- If the node has:
  - No children, we simply remove the node.
  - One child, we replace the node with its child.
  - Two children, we replace the node with its inorder predecessor (rightmost node in the left subtree).
- The pseudocode steps are provided, which we will follow for implementation.

Plan:
1. Search for the node with the specified `name` in the BST:
   - Use the BST properties: if the target name is smaller, move to the left child; if larger, move to the right.
2. Node Removal Cases:
   - **No children**: Set the parent's pointer to None to remove the node.
   - **One child**: Replace the node with its only child.
   - **Two children**: 
     - Find the inorder predecessor (rightmost node in the left subtree).
     - Replace the target node's value with the inorder predecessor's value.
     - Remove the inorder predecessor.
3. Return the root of the updated tree.

Time Complexity:
- For a balanced BST, the time complexity for finding and removing a node is O(log n), where n is the number of nodes.
- In the case of two children, finding the inorder predecessor takes O(log n) in a balanced tree.

"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# Implement:
def remove_plant(collection, name):
    # Helper function to find the rightmost node in a subtree (inorder predecessor)
    def find_max(node):
        while node.right:
            node = node.right
        return node

    # Recursive function to remove the plant
    def remove_node(root, name):
        if root is None:
            return None
        
        # Search for the node to delete
        if name < root.val:
            root.left = remove_node(root.left, name)
        elif name > root.val:
            root.right = remove_node(root.right, name)
        else:
            # Node found, proceed with deletion cases

            # Case 1: Node has no children
            if root.left is None and root.right is None:
                return None
            
            # Case 2: Node has one child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            # Case 3: Node has two children
            # Find the inorder predecessor (maximum in the left subtree)
            pred = find_max(root.left)
            # Replace root value with predecessor's value
            root.val = pred.val
            # Remove the predecessor node
            root.left = remove_node(root.left, pred.val)
        
        return root

    # Call the remove function starting from the root
    return remove_node(collection, name)

# Example usage
def build_tree(values):
    if not values:
        return None
    
    def insert_level_order(index):
        if index >= len(values) or values[index] is None:
            return None
        root = TreeNode(values[index])
        root.left = insert_level_order(2 * index + 1)
        root.right = insert_level_order(2 * index + 2)
        return root

    return insert_level_order(0)

def print_tree(root):
    if root is None:
        return []
    
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values for better output readability
    while result and result[-1] is None:
        result.pop()
    return result

# Construct example tree
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Test the remove_plant function
print(print_tree(remove_plant(collection, "Pilea")))  # Expected output: ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']

"""
Set 2

Understand:
- We have a Binary Search Tree (BST) where each node represents a pearl of a specific size.
- We need to find the minimum difference between the sizes of any two different pearls.
- In a BST, an inorder traversal provides a sorted list of values, so the minimum difference will be between two adjacent nodes in the inorder traversal.

Plan:
1. Perform an inorder traversal of the BST:
   - This will provide a sorted list of pearl sizes in ascending order.
2. Calculate the minimum difference:
   - Initialize a variable to store the minimum difference.
   - Iterate through the sorted list and find the difference between each pair of adjacent values.
   - Update the minimum difference if a smaller difference is found.
3. Return the minimum difference.

Time Complexity:
- The inorder traversal of the BST takes O(n) time, where n is the number of nodes, as we visit each node once.
- The calculation of the minimum difference also takes O(n).
- Therefore, the overall time complexity is O(n).

"""
# Implement:
class Pearl:
    def __init__(self, size=0, left=None, right=None):
        self.val = size
        self.left = left
        self.right = right

def min_diff_in_pearl_sizes(pearls):
    # Helper function to perform inorder traversal
    def inorder(node):
        if node is None:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    # Perform inorder traversal to get a sorted list of pearl sizes
    sorted_sizes = inorder(pearls)
    
    # Initialize minimum difference as a large number
    min_diff = float('inf')
    
    # Calculate the minimum difference between adjacent sizes
    for i in range(1, len(sorted_sizes)):
        min_diff = min(min_diff, sorted_sizes[i] - sorted_sizes[i - 1])
    
    return min_diff

# Helper function to build tree from list (for testing purposes)
def build_tree(values):
    if not values:
        return None
    
    def insert_level_order(index):
        if index >= len(values) or values[index] is None:
            return None
        root = Pearl(values[index])
        root.left = insert_level_order(2 * index + 1)
        root.right = insert_level_order(2 * index + 2)
        return root

    return insert_level_order(0)

# Example usage
values = [4, 2, 6, 1, 3, None, 8]
pearls = build_tree(values)
print(min_diff_in_pearl_sizes(pearls))  # Expected output: 1

"""
Advanced Set 1

Understand:
- We are given a binary tree where each node represents a plant species.
- Our goal is to find the Lowest Common Ancestor (LCA) of two given species based on lexicographical ordering.
- The LCA of two nodes is the lowest node in the tree that has both nodes as descendants, where a node is allowed to be a descendant of itself.
- Each node has a reference to its parent, allowing us to trace back to the root from any node.

Plan:
1. **Trace the Path to Root**:
   - Start from each node (`p` and `q`) and trace back to the root, storing the path in a set.
   - This will give us the ancestry paths for both nodes.
2. **Find the Common Ancestor**:
   - Starting from one node, check each ancestor in the set of ancestors of the other node.
   - The first common ancestor encountered in the path to the root is the LCA.

3. **Time Complexity**:
   - Since we are only traversing from each node to the root, the time complexity is O(h), where h is the height of the tree.
   - In a balanced binary tree, this would be O(log n).

4. **Space Complexity**:
   - We use a set to store the ancestors of one node, so the space complexity is O(h), where h is the height of the tree.

"""
# Implement:
def lca(root, p_species, q_species):
    # Helper function to find the node with the given species name
    def find_node(root, species):
        if not root:
            return None
        if root.val == species:
            return root
        left_search = find_node(root.left, species)
        if left_search:
            return left_search
        return find_node(root.right, species)

    # Get the nodes for p and q based on species names
    p_node = find_node(root, p_species)
    q_node = find_node(root, q_species)
    
    # Edge case: If either species is not found, return None
    if not p_node or not q_node:
        return None
    
    # Trace path to root for p_node
    ancestors_p = set()
    while p_node:
        ancestors_p.add(p_node)
        p_node = p_node.parent
    
    # Trace path to root for q_node and find the first common ancestor
    while q_node:
        if q_node in ancestors_p:
            return q_node.val  # Return the value of the common ancestor
        q_node = q_node.parent
    
    return None  # In case there is no common ancestor (should not happen if tree is well-formed)

# Example usage
fern = TreeNode("fern")
cactus = TreeNode("cactus", fern)
rose = TreeNode("rose", fern)
bamboo = TreeNode("bamboo", cactus)
dahlia = TreeNode("dahlia", cactus)
lily = TreeNode("lily", rose)
oak = TreeNode("oak", rose)

# Build the tree structure with parent pointers
fern.left, fern.right = cactus, rose
cactus.left, cactus.right = bamboo, dahlia
rose.left, rose.right = lily, oak

# Test the LCA function
print(lca(fern, "cactus", "rose"))  # Expected output: "fern"
print(lca(fern, "bamboo", "oak"))   # Expected output: "fern"
print(lca(fern, "bamboo", "dahlia")) # Expected output: "cactus"


"""
Advanced Set 2

Understand:


Plan:

"""
# Implement:

