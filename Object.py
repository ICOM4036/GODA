"""
    OBJECT
    AN OBJECT IS AN ADT THAT CONTAINS:
    - TYPE OF OBJECT
    - LIST OF ATTRIBUTES (I.E. VARIABLES)
    - MAP OF VARIABLES WITH RESPECTIVE KEYWORDS
"""


class Object:

    __obj_type = ''
    __attributes = []
    __var_map = {}

    def __init__(self, otype, att_list):
        self.__obj_type = otype
        self.__attributes = att_list

    def set_values(self, val_list):
        for i in range(0, len(self.__attributes)):
            self.__var_map.__setitem__(self.__attributes[i], val_list[i])

    def get_attributes(self):
        return self.__attributes

    def get_val(self, key):
        return self.__var_map.get(key)

    def get_val_list(self):
        val_list = []
        for key in self.__var_map:
            val_list.append(self.__var_map.get(key))
        return val_list

    def get_type(self):
        return self.__obj_type


