"""
    INPUT MANAGER:
    - READ FILES
    - IMPORT FILES
    - MANAGE INPUT
"""
from ADT.Library import *
from ADT.Collection import *
from ADT.ObjectType import *
import csv
import os
import Exceptions


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
                if row[a] == 'None':
                    values.append(None)
                elif attribute_types[a] is str:
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


def get_library_names(dir_path):
    filereader = open("%s/libraries.txt" % dir_path, 'r')
    libraries = filereader.read().split("\n")
    return libraries


def imp_new_collection(filename):
    """
    IMPORT A NEW COLLECTION
    :param filename: STRING - FILE NAME
    :return: COLLECTION - NEW COLLECTION
    """
    try:
        f = open(filename, 'r+')
        colfile = f.readline().replace('\n', '')
        colname = f.readline().replace('\n', '')
        objtype = f.readline().replace('\n', '')
        objatt = f.readline().replace('\n', '').split(',')
        attdef = {}
        for a in objatt:
            v = a.split(':')
            attdef.__setitem__(v[0], v[1])
        odef = ObjectType(objtype, attdef)
        c = Collection(colname, odef)
        f.close()
        imp_data(colfile, c)
        return c
    except FileNotFoundError:
        print('Something went wrong while importing ', filename, '.',
              '\nPlease make sure that the file exists and that its format is correct.')
        return None


def imp_data(filename, col):
    """
    IMPORT DATA TO A COLLECTION
    :param filename: STRING - FILE NAME
    :param col: COLLECTION - COLLECTION TO WHICH DATA WILL BE IMPORTED
    :return: VOID
    """
    try:
        odt = col.get_obj_def().get_obj_data_types()
        with open(filename) as f:
            data = csv.reader(f, delimiter=',')
            for line in data:
                obj = []
                for i in range(0, len(line)):
                    t = str(odt[i]).split("'")[1]
                    if line[i] == "None":
                        obj.append(None)
                    elif t == "int":
                        obj.append(int(line[i]))
                    elif t == "float":
                        obj.append(float(line[i]))
                    else:
                        obj.append(line[i])
                col.add_obj(obj)
            f.close()
    except FileNotFoundError:
        print('Something went wrong while importing ', filename, '.',
              '\nPlease make sure that the file exists and that its format is correct.')


def imp_new_library(filename):
    """
    IMPORT A NEW LIBRARY
    :param filename: STRING - FILE NAME
    :return: LIBRARY - NEW LIBRARY
    """
    try:
        f = open(filename, 'r+')
        liblist = []
        for line in f:
            liblist.append(line.replace('\n', ''))
        lib = Library(liblist[0])
        for c in range(1, len(liblist)):
            col = imp_new_collection(liblist[c])
            lib.add_collection(col)
        f.close()
        return lib
    except FileNotFoundError:
        print('Something went wrong while importing ', filename, '.',
              '\nPlease make sure that the file exists and that its format is correct.')
        return None


def imp_cmd(cmd_name, pyfile):
    """
    IMPORT COMMAND
    :param cmd_name: STRING - COMMAND NAME
    :param pyfile: STRING - PATH OF ALGORITHM
    :return: VOID
    """
    try:
        pyname = os.path.basename(pyfile)
        cmd_dir = r'ImportedCommands/'+pyname
        mod_name = pyname.replace(".py", "")
        f1 = open(pyfile, 'r+')
        f2 = open(cmd_dir, 'w+')
        lines = f1.readlines()
        for line in lines:
            f2.write(line)
        f1.close()
        f2.close()
        f3 = open('ImpCmd.py', 'r+')
        cmd_par = f3.readlines()
        f3.close()
        f4 = open('ImpCmd.py', 'w+')
        for line in cmd_par:
            if "# imports" in line:
                f4.write(line)
                f4.write('import ImportedCommands.{} as {}\n'.format(mod_name, mod_name))
            elif "# cmds" in line:
                f4.write(line+'\n')
                f4.write('    elif cmd is "{}":\n'.format(cmd_name))
                f4.write('        return {}.main(lib)\n'.format(mod_name))
            else:
                f4.write(line)
        f4.close()
    except Exception:
        FileNotFoundError(pyfile)




