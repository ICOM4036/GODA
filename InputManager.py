"""
    INPUT MANAGER:
    - READ FILES
    - IMPORT FILES
    - MANAGE INPUT
"""
from Library import Library
from Collection import Collection
from ObjectType import ObjectType
import csv


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
                    if odt[i] == "int":
                        obj.append(int(line[i]))
                    elif odt[i] == "float":
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
            col = imp_new_collection(liblist[c].replace('\n', ''))
            lib.add_collection(col)
        f.close()
        return lib
    except FileNotFoundError:
        print('Something went wrong while importing ', filename, '.',
              '\nPlease make sure that the file exists and that its format is correct.')
        return None
