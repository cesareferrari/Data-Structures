"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"[V: {self.value} P: {self.prev}, N: {self.next}]"

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length


    def find_middle(self):
        middle = self.head
        end = self.head

        while end != None and end.next.next != None:
                end = end.next.next
                middle = middle.next

        return middle


    # head should be tail
    # tail should be head
    # no recursion, no other data structures
    def reverse_list(self):
        pass

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # if list has no nodes, head == None
        new_node = ListNode(value)

        # list has a head
        if self.head:
            current_head = self.head
            new_node.next = current_head
            self.head = new_node
        # list has no head
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1


    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head:
            current_value = self.head.value
            self.delete(self.head)

        return current_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)

        # if there is a tail
        if self.tail:
            current_tail = self.tail
            new_node.prev = current_tail
            self.tail = new_node
        else:
            # if there is no tail, there is also no head
            self.tail = new_node
            self.head = new_node

        self.length += 1


    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value

        # if 0 node
        if not self.tail:
            return

        # if head and tail are the same (1 node)
        elif self.head == self.tail:
            self.head = None
            self.tail = None

        # more than 1 node
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1
        return value

        # if self.tail:
        #     current_value = self.tail.value
        #     self.delete(self.tail)

        # return current_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        current_head = self.head
        node.next = current_head
        current_head.prev = node
        self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

        # current_tail = self.tail
        # node.prev = current_tail
        # current_tail.next = node
        # self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # list has no items
        if self.head == None:
            return

        # list has 1 item same head and tail
        if self.head == self.tail:
            self.head = None
            self.tail = None

        # delete the head
        if node == self.head:
            new_head = node.next
            self.head.prev = None
            self.head = new_head

        # delete the tail
        if node == self.tail:
            new_tail = node.prev
            self.tail.next = None
            self.tail = new_tail

        else:
            node.delete()

        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        # walk through the entire list
        # keep track of the biggest value we've found

        highest_value = self.head.value
        current_node = self.head

        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = curent_node.value

            current_node = current_node.next

        return highest_value


