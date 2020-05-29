"""
cs.usfca.edu/~galles/visualization/BST.html

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
    # My code
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

"""
# Instructor code
def insert(self, value):

    if value >= self.value:
        if self.right is not None:
            self.right.insert(value)
        else:
            new_node = BSTNode(value)
            self.right = new_node
    else:
        if self.left is not None:
            self.left.insert(value)
        else:
            new_node = BSTNode(value)
            self.left = new_node
"""






    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if current node value is the target, return true
        if self.value == target:
            return True

        # if current node value is less than the target
        # target must be on the right
        if self.value < target:
            # if there's nothing on the right, we didn't find the target,
            # return false
            if self.right is None:
                return False
            else:
                # if there's something on the right, keep searching recursively
                # until the value is found, 
                # and returns True (self.value == target see line 48)
                return self.right.contains(target)

        # same code as previous branch, but looking left
        if self.value >= target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)


"""
    # Instructor code
    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is not None:
                return self.right.contains(target)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.contains(target)
            else:
                return False
"""




    # Return the maximum value found in the tree
    def get_max(self):
        # larger values are on the right, so we only look at the right side

        # if there is nothing at the right of the current node,
        # this is the largest value
        if self.right is None:
            return self.value
        else:
            # recursively look at the right until you get to the end
            # where self.right is None
            return self.right.get_max()


"""
    # Instructor code
    def get_max(self):
        current_node = self
        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value
"""



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)





    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        
        # make a queue
        # enqueue the node
        # as long as the queue is not empty
        ## dequeue from the front of the queue, this is our current node
        ## enqueue the kids of the current node on the queue

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

        # make a stack
        # push the node on the stack
        # as long as the stack is not empty
        ## pop off the stack, this is our current node
        ## put the kids of the current node on the stack
        ## (check that they are not None, then put them on the stack)




    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

