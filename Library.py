from ObjectType import ObjectType
from Collection import Collection


class Library(object):
    """
        CLASS LIBRARY
        A LIBRARY IS AN ADT THAT CONTAINS:
        - STRING    LIBRARY NAME
        - LIST      COLLECTION LIST
        - LIST      OBJECT LIST
        - DICT.     COLLECTION TYPES

        *TO BE ADDED IN THE FUTURE:
        - LIST OF USERS WITH ACCESS
        - DIRECTORY OF A DATA FILE
    """
    def __init__(self, name):
        """
        CONSTRUCTOR FOR LIBRARY
        :param name: STRING - NAME OF LIBRARY
        """
        self.__lib_name = name
        self.__col_list = []
        self.__obj_list = []
        self.__col_types = {}

    def create_collection(self, col_name, obj_type, obj_attributes):
        """
        CREATE A NEW COLLECTION IN LIBRARY
        :param col_name: STRING - NAME OF NEW COLLECTION
        :param obj_type: STRING - OBJECT TYPE
        :param obj_attributes: DICTIONARY - OBJECT DEFINITION
        :return: VOID
        """
        for c in self.__col_list:
            if c.get_name() == col_name:
                print("A Collection with that name already exists")
                return
        obj_def = ObjectType(obj_type, obj_attributes)
        new_col = Collection(col_name, obj_def)
        self.__col_list.append(new_col)
        objdef_exist = False
        for o in self.__obj_list:
            if o.get_obj_type() == obj_def.get_obj_type() \
                    and o.get_obj_att_def() == obj_def.get_obj_att_def():
                objdef_exist = True
        if not objdef_exist:
            self.__obj_list.append(obj_def)
        return

    def add_collection(self, collection):
        """
        ADD COLLECTION TO LIBRARY
        :param collection: COLLECTION - COLLECTION TO BE ADDED
        :return: VOID
        """
        for c in self.__col_list:
            if c.get_name() == collection.get_name():
                print("A Collection with that name already exists")
                return
        self.__col_list.append(collection)
        obj_def = collection.get_obj_def()
        objdef_exist = False
        for o in self.__obj_list:
            if o.get_obj_type() == obj_def.get_obj_type() \
                    and o.get_obj_att_def() == obj_def.get_obj_att_def():
                objdef_exist = True
        if not objdef_exist:
            self.__obj_list.append(obj_def)

    def remove_collection(self, col_name):
        """
        REMOVE COLLECTION FROM LIBRARY
        :param col_name: STRING - NAME OF COLLECTION TO BE REMOVED
        :return: VOID
        """
        for c in self.__col_list:
            if c.get_name() == col_name:
                self.__col_list.remove(c)
                objdef_used = False
                obj_def = c.get_obj_def()
                for c2 in self.__col_list:
                    if c2.get_obj_def().get_obj_type() == obj_def.get_obj_type() \
                            and c2.get_obj_def().get_obj_att_def() == obj_def.get_obj_att_def():
                        objdef_used = True
                if not objdef_used:
                    self.__obj_list.remove(obj_def)
                c.destroy_col()
                return
        print('"{}" does not exist in this library.'.format(col_name))

    def get_collection(self, col_name):
        """
        GET COLLECTION
        :param col_name: STRING - NAME OF COLLECTION
        :return: COLLECTION
        """
        for c in self.__col_list:
            if c.get_name() == col_name:
                return c
        print('"{}" does not exist in this library.'.format(col_name))

    def get_col_list_size(self):
        """
        GET SIZE OF COLLECTION LIST IN LIBRARY
        :return: INT - SIZE OF COLLECTION LIST
        """
        return len(self.__col_list)

    def get_obj_list_size(self):
        """
        GET SIZE OF OBJECT LIST IN LIBRARY
        :return: INT - SIZE OF OBJECT LIST
        """
        return len(self.__obj_list)

    def display_lib(self):
        """
        DISPLAY LIBRARY INFO
        :return: VOID
        """
        print("============================")
        print("Library: {}".format(self.__lib_name))
        print("{} Collections\n{} Objects".format(self.get_col_list_size(), self.get_obj_list_size()))
        for c in self.__col_list:
            print("----------------------------")
            print("Name: {}".format(c.get_name()))
            print("Size: {}".format(c.col_size()))
            print("Type:", c.get_obj_def_str())
        print("----------------------------")

    def display_all_lib(self):
        """
        DISPLAY LIBRARY INFO WITH COLLECTIONS
        :return: VOID
        """
        print("============================")
        print("Library: {}".format(self.__lib_name))
        print("{} Collections\n{} Objects".format(self.get_col_list_size(), self.get_obj_list_size()))
        print("============================")
        for c in self.__col_list:
            c.display_col()
            print("----------------------------")

    def is_empty(self):
        """
        CHECKS IF COLLECTION LIST IS EMPTY
        :return: BOOLEAN
        """
        return 0 == len(self.__col_list)

    def get_name(self):
        """
        GET LIBRARY NAME
        :return: STRING - LIBRARY NAME
        """
        return self.__lib_name

    def get_collection_list(self):
        """
        GET COLLECTION LIST
        :return: LIST - COLECTIONS
        """
        return self.__col_list

    def get_collection_name_list(self):
        """
        GET LIST WITH NAMES OF ALL COLLECTIONS
        :return: LIST - COLLECTIONS NAMES
        """
        return [c.get_name() for c in self.__col_list]
