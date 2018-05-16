"""
    OUTPUT MANAGER
    - WRITE FILES
    - EXPORT FILES
    - MANAGE OUTPUT
"""
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

    # Write library name to libraries text file in Directory
    libtxtfile = open('{}/libraries.txt'.format(dir_path), 'a', newline='')
    libtxtfile.write("%s\n" % library_name)
    libtxtfile.close()


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
    open(lib_path + "/Collections/" + collection.get_name() + ".csv", 'w')


def add_object_to_collection(col_path, obj_values):
    file_writer = csv.writer(open(col_path, 'a', newline = ''))
    file_writer.writerow(obj_values)


def delete_library(dir_path, lib_name):
    try:
        shutil.rmtree('%s/%s' % (dir_path, lib_name))
    except Exception:
        return LibraryDoesNotExistError(lib_name)

    # Delete collection file path from library text file
    txtfile = open("%s/libraries.txt" % dir_path, 'r')
    textreader = txtfile.read().split("\n")
    del textreader[len(textreader) - 1]
    new_txtfile = []
    for line in textreader:
        if not line == lib_name:
            new_txtfile.append(line)

    txtfile.close()
    txtfile = open("%s/libraries.txt" % dir_path, 'w+')
    for line in new_txtfile:
        txtfile.write(line + "\n")


def delete_collection(lib_path, lib_name, collection_name):
    try:
        path1 = "{}/{}.txt".format(lib_path, collection_name)
        os.remove(path1)
        path2 = "{}/Collections/{}.csv".format(lib_path, collection_name)
        os.remove(path2)

        # Delete collection file path from library text file
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
        return CollectionDoesNotExistError(collection_name)


def save_library(library):
    """
    SAVE A LIBRARY IN PROJECT FILES
    :param library: LIBRARY - LIBRARY TO BE SAVED
    :return: VOID
    """
    directory = 'Directory'
    export_library(library, directory)


def exp_lib_aux(lib):
    """
    EXPORT A LIBRARY TO DESKTOP
    :param library: LIBRARY - LIBRARY TO BE EXPORTED
    :return: VOID
    """
    userpath = os.path.expanduser('~')
    path = userpath+'/Desktop'
    export_library(lib, path)


def export_library(library, directory):
    """
    EXPORT A LIBRARY TO A SPECIFIED DIRECTORY
    :param library: LIBRARY - LIBRARY TO BE EXPORTED
    :param directory: STRING - DIRECTORY WHERE LIBRARY WILL BE EXPORTED TO
    :return: VOID
    """
    collections = library.get_collection_list()
    directory = directory+'/'+library.get_name()
    if not os.path.exists(directory):
        os.makedirs(directory)

    cl = open(directory+'/'+library.get_name()+'.txt', 'w+')
    cl.write(library.get_name()+'\n')
    for c in collections:
        cl.write(directory+'/'+c.get_name()+'.txt\n')
        f = open(directory+'/'+c.get_name()+'.txt', 'w+')
        f.write(directory+'/Collections/'+c.get_name()+'.csv\n'
                +c.get_name()+'\n'
                +c.get_obj_def().get_obj_type()+'\n')
        a = c.get_obj_def().get_obj_attributes()
        d = c.get_obj_def().get_obj_data_types()
        for i in range(0, len(a)):
            f.write(a[i]+':'+str(d[i]).split("'")[1])
            if i < len(a)-1:
                f.write(',')
        f.close()
        export_collection(c, directory+'/Collections')
    cl.close()


def exp_col_aux(col):
    """
    EXPORT A COLLECTION IN PROJECT FILES
    :param library: LIBRARY - COLLECTION TO BE EXPORTED
    :return: VOID
    """
    userpath = os.path.expanduser('~')
    path = userpath+'/Desktop'
    export_collection(col, path)


def export_collection(collection, directory):
    """
    EXPORT A COLLECTION TO A SPECIFIED DIRECTORY
    :param collection: COLLECTION - COLLECTION TO BE EXPORTED
    :param directory: STRING - DIRECTORY WHERE COLLECTION WILL BE EXPORTED TO
    :return:
    """
    colname = collection.get_name()
    objs = collection.get_obj_list()
    if not os.path.exists(directory):
        os.makedirs(directory)
    f = open(directory+'/'+colname+'.csv', "w+")
    for x in objs:
        val = x.get_values()
        for a in range(0, len(val)):
            f.write(str(val[a]))
            if a < len(val)-1:
                f.write(',')
        f.write('\n')
    f.close()

