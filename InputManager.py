"""
    INPUT MANAGER:
    - READ FILES
    - IMPORT FILES
    - MANAGE INPUT
"""
from DataTypes.Library import *
from DataTypes.Collection import *
from DataTypes.ObjectType import *
import csv
import os


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
    except FileNotFoundError:
        print("nope")





