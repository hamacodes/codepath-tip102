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

# Set 1 Tests:
mission1 = Node(1, Node(2, Node(4)))
mission2 = Node(1, Node(3, Node(4)))

print_linked_list(merge_missions(mission1, mission2))  # Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4 


"""
Set 2

Understand:
- We are given a linked list of spells
- each spell has a name and a next pointer
- we are to write a function weave_spells() to merge the spells in alternating order
- we return the head of the new linked list

Plan:
- check if there are nodes in each list
- merge the nodes in alternating order
- our base case is if both the lists are exhausted

"""
# Implement:
def weave_spells(spell_a, spell_b):
    if spell_a is None:
        return spell_b
    if spell_b is None:
        return spell_a
    
    spell_a.next = weave_spells(spell_b, spell_a.next)
    return spell_a

# Set 2 Tests:
spell_a = Node('A', Node('C', Node('E')))
spell_b = Node('B', Node('D', Node('F')))

print_linked_list(weave_spells(spell_a, spell_b))  # Expected: A -> B -> C -> D -> E -> F

"""
Advanced Set 1

Understand:
- We are given a string 'expression' that represents a ternary expression
- the expression consists of digits and the characters 'T' and 'F'
- we are to write a function evaluate_ternary_expression_recursive() to evaluate the expression
- the expression is evaluated from left
- if the character is 'T', we evaluate the expression to the left of '?'
- if the character is 'F', we evaluate the expression to the right of ':'
- we return the evaluated result

Plan:
- we define a helper function that takes an index as an argument
- if the character at the index is a digit or 'T' or 'F', we return the character and index
- we recursively call the helper function for the expressions to the left and right of '?'
- we evaluate the result based on the condition ('T' or 'F')
- we return the result
"""
# Implement:
def evaluate_ternary_expression_recursive(expression):
    def helper(index):
        # Base case: If it's a digit or 'T'/'F', return the character and index
        if expression[index] not in '?TF':
            return expression[index], index

        # Recursive case
        condition = expression[index]
        true_expr, index = helper(index + 2)  # Skip '?'
        false_expr, index = helper(index + 1)  # Skip ':'

        # Evaluate based on the condition ('T' or 'F')
        result = true_expr if condition == 'T' else false_expr
        return result, index

    # Start the helper from the first character and return the result
    result, _ = helper(0)
    return result

# Test cases
print(evaluate_ternary_expression_recursive("T?2:3"))      # Expected output: "2"
print(evaluate_ternary_expression_recursive("F?1:T?4:5"))  # Expected output: "4"
print(evaluate_ternary_expression_recursive("T?T?F:5:3"))  # Expected output: "F"

"""
Advanced Set 2

Understand:


Plan:

"""
# Implement:

