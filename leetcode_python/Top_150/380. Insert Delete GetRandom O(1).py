class RandomizedSet(object):

    def __init__(self):

        self.data_dict = {}
        self.data = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            return False

        self.data_dict[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.data_dict:
            return False

        last_elem_in_list = self.data[-1]
        index_of_elem_tp_remove = self.data_dict[val]

        self.data_dict[last_elem_in_list] = index_of_elem_tp_remove
        self.data[index_of_elem_tp_remove] = last_elem_in_list

        self.data[-1] = val
        self.data.pop()
        self.data_dict.pop(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()