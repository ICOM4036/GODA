

class Collection(object):
    """
        CLASS COLLECTION
        A COLLECTION IS AN ADT THAT CONTAINS:
        - STRING    COLLECTION NAME
        - STRING    OBJECT TYPE
        - LIST      OBJECT ATTRIBUTES
        - LIST      OBJECT DATA TYPES
        - LIST      OBJECT COLLECTION
        - DICT.     OBJECT VALUES MAP
        * DIRECTORY OF A DATA FILE (TO BE ADDED IN THE FUTURE)*
    """

    def __init__(self, name, obj_def):
        """
        COLLECTION CLASS CONSTRUCTOR
        :param name: STRING - NAME OF COLLECTION
        :param obj_def: OBJECTTYPE - DEFINITION OF OBJECTS WITHIN COLLECTION
        """
        self.__col_name = name
        self.__obj_def = obj_def
        self.__obj_att_dict = obj_def.get_obj_att_dict()
        self.__obj_type = obj_def.get_obj_type()
        self.__obj_attributes = obj_def.get_obj_attributes()
        self.__obj_val_map = {self.__obj_attributes[i]: i for i in range(0, len(self.__obj_attributes))}
        self.__obj_data_types = obj_def.get_obj_data_types()
        self.__obj_collection = []

    def add_obj(self, attribute_values):
        """
        ADD NEW OBJECT TO COLLECTION
        :param attribute_values: LIST - VALUES FOR AN OBJECT'S ATTRIBUTES
        :return: VOID
        """
        if len(attribute_values) != len(self.__obj_attributes)\
                or not self.__obj_check_data_type(attribute_values):
            print("Object not compatible with collection")
            return
        obj = self.__Object(attribute_values)
        self.__obj_collection.append(obj)

    def remove_obj(self, index):
        """
        REMOVE OBJECT AT INDEX
        :param index: INTEGER - INDEX OF OBJECT TO BE REMOVED
        :return: VOID
        """
        if index < 0 or index > len(self.__obj_collection) - 1:
            print("Index is out of bounds")
            return
        self.__obj_collection.remove(self.__obj_collection[index])

    def set_obj_val(self, index, attribute, value):
        """
        SET OR CHANGE A VALUE FROM AN OBJECT ATTRIBUTE
        :param index: INTEGER - INDEX OF OBJECT
        :param attribute: STRING - ATTRIBUTE TO BE CHANGED
        :param value: NEW VALUE
        :return: VOID
        """
        if index < 0 or index > len(self.__obj_collection) - 1:
            print("Index is out of bounds")
            return
        if not self.__obj_attributes.__contains__(attribute):
            print('Object does not have attribute "{}"'.format(attribute))
            return
        if not self.__obj_check_one_data_type(attribute, value):
            print('Value "{}" is not compatible with Object'.format(value))
            return
        self.__obj_collection[index].set_value(self.__obj_val_map.get(attribute), value)

    def get_obj_val(self, index, attribute):
        """
        GET VALUE OF AN OBJECT'S ATTRIBUTE AT INDEX
        :param index: INTEGER - INDEX OF OBJECT
        :param attribute: STRING - VALUE TO BE RETURNED
        :return: VALUE
        """
        if index < 0 or index > len(self.__obj_collection) - 1:
            print("Index is out of bounds")
            return
        if not self.__obj_attributes.__contains__(attribute):
            print('Object does not have attribute "{}"'.format(attribute))
            return
        return self.__obj_collection[index].get_value(self.__obj_val_map.get(attribute))

    def get_all_obj_val(self, attribute):
        """
        GET LIST OF SPECIFIC VALUE FROM ALL OBJECTS
        :param attribute: STRING - VALUE TO BE LISTED
        :return: LIST - VALUES
        """
        if not self.__obj_attributes.__contains__(attribute):
            print('Object does not have attribute "{}"'.format(attribute))
            return
        temp = []
        valpos = self.__obj_val_map.get(attribute)
        for o in self.__obj_collection:
            temp.append(o.get_value(valpos))
        return temp

    def get_obj(self, index):
        """
        GET OBJECT
        :param index: INTEGER - INDEX OF OBJECT
        :return: OBJECT
        """
        if index < 0 or index > len(self.__obj_collection) - 1:
            print("Index is out of bounds")
            return
        return self.__obj_collection[index]

    def get_obj_list(self):
        """
        GET LIST OF OBJECTS
        :return: LIST - OBJECT
        """
        return self.__obj_collection

    def get_obj_def(self):
        """
        GET OBJECT DEFINITION
        :return: OBJECTTYPE - OBJECT DEFINITION
        """
        return self.__obj_def

    def get_obj_def_str(self):
        """
        GETTER FOR OBJECT DEFINITION
        :return: STRING - OBJECT DEFINITION IN A STRING
        """
        s = self.__obj_type + "{|"
        for i in self.__obj_att_dict:
            s = s + " {}: {} |".format(i, str(self.__obj_att_dict[i]).split("'")[1])
        s = s + "}"
        return s

    def __obj_check_data_type(self, values):
        """
        OBJECT COMPATIBILITY WITH COLLECTION
        :param values: LIST - OBJECT VALUES
        :return: BOOLEAN
        """
        for i in range(0, len(self.__obj_data_types)):
            if not isinstance(values[i], self.__obj_data_types[i]) and values[i] is not None:
                return False
        return True

    def __obj_check_one_data_type(self, attribute, value):
        """
        CHECK ATTRIBUTE COMPATIBILITY WITH OBJECT
        :param attribute: STRING - ATTRIBUTE
        :param value: VALUE - NEW VALUE
        :return: BOOLEAN
        """
        index = self.__obj_val_map[attribute]
        return isinstance(value, self.__obj_data_types[index]) and value is not None

    def display_col(self):
        """
        DISPLAY COLLECTION TO CONSOLE
        :return: VOID
        """
        print("Collection:", self.__col_name, "\nSize:", self.col_size(), "\nType:", self.__obj_type)
        s = "INDEX |"
        for i in self.__obj_attributes:
            s = s + " {} |".format(i)
        print(s)
        for i in range(0, len(self.__obj_collection)):
            s1 = " {} ".format(i) + self.__obj_collection[i].to_string()
            print(s1)

    def col_size(self):
        """
        SIZE OF COLLECTION
        :return: INTEGER - SIZE OF COLLECTION
        """
        return len(self.__obj_collection)

    def is_empty(self):
        """
        CHECKS IF COLLECTION IS EMPTY
        :return: BOOLEAN
        """
        return len(self.__obj_collection) == 0

    def get_name(self):
        """
        GET COLLECTION NAME
        :return: STRING - COLLECTION NAME
        """
        return self.__col_name

    def destroy_col(self):
        """
        CLEAR A COLLECTION
        :return: VOID
        """
        self.__col_name = None
        self.__obj_type = None
        self.__obj_attributes.clear()
        self.__obj_val_map.clear()
        self.__obj_data_types.clear()
        self.__obj_val_map.clear()
        self.__obj_data_types.clear()
        self.__obj_def = None
        for o in self.__obj_collection:
            o.destroy_obj()
        self.__obj_collection.clear()

    class __Object(object):
        """
        INNER CLASS OBJECT
        AN OBJECT CONTAINS:
        - LIST  VALUES
        """

        def __init__(self, values):
            """
            CONSTRUCTOR FOR OBJECT
            :param values: LIST - VALUES FOR ATTRIBUTES
            """
            self.__values = values


        def get_value(self, index):
            """
            GET VALUE AT INDEX
            :param index: INTEGER - INDEX OF VALUE
            :return: VALUE
            """
            return self.__values[index]

        def get_values(self):
            """
            GET LIST OF ALL VALUES OF AN OBJECT
            :return: LIST - VALUES
            """
            return self.__values

        def set_value(self, index, value):
            """
            SET OR CHANGE VALUE OF AN OBJECT'S ATTRIBUTE AT INDEX
            :param index: INTEGER - INDEX OF VALUE TO BE CHANGED
            :param value: NEW VALUE
            :return: VOID
            """
            self.__values[index] = value

        def to_string(self):
            """
            GENERATE A STRING OF AN OBJECT'S VALUES
            :return: STRING - OBJECT VALUES
            """
            s = '|'
            for i in self.__values:
                s = s + " {} |".format(i)
            return s

        def destroy_obj(self):
            """
            CLEAR OBJECT VALUES
            :return: VOID
            """
            self.__values.clear()
