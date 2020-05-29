
# add to the back of a text buffer
# add to the front of a text buffer
# delete from the back of a text buffer
# delete from the front of a text buffer
# add to the middle
# join text buffers together


# array vs DLL
# array: add to back: O(1) constant
# array: add to front: O(n) Linear
# array: delete from back: O(1) constant
# array: delete from  front: O(n) Linear
# array: join text buffers together: O(n)

# DLL: add to back: O(1)
# DLL: add to front: O(1)
# DLL: delete from back: O(1)
# DLL: delete from front: O(1)
# DLL: join text buffers together: O(1) point end of one list to the front of
# the next

# __str__ to print out what's inside
# array: O(n)
# DLL: O(n)

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLindedList

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLindedList()

    def __str__(self):
        string_to_return = ""
        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next

        return string_to_return

    def join(self, other_buffer):
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head = self.storage.tail

        # point tail to new tail
        self.storage.tail = other_buffer.storage.tail

    def append(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_tail()

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head()

    def delete_from_front(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head()

    def delete_from_back(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_tail()

    def find_text(self, text_to_find):
        pass


text = TextBuffer()
text.append('hello')

other_buffer = TextBuffer()
other_buffer.append(' how are you')

text.join(other_buffer)

print(text)



