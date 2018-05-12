import os, shutil
import csv
from Exceptions import *

def create_library(dir_path, library_name):

    library_path = "{}/{}".format(dir_path, library_name)
    try:
        os.makedirs(library_path)
    except Exception:
        return LibraryExistsError(library_name)

    # Create a CollectionsList text file
    txtfile = open('{}/{}.txt'.format(library_path, library_name), 'w')
    txtfile.close()

    # Create a subdirectory to contain all collections
    coll_path = "{}/Collections".format(library_path)
    os.makedirs(coll_path)


def create_collection(dir_path, library_name, collection):

    lib_path = "{}/{}".format(dir_path, library_name)

    # Check if a collection with that name exists
    if os.path.isfile("%s/%s.txt" % (lib_path, collection.get_name())):
        print("Collection %s already exists in library" % collection.get_name())
        return

    # Check if library path is valid
    if not os.path.isdir(lib_path):
        print("Library does not exist.")
        return

    # Write the collection name in library text file
    txtfile = open("%s/%s.txt" % (lib_path, library_name), 'a')
    txtfile.write("{}/{}.txt\n".format(lib_path, collection.get_name()))
    txtfile.close()

    # Create a text file with the collection details
    colfile = open("%s/%s.txt" % (lib_path, collection.get_name()), 'w')
    colfile.write("{}/Collections/{}.csv".format(lib_path, collection.get_name()))
    colfile.write("\n" + collection.get_name())
    colfile.write("\n" + collection.get_obj_def().get_obj_type())
    colfile.write("\n" + collection.get_obj_def().get_obj_att_string())
    colfile.close()

    # Create a csv file where the collection objects will be written
    open(lib_path + "/Collections/" + collection.get_name() + ".csv", 'w').close()

def add_object_to_collection(col_path, obj_values):
    file_writer = csv.writer(open(col_path, 'a', newline = ''))
    file_writer.writerow(obj_values)

def delete_library(lib_path):
    try:
        shutil.rmtree(lib_path)
    except Exception:
        print("Cannot delete library. Library does not exist.")


def delete_collection(lib_path, lib_name, collection_name):
    try:
        path1 = "{}/{}.txt".format(lib_path, collection_name)
        os.remove(path1)
        path2 = "{}/Collections/{}.csv".format(lib_path, collection_name)
        os.remove(path2)

        txtfile = open("%s/%s.txt" % (lib_path, lib_name), 'r')
        textreader = txtfile.read().split("\n")
        del textreader[len(textreader) - 1]
        new_txtfile = []
        for line in textreader:
            if not line == path1:
                new_txtfile.append(line)

        txtfile.close()
        txtfile = open("%s/%s.txt" % (lib_path, lib_name), 'w+')
        for line in new_txtfile:
            txtfile.write(line + "\n")


    except Exception:
        print("Cannot delete collection %s. Collection does not exist." % collection_name)