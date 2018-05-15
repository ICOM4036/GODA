import os, csv
from ADT.ObjectType import ObjectType
from ADT.Collection import Collection
from ADT.Library import Library
import InputManager, OutputManager, InputManager2, OutputManager2, ImpCmd
from Comparators.NumberComparator import NumberComparator
from Comparators.LetterComparator import LetterComparator
from Comparators.BooleanComparator import BooleanComparator
from SortingAlgorithms.Quicksort import Quicksort
from math import fabs
from Exceptions import *
import importlib


class Handler:

    def __init__(self):

        # This is the default Directory where libraries are saved
        self.dir_path = "Directory"
        self.libraries = {}
        self.objects = {}


    def openLibrary(self, library_name):
        """
        Creates an instance of a library so that a user can
        use commands to manage it
        :param library_name: str - library name
        :return: None
        """

        if library_name in self.libraries:
            return LibraryOpenedError(library_name)

        # library = InputManager2.import_library(self.dir_path + "/" + library_name, library_name)
        library = InputManager.imp_new_library('Directory/'+library_name)

        if isinstance(library, Error):
            return library

        self.libraries[library_name] = library
        collections = library.get_collection_list()
        for col in collections:
            obj = col.get_obj_def().get_obj_type()
            if not obj in self.objects:
                self.objects[obj] = col.get_obj_def()


    def close_library(self, library_name):
        """
        Deletes the instance of an opened library
        :param library_name: str - library name
        :return: None
        """
        try:
            del self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)


    def create_library(self, library_name):
        """
        Creates a new library
        :param library_name: str - library name
        :return: None
        """
        e = OutputManager2.create_library(self.dir_path, library_name)
        # If library exists OutputManager returns an error
        if isinstance(e, Error):
            return e


    def create_collection(self, library_name, collection_name, object_type):
        """
        Creates a new collection and adds it to a library
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param object_type: str - name of the object type
        :return:
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        try:
            obj_type = self.objects[object_type]
        except Exception:
            return ObjectDoesNotExistError(object_type)

        col = Collection(collection_name, obj_type)
        e = lib.add_collection(col)
        # If collection already exists Library returns an error
        if isinstance(e, Error):
            return e
        else:
            OutputManager2.create_collection(self.dir_path, library_name, col)


    def create_object(self, obj_name, obj_attributes):
        """
        Creates a new object
        :param obj_name: str - object name
        :param obj_attributes: dictionary of object attributes
        :return: None
        """
        if obj_name in self.objects:
            return ObjectExistsError(obj_name)

        obj = ObjectType(obj_name, obj_attributes)
        self.objects[obj_name] = obj


    def add_object(self, library_name, collection_name, arr):
        """
        Adds an object to a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param arr: str[] - object values
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col
        data_types = col.get_obj_def().get_obj_data_types()
        values = []
        for i in range(len(arr)):
            try:
                if arr[i] == 'None':
                    values.append(None)
                elif data_types[i] is bool:
                    if arr[i] == 'True':
                        values.append(True)
                    else:
                        values.append(False)
                elif data_types[i] is str:
                    values.append(arr[i])
                elif data_types[i] is int:
                    values.append(int(arr[i]))
                elif data_types[i] is float:
                    values.append(float(arr[i]))
                else:
                    values.append(None)
            except Exception:
                return ObjectNotCompatibleError()

        col.add_obj(values)
        OutputManager2.add_object_to_collection("{}/{}/Collections/{}.csv".format(self.dir_path, library_name, collection_name), arr)


    def imp_lib(self, filename):
        """
        Import an external library to the default directory
        :param filename: str - path of the library directory
        :return:
        """
        library_name = os.path.basename(filename)
        # e = InputManager.import_library(filename, library_name)
        e = InputManager.imp_new_library(filename)
        OutputManager2.create_library(self.dir_path, library_name)
        OutputManager.save_library(e)
        return e


    def imp_col(self, file_path, library_name):
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        try:
            filereader = open(file_path, 'r')
        except Exception:
            return FileNotFoundError(file_path)

        file = filereader.read().split("\n")
        # Path of file with data
        col_path = file[0]
        # Name of collection
        col_name = file[1]
        # Name of object
        obj_name = file[2]
        # Object attributes
        obj_attr = file[3]

        # Convert the object attributes to a string
        att = obj_attr.split(",")
        att_dict = {}
        for a in att:
            split = a.split(":")
            att_dict[split[0]] = split[1]

        obj = ObjectType(obj_name, att_dict)
        data_types = obj.get_obj_data_types()
        try:
            col = InputManager.import_collection(col_path, Collection(col_name, obj), data_types)
        except Exception:
            return FileNotFoundError(col_path)

        lib.add_collection(col)
        OutputManager2.create_collection(self.dir_path, library_name, col)


    def imp_command(self, command_name, pyfile):
        print('Please enter a description for "{}" command.'.format(command_name))
        cmd_des = input('>>>')+' '
        e = InputManager.imp_cmd(command_name, pyfile, cmd_des)
        return e


    def imp_cmd_help(self):
        help = ''
        try:
            c = open('ImportedCommands/ImportedCommands.txt', 'r')
            lines = c.readlines()
            c.close()
            for line in lines:
                line = line.split('{cmd+des}')
                help += line[0] + '\t\t' + line[1]
            print('Imported Commands help\n{}'.format(help))
        except:
            pass


    def run_command(self, command_name, library_name):
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        try:
            import ImpCmd as impcmd
            impcmd = importlib.reload(ImpCmd)
            impcmd.run_cmd(command_name, lib)
        except Exception:
            CommandNotFoundError(command_name)


    def remove_library(self, library_name):
        """
        Deletes a library
        :param library_name: str - library name
        :return: None
        """
        e = OutputManager2.delete_library(self.dir_path, library_name)
        if isinstance(e, Error):
            return e
        try:
            del self.libraries[library_name]
        except Exception:
            pass


    def remove_collection_from_library(self, library_name, collection_name):
        """
        Deletes a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        e = lib.remove_collection(collection_name)
        if isinstance(e, Error):
            return e
        OutputManager2.delete_collection(self.dir_path + "/" + library_name, library_name, collection_name)


    def remove_object_from_collection(self, library_name, collection_name, index):
        """
        Removes an object from a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param index: int - index of the object to be removed
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col
        index = int(index)
        if index >= col.col_size():
            return ObjectIndexOutOfBound(str(index))

        col.remove_obj(index)
        OutputManager2.delete_collection(self.dir_path + "/" + library_name, library_name, collection_name)
        OutputManager2.create_collection(self.dir_path, library_name, col)


    def export_library(self, library_name, filepath):
        """
        Export existing library to a given path
        :param library_name: str - library name
        :param filepath: srt - path of file to export to
        :return:
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)
        OutputManager.export_library(lib, filepath)


    def export_collection(self, library_name, collection_name, filepath):
        """
        Export an existing collection to a given path
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param filepath: srt - path of file to export to
        :return:
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)
        col = lib.get_collection(collection_name)
        # Collection does not exist
        if isinstance(col, Error):
            return col
        OutputManager.export_collection(col, filepath)


    def sort(self, library_name, collection_name, attribute_name):
        """
        Sorts a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute to which the collection will be sorted
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col

        obj = col.get_obj_def()
        attr = obj.get_obj_attributes()

        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            return AttributeDoesNotExistError(attribute_name)

        # Create comparator according to the attribute data type
        data_type = obj.get_obj_data_types()[index]
        # Data type is a string
        if data_type is str:
            comp = LetterComparator()
        # Data type is either an int or a float
        elif data_type is (int or float): #type(data_type) is (type(int) or type(float)):
            comp = NumberComparator()
        # Data type is boolean
        elif data_type is bool:#type(data_type) is type(bool):
            comp = BooleanComparator()
        else:
            print("Error") # no se supone que ocurra este error
            return

        data = col.get_obj_list()

        sorted_list = Quicksort().sort(data, comp, index)
        temp_collection = Collection('{} sorted by {}'.format(collection_name, attribute_name), obj)
        for o in sorted_list:
            temp_collection.add_obj(o.get_values())
        col = temp_collection
        del temp_collection
        col.display_col()


    def search_in_collection(self, library_name, collection_name, attribute_name, data_to_search):
        """
        Search for objects with a given parameter in a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :param attribute_name: str - attribute name
        :param data_to_search: data that the user wishes to search
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col

        attr = col.get_obj_def().get_obj_attributes()
        # Get the attribute index in the object array
        index = -1
        for a in range(len(attr)):
            if attr[a] == attribute_name:
                index = a
                break
        if index == -1:
            return AttributeDoesNotExistError(attribute_name)

        # Change the string of the data to search to its type
        data_type = col.get_obj_def().get_obj_data_types()
        type = data_type[index]
        if type is int:
            data_to_search = int(data_to_search)
        elif type is float:
            data_to_search = float(data_to_search)
        elif type is bool:
            if data_to_search == 'True':
                data_to_search = True
            elif data_to_search == 'False':
                data_to_search = False
            else:
                data_to_search = None
        elif type is str:
            pass
        else:
            data_to_search = None

        data = col.get_obj_list()
        result = []
        for obj in data:
            if obj.get_value(index) == data_to_search:
                result.append(obj)

        temp_collection = Collection('{} with {} as {}'.format(collection_name, attribute_name, data_to_search), col.get_obj_def())
        for o in result:
            temp_collection.add_obj(o.get_values())
        temp_collection.display_col()
        del temp_collection


    def show_all_libraries(self):
        libraries = InputManager2.get_library_names(self.dir_path)
        for l in libraries:
            print(l)


    def show_library(self, library_name):
        """
        Shows all the collection names in a library
        :param library_name: str - library name
        :return:
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        lib.display_lib()


    def show_collection(self, library_name, collection_name):
        """
        Displays the data inside a collection
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col

        col.display_col()


    def show_all_in_library(self, library_name):
        """
        Display all the collections in a library with corresponding data
        :param library_name: str - library name
        :return: None
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        lib.display_all_lib()


    def merge(self, lib_name1, col_name1, lib_name2, col_name2, new_col_name, lib_name3):
        """
        Merges two collections
        :param lib_name1: str - library name of collection 1
        :param col_name1: str - collection 1 name
        :param lib_name2: str - library name of collection 2
        :param col_name2: str - collection 2 name
        :param new_col_name: str - name of the new collection to be created
        :param lib1: str - library name where new collection will be saved
        :return: None
        """
        try:
            lib1 = self.libraries[lib_name1]
        except Exception:
            return LibraryNotOpenedError(lib_name1)
        try:
            lib2 = self.libraries[lib_name2]
        except Exception:
            return LibraryNotOpenedError(lib_name2)
        try:
            lib3 = self.libraries[lib_name3]
        except Exception:
            return LibraryNotOpenedError(lib_name3)

        col1 = lib1.get_collection(col_name1)
        if isinstance(col1, Error):
            return col1

        col2 = lib2.get_collection(col_name2)
        if isinstance(col2, Error):
            return col2

        # Get object types
        obj1 = col1.get_obj_def()
        obj2 = col2.get_obj_def()

        # Check compatibility
        if self.is_coll_compatible(obj1, obj2):
            self.create_collection(lib_name3, new_col_name, obj1.get_obj_type())
            # lib3.create_collection(new_col_name, obj1.get_obj_type(), obj1.get_obj_att_dict())
            # OutputManager2.create_collection(self.dir_path, lib_name3, new_col)
            # Append objects in collection 1
            list1 = col1.get_obj_list()
            for obj in list1:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(str(v))
                # new_col.add_obj(newValues)
                # OutputManager2.add_object_to_collection("{}/{}/Collections/{}.csv".format(self.dir_path, lib_name3,
                #                                                                           new_col_name), newValues)
                self.add_object(lib_name3, new_col_name, newValues)
            # Append objects in collection 2
            list2 = col2.get_obj_list()
            for obj in list2:
                newValues = []
                values = obj.get_values()
                for v in values:
                    newValues.append(str(v))
                # new_col.add_obj(newValues)
                # OutputManager2.add_object_to_collection("{}/{}/Collections/{}.csv".format(self.dir_path, lib_name3,
                #                                                                           new_col_name), newValues)
                self.add_object(lib_name3, new_col_name, newValues)

        # Not compatible
        else:
            return CollectionsNotCompatibleError(col_name1, col_name2)

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

    def get_col_attributes(self, library_name, collection_name):
        """
        Get a list of object attributes
        :param library_name: str - library name
        :param collection_name: str - collection name
        :return: str[] - list of object attributes
        """
        try:
            lib = self.libraries[library_name]
        except Exception:
            return LibraryNotOpenedError(library_name)

        col = lib.get_collection(collection_name)
        if isinstance(col, Error):
            return col

        obj = col.get_obj_def()
        obj_attributes = obj.get_obj_attributes()
        return obj_attributes
