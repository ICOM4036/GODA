import os, csv
from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from DataTypes.Library import Library
import InputManager, OutputManager
from Comparators.NumberComparator import NumberComparator

class Handler:

    def __init__(self):

        # This is the default Directory where libraries are saved
        self.dir_path = "C:/Users/irixa/PycharmProjects/GODA/Directory"
        self.libraries = {}
        self.collections = {}
        self.objects = {}


    def openLibrary(self, library_name):

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

        library = InputManager.imp_new_library(library_name)
        self.libraries[library_name] = library
        collections = library.get_collection_list()
        # LOL this is not efficient!!!!!
        for col in collections:
            self.collections[col.get_name] = col


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


    def removeObjectFromLibrary(self, library, object):
        pass

    def createCollection(self, coll_name):
        pass

    def addCollectionToLibrary(self, library, collection):
        pass

    def removeCollectionFromLibrary(self, library, collection):
        pass





    def sort(self, collection_name, attribute_name):
        coll = self.collections[collection_name]


        # coll = Collection(coll, obj)
        # # if attribute_name.type = int:
        # #     comp = NumberComparator()
        # comp = Comparator()
        # quicksort(coll.get_obj_list())

        OutputManager.export_collection(coll)


    def quicksort(self, array, comp, index):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if comp.compare(x[index], pivot[index]) < 0:
                    less.append(x)
                elif comp.compare(x[index], pivot[index]) > 0:
                    greater.append(x)
                else:
                    equal.append(x)
            return self.quicksort(less, comp, index) + equal + self.quicksort(greater, comp, index)
        else:
            return array


    def show_library(self, library_name):
        library = self.libraries[library_name]
        collections = library.get_collection_list()
        for col in collections:
            show_collection(col)


    def show_collection(self, collection_name):
        collection = self.collections[collection_name]
        collection.display_col()


    def merge(self, collection1, collection2):
        pass

    def edit_collection(self, collection_name):
        pass

    def edit_library(self, library_name):
        pass
