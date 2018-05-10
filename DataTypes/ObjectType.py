

class ObjectType(object):
    """
        CLASS OBJECT TYPE
        AN OBJECT TYPE IS AN ADT THAT CONTAINS THE DEFINITION OF AN OBJECT TYPE:
        - STRING    OBJECT TYPE
        - DICT.     OBJECT DATA TYPES
    """

    def __init__(self, obj_type, attribute_dict):
        """
        OBJECT TYPE CONSTRUCTOR
        WILL CONVERT DICTIONARY FROM {STR_ATTRIBUTE : STR_TYPE} TO {STR_ATTRIBUTE : TYPE}
        :param obj_type: STRING - OBJECT TYPE
        :param attribute_dict: DICTIONARY - {STR_ATTRIBUTE : STR_TYPE}
        """
        self.__obj_type = obj_type
        self.__attributes_dict = {}
        for d in attribute_dict:
            t = attribute_dict[d]
            if t == "int":
                self.__attributes_dict.__setitem__(d, int)
            elif t == "float":
                self.__attributes_dict.__setitem__(d, float)
            elif t == "str":
                self.__attributes_dict.__setitem__(d, str)
            elif t == "bool":
                self.__attributes_dict.__setitem__(d, bool)
            else:
                print('Unsupported data type "{}"'.format(t))

    def get_obj_attributes(self):
        """
        GET LIST OF ATTRIBUTES
        :return: LIST - ATTRIBUTES
        """
        return [key for key in self.__attributes_dict]

    def get_obj_data_types(self):
        """
        GET LIST OF DATA TYPES
        :return: LIST - TYPES
        """
        return [self.__attributes_dict[x] for x in self.__attributes_dict]

    def get_obj_att_dict(self):
        """
        GET DICTIONARY OF ATTRIBUTES WITH RESPECTIVE DATA TYPES
        :return: DICTIONARY - {STR_ATTRIBUTE : TYPE}
        """
        return self.__attributes_dict

    def get_obj_att_string(self):
        string = ""
        count = len(self.__attributes_dict) - 1
        for key in self.__attributes_dict:
            count -= 1
            string += key + ":" + self.__attributes_dict[key]
            if count >= 0:
                string += ","
        return string

    def get_obj_type(self):
        """
        GET OBJECT TYPE
        :return: STRING - OBJECT TYPE
        """
        return self.__obj_type


