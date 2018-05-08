import os, csv
from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from DataTypes.Library import Library
'import InputManager, OutputManager, OutputManager2'
from Comparators.NumberComparator import NumberComparator
import SortingAlgorithms.Quicksort
from math import fabs

class Handler:

    def __init__(self):

        # This is the default Directory where libraries are saved
        self.dir_path = "C:/Users/crysm/PycharmProjects/GODA/Directory"
        self.libraries = {}
        self.collections = {}
        self.objects = {}


    def openLibrary(self, library_name):

         library_path = "{}/{}".format(self.dir_path, library_name)

         try:
             # Open list with collections in library
             with open("{}/{}.txt".format(library_path, library_name), 'wb') as csvfile:
                 library_reader = csv.reader(csvfile, delimiter=",", quotechar="|")

             for coll in library_reader:
                 # Open collection text
                 with open("{}/{}.txt".format(library_path, coll), 'wb') as csvfile:
                     collection_reader = csv.reader(csvfile, delimiter=",", quotechar="|")
                     coll_name = collection_reader.nextLine
                     obj_name = nextLine
                     if object_name is not in self.objects:
                         obj_attributes = nextLine
                         object = ObjectType().__init__(obj_name, obj_attributes)
                         self.objects.append(object)
                     collection

             # Open Collection List
             with open("{}/{}/CollectionsList.csv".format(self.dir_path, library_name), 'wb') as csvfile:
                 collection_reader = csv.reader(csvfile, delimiter=",", quotechar="|")

             for row in collection_reader:
                 createCollection(row)


         except Error:
             pass

        library = InputManager.imp_new_library(library_name)
        self.libraries[library_name] = library
        collections = library.get_collection_list()
        # LOL this is not efficient!!!!!
        for col in collections:
            self.collections[col.get_name] = col


     def createLibraryDirectory(self, library_name):

         # Create a directory with the library's name
         library_path = "%s/%s" % (self.dir_path, library_name)

         try:
             os.makedirs(library_path)
         except OSError as e:
             print("A library with that name already exists")
             return

         # Create an ObjectList csv file
         with open('{}/ObjectsList.csv'.format(library_path), 'wb') as csvfile:
             filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

         # Create a CollectionsList csv file
         with open('{}/CollectionsList.csv'.format(library_path), 'wb') as csvfile:
             filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

         # Create an ImportedCommandsList csv file
         with open('{}/ImportedCommandsList.csv'.format(library_path), 'wb') as csvfile:
             filewriter = csv.writer(csvfile, delimiter=",", quotechar="|", quoting=csv.QUOTE_MINIMAL)

         # Create a subdirectory to contain all collections
         coll_path = "{}/Collections".format(library_path)
         os.makedirs(coll_path)




    def createObject(self, obj_string):
         """
         Crea un objeto con la clase OjectType
         :param str:
         :return:
         """

         type = obj_string[0]
         attributes = []
         for s in range(len(obj_string) - 1):
             attributes.append(obj_string[s + 1])
         new_object = ObjectType(type, self.mapAttributesToDict(attributes))

         self.objects[type] = new_object


    def mapAttributesToDict(self, attributes):
         dict = {}
         for a in attributes:
             dict[a] = None
         return dict


    def createLibrary(self, library_name):

         lib = Library(library_name)
         self.libraries[library_name] = lib



    def addObjectToLibrary(self, library, object):
         library_path = "{}/{}".format(self.dir_path, library)

         #Open ObjectsList file
         filewriter = csv.writer(open ('{}/ObjectsList.csv'.format(library_path), 'w'))

         #Append the object to ObjectsList file
         filewriter.writerow(object)

         self.createObject(object)


    def create_library(self, library_name):
        OutputManager.save_library(library_name)
        self.openLibrary(library_name)


    def create_collection(self, library_name, collection_name, object_type):
        lib = self.libraries[library_name]
        obj_type = self.object[object_type]
        col = Collection(collection_name, obj_type)
        lib.add_collection(col)



    def create_object(self, obj_name, obj_attributes):
        pass




    def remove_library(self, library_name):
        OutputManager2.delete_library(library_name)


    def remove_collection_from_library(self, library_name, collection_name):
        lib = self.libraries[library_name]
        lib.remove_collection(collection_name)
        OutputManager2.delete_collection(library_name, collection_name)


    def remove_object_from_collection(self, library_name, collection_name, object):
        # Cual se supone que sea el parametro de object??
        pass





    def sort(self, library_name, collection_name, attribute_name):
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        obj = col.get_obj_def
        # index = obj.

        # coll = Collection(coll, obj)
        # # if attribute_name.type = int:
        # #     comp = NumberComparator()
        # comp = Comparator()
        # quicksort(coll.get_obj_list())

        col = Quicksort.sort(coll, comp, index)
        OutputManager.export_collection(coll)



    def search_in_collection(self, library_name, collection_name, attribute, data_to_search):
        lib = self.libraries[library_name]
        col = lib.get_collection(collection_name)
        data = col.get_obj_list()
        result = []
        for row in data:
            if row[attribute] == data_to_search:
                result.append(row)
        print(result)


    def search_in_library(self):
        # What does this do?


    def show_library(self, library_name):
        library = self.libraries[library_name]
        collections = library.get_collection_name_list()
        for col in collections:
            print(col)


    def show_collection(self, library_name, collection_name):
        lib = self.libraries[library_name]
        collection = lib.get_collection(collection_name)
        collection.display_col()


    def merge(self, lib1, col_name1, lib2, col_name2, new_col_name):
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
                newCol.add_obj(obj.get_values())
            list2 = col2.get_obj_list()
            for obj in list2:
                newCol.add_obj(obj.get_values())
            # Fix this to output to default directory
            OutputManager.export_collection(newCol)

        # Not compatible
        else:
            print("Collections %s and %s are not compatible." % (col_name1, col_name2))


    # Not sure if this function is already in another class ??
    def is_coll_compatible(self, obj1, obj2):
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
