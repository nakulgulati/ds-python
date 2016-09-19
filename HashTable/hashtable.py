class HashTable:
    """
    Hash table class
    """

    def __init__(self, max_size=10):
        self.max_size = max_size
        self.data = [[] for _ in range(max_size)]

    def __hashFunc__(self, key):
        return sum(ord(c) for c in key) % self.max_size

    def __findByKey__(self, key, func):
        found_item = None
        index = self.__hashFunc__(key)
        cell = self.data[index]

        for d in cell:
            if d[0] == key:
                found_item = d
                break

        return func(found_item, cell)

    def set(self, key, obj):
        """
        Sets the key with the specified value.
        :param key:
        :param obj:
        :return:
        """

        def set_item(item, cell):
            if item:
                item[1] = obj
            else:
                cell.append([key, obj])

        self.__findByKey__(key, set_item)

    def get(self, key):
        """
        Retrieves the value for a given key
        :param key:
        :return obj || -1:
        """

        def get_item(item, cell):
            if item:
                return item[1]
            else:
                return -1

        return self.__findByKey__(key, get_item)

    def remove(self, key):
        """
        Remove an item for a given key
        :param key:
        :return:
        """

        def remove_item(item, cell):
            if item:
                cell.remove(item)
            else:
                raise KeyError(key)

        self.__findByKey__(key, remove_item)
