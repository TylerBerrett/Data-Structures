from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    # dll(ListNode(item1, a))
    # dict[item1] returns ListNode(item1, a)

    def __init__(self, limit=10):
        self.limit = limit
        self.cache = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        try:
            node = self.storage[key]
            self.cache.move_to_front(node)
            return node.value
        except KeyError:
            return None

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
        if key in self.storage.keys():
            self.storage[key] = ListNode(value)
        else:
            if self.cache.length < self.limit:
                self.cache.add_to_head(value)
                self.storage[key] = self.cache.head
            elif self.cache.length >= self.limit:
                self.cache.tail.value = None
                self.cache.remove_from_tail()
                self.cache.add_to_head(value)
                self.storage[key] = self.cache.head
