import os, csv
from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from DataTypes.Library import Library
import InputManager, OutputManager, OutputManager2
from Comparators.NumberComparator import NumberComparator
from Comparators.LetterComparator import LetterComparator
from SortingAlgorithms.Quicksort import Quicksort
from math import fabs

class Handler:

    def __init__(self):

        # This is the default Directory where libraries are saved
        self.dir_path = "C:/Users/irixa/PycharmProjects/GODA/Directory"
        self.libraries = {}
        #self.collections = {}
        self.objects = {}


    def openLibrary(self, library_name):
        """
        Creates an instance of a library so that a user can
        use commands to manage it
        :param library_name: str - library name
        :return: None
        """

        # library_path = "{}/{}".format(self.dir_path, library_name)
        #
        # try:
        #     # Open list with collections in library
        #     with open("{}/{}.txt".format(library_path, library_name), 'wb') as csvfile:
        #         library_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        #
        #     for coll in library_reader:
        #         # Open collection text
        #         with open("{}/{}.txt".format(library_path, coll), 'wb') as csvfile:
        #             collection_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        #             coll_name = collection_reader.nextLine
        #             obj_name = nextLine
        #             if object_name is not in self.objects:
        #                 obj_attributes = nextLine
        #                 object = ObjectType().__init__(obj_name, obj_attributes)
        #                 self.objects.append(object)
        #             collection
        #
        #     # Open Collection List
        #     with open("{}/{}/CollectionsList.csv".format(self.dir_path, library_name), 'wb') as csvfile:
        #         collection_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        #
        #     for row in collection_reader:
        #         createCollection(row)
        #
        #
        # except Error:
        #     pass

        if self.library_is_opened(library_name):
            print("Library %s is already opened" % library_name)
            return
        #library = InputManager.imp_new_library(library_name)
        self.libraries[library_name] = Library(library_name)



    def close_library(self, library_name):
        """
        Deletes the instance of an opened library
        :param library_name: str - library name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or it is not opened" % library_name)
            return
        del self.libraries[library_name]


    def library_is_opened(self, library_name):
        for key in self.libraries:
            if key == library_name:
                return True
        return False


    # def createLibraryDirectory(self, library_name):
    #
    #     # Create a directory with the library's name
    #     library_path = "%s/%s" % (self.dir_path, library_name)
    #
    #     try:
    #         os.makedirs(library_path)
    #     except OSError as e:
    #         print("A library with that name already exists")
    #         return
    #
    #     # Create an ObjectList csv file
    #     with open('{}/ObjectsList.csv'.format(library_path), 'wb') as csvfile:
    #         filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    #
    #     # Create a CollectionsList csv file
    #     with open('{}/CollectionsList.csv'.format(library_path), 'wb') as csvfile:
    #         filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    #
    #     # Create an ImportedCommandsList csv file
    #     with open('{}/ImportedCommandsList.csv'.format(library_path), 'wb') as csvfile:
    #         filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    #
    #     # Create a subdirectory to contain all collections
    #     coll_path = "{}/Collections".format(library_path)
    #     os.makedirs(coll_path)
    #
    #
    #
    # def createObject(self, obj_string):
    #     """
    #     Crea un objeto con la clase OjectType
    #     :param str:
    #     :return:
    #     """
    #
    #     type = obj_string[0]
    #     attributes = []
    #     for s in range(len(obj_string) - 1):
    #         attributes.append(obj_string[s + 1])
    #     new_object = ObjectType(type, self.mapAttributesToDict(attributes))
    #
    #     self.objects[type] = new_object
    #
    #
    # def mapAttributesToDict(self, attributes):
    #     dict = {}
    #     for a in attributes:
    #         dict[a] = None
    #     return dict
    #
    # def createLibrary(self, library_name):
    #
    #     lib = Library(library_name)
    #     self.libraries[library_name] = lib
    #
    #
    #
    # def addObjectToLibrary(self, library, object):
    #     library_path = "{}/{}".format(self.dir_path, library)
    #
    #     #Open ObjectsList file
    #     filewriter = csv.writer(open ('{}/ObjectsList.csv'.format(library_path), 'w'))
    #
    #     #Append the object to ObjectsList file
    #     filewriter.writerow(object)
    #
    #     self.createObject(object)


    def create_library(self, library_name):
        """
        Creates a new library
        :param library_name: str - library name
        :return: None
        """
        #library = Library(library_name)
        OutputManager2.create_library(self.dir_path, library_name)
        #OutputManager.save_library(library)
        self.openLibrary(library_name)


    def create_collection(self, library_name, collection_name, object_type):
        """
        Creates a new collection and adds it to a library
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param object_type: str - name of the object type
        :return:
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return

        lib = self.libraries[library_name]
        obj_type = self.objects[object_type]
        col = Collection(collection_name, obj_type)
        lib.add_collection(col)
        OutputManager2.create_collection(self.dir_path, library_name, col)
        #OutputManager.export_collection(col)


    def create_object(self, obj_name, obj_attributes):
        """
        Creates a new object
        :param obj_name: str - object name
        :param obj_attributes: dictionary of object attributes
        :return: None
        """
        obj = ObjectType(obj_name, obj_attributes)
        self.objects[obj_name] = obj


    def add_object(self, library_name, collection_name, arr):
        """
        Adds an object to a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param arr: array - object values
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        col.add_obj(arr)
        OutputManager2.add_object_to_collection("{}/{}/Collections/{}.csv".format(self.dir_path, library_name, collection_name), arr)


    def remove_library(self, library_name):
        """
        Deletes a library
        :param library_name: str - library name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        OutputManager2.delete_library(self.dir_path + "/" + library_name)
        del self.libraries[library_name]


    def remove_collection_from_library(self, library_name, collection_name):
        """
        Deletes a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        lib.remove_collection(collection_name)
        OutputManager2.delete_collection(self.dir_path + "/" + library_name, collection_name)


    def remove_object_from_collection(self, library_name, collection_name, index):
        """
        Removes an object from a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param index: int - index of the object to be removed
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        col.get_obj(index).destroy_obj()
        path = ""
        OutputManager.export_collection(col, path)


    def sort(self, library_name, collection_name, attribute_name):
        """
        Sorts a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute to which the collection will be sorted
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        obj = col.get_obj_def()
        attr = obj.get_obj_attributes()

        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            print("Attribute %s does not exist." % attribute_name)
            return

        # Create comparator according to the attribute data type
        data_type = obj.get_obj_data_types()[index]
        if data_type == 'str':
            comp = LetterComparator()
        elif data_type == 'int' or 'float':
            comp = NumberComparator()
        elif data_type == 'boolean':
            pass
        else:
            print("Error") # no se supone que ocurra este error

        data = col.get_obj_list()

        sorted_list = Quicksort().sort(data, comp, index)
        temp_collection = Collection('temp', obj)
        for o in sorted_list:
            temp_collection.add_obj(o.get_values())
        col = temp_collection
        del temp_collection
        col.display_col()
        #OutputManager.export_collection(col)



    def search_in_collection(self, library_name, collection_name, attribute_name, data_to_search):
        """
        Search for objects with a given parameter in a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute name
        :param data_to_search: data that the user wishes to search
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)

        attr = col.get_obj_def().get_obj_attributes()
        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            print("Attribute %s does not exist." % attribute_name)
            return

        data = col.get_obj_list()
        result = []
        for obj in data:
            if obj.get_value(index) == data_to_search:
                result.append(obj)

        temp_collection = Collection('temp', col.get_obj_def())
        for o in result:
            temp_collection.add_obj(o.get_values())
        temp_collection.display_col()
        del temp_collection


    def search_in_library(self):
        # What does this do?
        pass


    def show_library(self, library_name):
        """
        Shows all the collection names in a library
        :param library_name: str - library name
        :return:
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        library = self.libraries[library_name]
        collections = library.get_collection_name_list()
        print("Library: %s" % library_name)
        print("Collections:")
        for col in collections:
            print(col)


    def show_collection(self, library_name, collection_name):
        """
        Displays the data inside a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        if not self.library_is_opened(library_name):
            print("Library %s does not exist or is not opened" % library_name)
            return
        lib = self.libraries[library_name]
        collection = lib.get_collection(collection_name)
        collection.display_col()


    def merge(self, lib1, col_name1, lib2, col_name2, new_col_name):
        """
        Merges two collections
        :param lib1: str - library name of collection 1
        :param col_name1: str - collection 1 name
        :param lib2: str - library name of collection 2
        :param col_name2: str - collection 2 name
        :param new_col_name: str - name of the new collection to be created
        :return: None
        """
        if not self.library_is_opened(lib1) or not self.library_is_opened(lib2):
            print("Either library %s or %s do not exist or are not opened" % (lib1, lib2))
            return
        lib1 = self.libraries[lib1]
        lib2 = self.libraries[lib2]

        col1 = lib1.get_collection(col_name1)
        col2 = lib2.get_collection(col_name2)

        # Get object types
        obj1 = col1.get_obj_def()
        obj2 = col2.get_obj_def()

        # Check compatibility
        if self.is_coll_compatible(obj1, obj2):
            newCol = Collection(new_col_name, obj1)
            list1 = col1.get_obj_list()
            for obj in list1:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(v)
                newCol.add_obj(newValues)
            list2 = col2.get_obj_list()
            for obj in list2:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(v)
                newCol.add_obj(newValues)
            # Fix this to output to default directory
            lib1.add_collection(newCol)
            #OutputManager.export_collection(newCol)

        # Not compatible
        else:
            print("Collections %s and %s are not compatible." % (col_name1, col_name2))


    # Not sure if this function is already in another class ??
    def is_coll_compatible(self, obj1, obj2):
        """
        Checks compatibility between two objects.
        That is, that all attributes are exactly the same.
        :param obj1: ObjectType - object 1
        :param obj2: ObjectType - object 2
        :return: boolean - True if objects are compatible
        """
        # Check that attribute names are the same
        attr1 = obj1.get_obj_attributes()
        attr2 = obj2.get_obj_attributes()
        if fabs(len(attr1) - len(attr2)) > 0:
            return False
        for a in range(len(attr1)):
            if attr1[a] is not attr2[a]:
                return False

        # Check that attribute types are the same
        type1 = obj1.get_obj_data_types()
        type2 = obj2.get_obj_data_types()
        for t in range(len(type1)):
            if type1[t] is not type2[t]:
                return False

        return True



    def edit_collection(self, collection_name):
        pass

    def edit_library(self, library_name):
        pass
