#!/usr/bin/python3
""" FIFO cache """

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
        FifoCache has two methods
        put(self, key, item)- this inserts the item
        into self.cache_data[key]

        get(self, key) - This returns the item
        with key <key>
    """
    def __init__(self):
        """ initialize the class """
        super().__init__()

    def put(self, key, item):
        """Method for adding an item"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            # Find the first item inserted into the cache (FIFO)
            first_key = next(iter(self.cache_data))
            print("DISCARD:", first_key)
            del self.cache_data[first_key]
        self.cache_data[key] = item

    def get(self, key):
        """Method for retrieving item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
