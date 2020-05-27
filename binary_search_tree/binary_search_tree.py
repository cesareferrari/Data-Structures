"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Create a new node
        node = BSTNode(value)

        # if value is more or equal than self.value, go to the right
        if value >= self.value:
            # if there is nothing at the right, insert the new node
            if self.right is None:
                self.right = node 
            else:
                # if there is a right node already, try again recursively
                # until you find None as the right node.
                # At that point, the previous branch is run and the 
                # node is inserted to the right.
                self.right.insert(value)

        # if value is less than current node value, insert to the left.
        # same logic as above
        if value < self.value:
            if self.left is None:
                self.left = node 
            else:
                self.left.insert(value)



    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        pass

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


my_node = BSTNode(5)
my_node.insert(2)
my_node.insert(3)

print("right", my_node.right)
print("left", my_node.left.value)
print("left - right", my_node.left.right.value)
