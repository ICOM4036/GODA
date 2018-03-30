

class ObjectType:
    """
        CLASS OBJECT TYPE
        AN OBJECT TYPE IS AN ADT THAT CONTAINS THE DEFINITION OF AN OBJECT TYPE:
        - TYPE OF OBJECT
        - LIST OF ATTRIBUTES (I.E. VARIABLES)
    """
    __obj_type = ''
    __attributes_dict = {}
    __attributes_list = []

    def __init__(self, obj_type, attribute_dict):
        """
        OBJECT TYPE CONSTRUCTOR
        :param obj_type: STRING - OBJECT TYPE
        :param attribute_dict: DICTIONARY - ATTRIBUTES' NAMES AND RESPECTIVE DATA TYPES
        """
        self.__obj_type = obj_type
        self.__attributes_dict = attribute_dict
        for a in self.__attributes_dict:
            self.__attributes_list.append(a)

    def get_obj_attributes(self):
        """
        GET LIST OF ATTRIBUTES
        :return: LIST - ATTRIBUTES
        """
        return self.__attributes_list

    def get_obj_data_types(self):
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
