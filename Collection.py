

class Collection:
    """
        CLASS COLLECTION
        A COLLECTION IS AN ADT THAT CONTAINS:
        - TYPE OF OBJECT
        - LIST OF OBJECTS
        - DIRECTORY OF A DATA FILE *(TO BE ADDED IN THE FUTURE)*
    """
    __col_name = ''
    __obj_type = ''
    __obj_attributes = []
    __obj_collection = []
    __obj_val_map = {}

    def __init__(self, name, obj_def):
        """
        COLLECTION CLASS CONSTRUCTOR
        :param name: STRING - NAME OF COLLECTION
        :param obj_def: OBJECTTYPE - DEFINITION OF OBJECTS WITHIN COLLECTION
        """
        self.__col_name = name
        self.__obj_type = obj_def.get_obj_type()
        self.__obj_attributes = obj_def.get_obj_attributes()
        for i in range(0, len(self.__obj_attributes)):
            self.__obj_val_map.__setitem__(self.__obj_attributes[i], i)

    def get_obj_def(self):
        """
        GETTER FOR OBJECT DEFINITION
        :return: STRING - OBJECT DEFINITION IN A STRING
        """
        s = self.__obj_type + "{|"
        for i in range(0, len(self.__obj_attributes)):
            s = s + " {} |".format(self.__obj_attributes[i])
        s = s + "}"
        return s

    def add_obj(self, attribute_values):
        """
        ADD NEW OBJECT TO COLLECTION
        :param attribute_values: LIST - VALUES FOR AN OBJECT'S ATTRIBUTES
        :return: VOID
        """
        self.__obj_collection.append(self.Object(attribute_values))

    def remove_obj(self, index):
        """
        REMOVE OBJECT AT INDEX
        :param index: INTEGER - INDEX OF OBJECT TO BE REMOVED
        :return: VOID
        """
        self.__obj_collection.remove(self.__obj_collection[index])

    def set_obj_val(self, index, attribute, value):
        """
        SET OR CHANGE A VALUE FROM AN OBJECT ATTRIBUTE
        :param index: INTEGER - INDEX OF OBJECT
        :param attribute: STRING - ATTRIBUTE TO BE CHANGED
        :param value: NEW VALUE
        :return: VOID
        """
        self.__obj_collection[index].set_value(self.__obj_val_map.get(attribute), value)

    def get_obj_val(self, index, attribute):
        """
        GET VALUE OF AN OBJECT'S ATTRIBUTE AT INDEX
        :param index: INTEGER - INDEX OF OBJECT
        :param attribute: STRING - VALUE TO BE RETURNED
        :return: VALUE
        """
        return self.__obj_collection[index].get_value(self.__obj_val_map.get(attribute))

    def get_all_obj_val(self, attribute):
        """
        GET LIST OF SPECIFIC VALUE FROM ALL OBJECTS
        :param attribute: STRING - VALUE TO BE LISTED
        :return: LIST - VALUES
        """
        temp = []
        for o in self.__obj_collection:
            temp.append(o.get_value(self.__obj_val_map.get(attribute)))
        return temp

    def display_col(self):
        """
        DISPLAY COLLECTION TO CONSOLE
        :return: VOID
        """
        print("Collection:", self.__col_name, "\nType:", self.__obj_type)
        s = "INDEX | "
        for i in self.__obj_attributes:
            s = s + " {} | ".format(i)
        print(s)
        for i in range(0, len(self.__obj_collection)):
            s1 = " {} | ".format(i) + self.__obj_collection[i].to_string()
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

    class Object:
        """
        INNER CLASS OBJECT
        AN OBJECT CONTAINS:
        - VALUES BASED ON THE OBJECTTYPE DEFINED FOR A COLLECTION
        """
        __values = []

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
            s = ''
            for i in self.__values:
                s = s + " {} |".format(i)
            return s

