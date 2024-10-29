"""
Set 1

Understand:
- We are given 2 inputs 'mission1' and 'mission2' which are heads to two linked lists
- each node represents a mission and its priority value (int)
- we are to write a function merge_missions() to recursively sort and merge the two lists into one linked list
- combined list should maintain correct order of priorities
- we combine by splicing the nodes from the two lists
- we return the head of the combined list

Plan:
- check if there are nodes in each list
- compare the value of the nodes, add them to a new combined list
- our base case is if both the lists are exhausted

"""
# Implement:
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_missions(mission1, mission2):
    
    # Base cases
    if mission1 is None:
        return mission2
    if mission2 is None:
        return mission1
    
    # Recursive cases
    if mission1.value < mission2.value:
        mission1.next = merge_missions(mission1.next, mission2)
        return mission1
    else:
        mission2.next = merge_missions(mission1, mission2.next)
        return mission2




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

