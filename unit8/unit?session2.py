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

