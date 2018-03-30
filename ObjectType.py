

class ObjectType:
    """
        CLASS OBJECT TYPE
        AN OBJECT TYPE IS AN ADT THAT CONTAINS THE DEFINITION OF AN OBJECT TYPE:
        - TYPE OF OBJECT
        - LIST OF ATTRIBUTES (I.E. VARIABLES)
    """
    __obj_type = ''
    __attributes = []

    def __init__(self, obj_type, attribute_list):
        """
        OBJECT TYPE CONSTRUCTOR
        :param obj_type: STRING - OBJECT TYPE
        :param attribute_list: LIST - ATTRIBUTES' NAMES
        """
        self.__obj_type = obj_type
        self.__attributes = attribute_list

    def get_obj_attributes(self):
        """
        GET LIST OF ATTRIBUTES
        :return: LIST - ATTRIBUTES
        """
        return self.__attributes

    def get_obj_type(self):
        """
        GET OBJECT TYPE
        :return: STRING - OBJECT TYPE
        """
        return self.__obj_type
