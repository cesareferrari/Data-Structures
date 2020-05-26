import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        # max number of nodes it can hold
        self.limit = limit
        # current number of nodes it's holding
        self.size = 0
        # store the entries in doubly linked list
        self.storage = DoublyLinkedList()
        # storage dictionary
        self.storage_dict = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        # Instructor code:
        if key not in self.storage_dict:
            return None

        node = self.storage.head
        while node is not None:
            if key == node.value[0]: # node is stored as a list [key, value]
                self.storage.move_to_front(node)
                break
            node = node.next
        
        return self.storage_dict[key]

        # My original code below:
        # if key in self.storage_dict:
        #     # print("### key:", key) # for debugging

        #     # find node with value == self.storage_dict[key]
        #     node = self.storage.find(self.storage_dict[key])
        #     # print("### node found:", node) # for debugging
        #     # and move it to the end
        #     if node:
        #         self.storage.move_to_end(node)

        #     return self.storage_dict[key]
        # else:
        #     return None


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        # Instructor code:
        if key in self.storage_dict:
            # overwrite in the dictionary
            self.storage_dict[key] = value
            # overwrite in DLL
            # iterate on the list and find node to be updated
            node = self.storage.head

            while node is not None:
                # node is a list: [key, value]
                if key == node.value[0]:
                    node.value[1] = value
                    # move to head of DLL
                    self.storage.move_to_front(node)
                    break
                node = node.next

        else:
            # handle case when we are full
            if self.size == self.limit:
                # delete tail of list
                node = self.storage.tail
                old_key = node.value[0] # because the node is a list: [key, value]

                self.storage.remove_from_tail()

                del self.storage_dict[old_key]
                # pop would also work
                # self.storage_dict.pop(old_key)

                self.size -= 1

            # add to the cache
            self.storage_dict[key] = value
            # add as a list because we may want to overwrite later
            self.storage.add_to_head([ key, value ]) 
            self.size += 1



        # My original code below:
        # if key in self.storage_dict:
        #     # if the key already exist
        #     # overwrite value
        #     self.storage_dict[key] = value

        # else:
        #     # add a new item to the tail
        #     self.storage.add_to_tail(value)
        #     self.storage_dict[key] = value
        #     self.size += 1

        #     if self.size > self.limit:
        #         # remove one item from the head if we are 
        #         # over the limit
        #         self.storage.remove_from_head()
        #         self.size -= 1


# my_cache = LRUCache()

# my_cache.set('one', 1)
# my_cache.set('two', 2)

# print(my_cache.storage_dict)
# print("DLL length:", my_cache.storage.length)

# print(my_cache.get('one'))
# print(my_cache.get('two'))

