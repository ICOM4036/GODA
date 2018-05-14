import os, csv
from ADT.Library import Library
from Exceptions import *


def import_library(lib_path, lib_name):
    if not os.path.isdir(lib_path):
        return LibraryDoesNotExistError(lib_name)

    # Create a library
    lib = Library(lib_name)

    filereader = open("{}/{}.txt".format(lib_path, lib_name), 'r')
    coll_files = filereader.read()
    # Every row is the path of a collection
    coll_files = coll_files.split("\n")
    # delete last line which is empty
    del coll_files[len(coll_files) - 1]
    for row in coll_files:
        # Open file with collection info
        coll_file = open(row, 'r')
        arr = coll_file.read().split("\n")
        # First line is the path of the file with the data
        coll_path = arr[0]
        # Second line is the name of the collection
        coll_name = arr[1]
        # Third line is the name of the object
        coll_obj_type = arr[2]
        # Fourth line are the attributes of the object
        coll_obj_att = arr[3]

        # Convert the object attributes to a string
        att = coll_obj_att.split(",")
        att_dict = {}
        for a in att:
            split = a.split(":")
            att_dict[split[0]] = split[1]

        # Create collection and add it to library
        lib.create_collection(coll_name, coll_obj_type, att_dict)
        col = lib.get_collection(coll_name)
        data_types = col.get_obj_def().get_obj_data_types()
        col = import_collection(coll_path, col, data_types)

    return lib

def import_collection(coll_path, col, attribute_types):
    # Open csv file and add objects to collection
    with open(coll_path, newline='') as csvfile:
        coll_reader = csv.reader(csvfile)
        # Change the string values to types
        for row in coll_reader:
            values = []
            for a in range(len(attribute_types)):
                if attribute_types[a] is str:
                    values.append(row[a])
                elif attribute_types[a] is bool:
                    if row[a] == 'True':
                        values.append(True)
                    elif row[a] == 'False':
                        values.append(False)
                    else:
                        values.append(None)
                elif attribute_types[a] is int:
                    values.append(int(row[a]))
                elif attribute_types[a] is float:
                    values.append(float(row[a]))
                else:
                    values.append(None)
            col.add_obj(values)
    return col