

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
        :param obj_type: STRING - OBJECT TYPE
        :param attribute_dict: DICTIONARY - {ATTRIBUTE : DATA TYPE}
        """
        self.__obj_type = obj_type
        self.__attributes_dict = attribute_dict

    def get_obj_attributes(self):
        """
        GET LIST OF ATTRIBUTES
        :return: LIST - ATTRIBUTES
        """
        return [key for key in self.__attributes_dict]

    def get_obj_data_types(self):
        """
        GET LIST OF DATA TYPES
        :return: LIST - DATA TYPES
        """
        return [self.__attributes_dict[x] for x in self.__attributes_dict]

    def get_obj_att_def(self):
        """
        GET DICTIONARY OF ATTRIBUTES WITH RESPECTIVE DATA TYPES
        :return: DICTIONARY - {ATTRIBUTE : DATA TYPE}
        """
        return self.__attributes_dict

    def get_obj_type(self):
        """
        GET OBJECT TYPE
        :return: STRING - OBJECT TYPE
        """
        return self.__obj_type



