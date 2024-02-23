#!/usr/bin/python3
""" Basic Caching """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
        BasicCache has two methods
        put(self, key, item)- this inserts the item
        into self.cache_data[key]

        get(self, key) - This returns the item
        with key <key>
    """
    def put(self, key, item):
        """Method for adding an item"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Method for retrieving item"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
