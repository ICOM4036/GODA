import Parser as par
from Handler import Handler
import textpool
from Exceptions import *
import os
import time

handler = Handler()

class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "
        self.ds = " "
        self.usercmd = " "
        self.names = {}


def simple_help():
    print(textpool.help_txt)


def cmd_help(cmd):
    if cmd == 'run':
        handler.imp_cmd_help()
    else:
        print(textpool.help_cmd.get(cmd))


def run_cmd(ds):
    msg = " "
    e = " "
    if ds == "cmd":
        print("\t\t\tPlease enter the name of the keyword: \n")
        keys = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the library to which will run the command: \n ")
        lib = par.parser.parse(input("\t\t\t>>>"))
        if keys is not None and lib is not None and 'info' in keys and 'info' in lib:
            msg = "Running command with name: '{0}' ".format(keys['info'])
            e = handler.run_command(keys['info'],lib['info'])
        else:
            msg = "Not able to run command!!"
    else:
        msg = "Not a valid structure!!!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def import_file(ds):
    msg = " "
    e = " "
    if ds == "lib":
        print("\t\t\tPlease enter the name of the file: \n")
        name = par.parser.parse(input("\t\t\t>>>"))
        if name is not None and 'info' in name:
            file = os.path.abspath(name['info'])
            if file is not None:
                msg = "Importing Library from file with name: %s",file
                e = handler.imp_lib(file)
            else:
                msg = "Not a valid operation!!"
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("\t\t\tPlease enter the name of the Library: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the file: \n")
        name = par.parser.parse(input("\t\t\t>>>"))
        if name is not None and 'info' in name:
            file = os.path.abspath(name['info'])
            if file is not None and lib is not None and 'info' in lib:
                msg = "Importing Collection from file: '{0}' into Library: '{1}' ".format(file,lib['info'])
                e = handler.imp_col(file,lib['info'])
            else:
                msg = "Not a valid operation!!"
        else:
            msg = "Not a valid operation!!"
    elif ds == "cmd":
        print("\t\t\tPlease enter the keyword: \n")
        names = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Python file from which to import command: \n ")
        name = par.parser.parse(input("\t\t\t>>>"))
        if name is not None:
            file = os.path.abspath(name['info'])
            if names is not None and file is not None and 'info' in names:
                msg = "Importing Command from file with name: '{0}' with keyword: '{1}' ".format(file,names['info'])
                e = handler.imp_command(names['info'],file)
            else:
                msg = "Not a valid operation!!"
        else:
            msg = "Not a valid operation!!"
    else:
        print("Not a valid operation!!")
    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def export(ds):
    msg = " "
    e = " "
    if ds == "lib":
        print("\t\t\tPlease enter the name of the Library to export: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and 'info' in lib:
            msg = "Exporting Library %s into Desktop", lib['info']
            e = handler.export_library(lib['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("\t\t\tPlease enter the name of the Library: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection to export: \n")
        coll = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and 'info' in lib and 'info' in coll:
            msg = "Exporting Collection with name: '{0}' from Library: '{1}' ".format(coll['info'],lib['info'])
            e = handler.export_colllection(lib['info'],coll['info'])
        else:
            msg = "Not a valid operation!!!"
    else:
        print("Not a valid operation!!")

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def show(ds):
    msg = ""
    e = " "
    if ds == "lib":
        print("\t\t\tPlease enter the name of the Library: \n ")
        names = par.parser.parse(input("\t\t\t>>>"))
        if names is not None and 'info' in names:
            msg = "Showing structure with name: %s" % names['info']
            e = handler.show_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("\t\t\tPlease enter the name of the Library: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection: \n")
        coll = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and 'info' in lib and 'info' in coll:
            msg = "Showing Collection with name: %s" % coll['info']
            e = handler.show_collection(lib['info'], coll['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "all":
        msg = "Showing contents of all open Libraries"
        e = handler.show_all_libraries()
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def delete(ds):
    msg = ""
    e = " "
    if ds == "lib":
        print("\t\t\tPlease enter the name of the Library: \n")
        names = par.parser.parse(input("\t\t\t>>>"))
        if names is not None and 'info' in names:
            msg = "Deleting Library with name: %s" % names['info']
            e = handler.remove_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("\t\t\tPlease enter the name of the Library: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection: \n ")
        coll = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and 'info' in lib and 'info' in coll :
            msg = "Deleting Collection with name: %s" % coll['info']
            e = handler.remove_collection_from_library(lib['info'],coll['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "inst":
        print("\t\t\tPlease enter the name of the Library: \n ")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection: \n")
        coll = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the index: \n")
        index = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and index is not None and'info' in lib and 'info' in coll  and 'info' in index:
            msg = "Deleting Instance with index: %s in Collection: %s" % (index['info'], coll['info'])
            e = handler.remove_object_from_collection(lib['info'],coll['info'],index['info'])
        else:
            msg = "Not a valid operation!!!"
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def create(ds):
    msg = ""
    e = " "
    if ds == "lib":
        print("\t\t\tPlease enter the name of the Library: \n ")
        names = par.parser.parse(input("\t\t\t>>>"))
        if names is not None and 'info' in names:
            msg = "Creating library with name: %s" % names['info']
            e = handler.create_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("\t\t\tPlease enter the name of the Library: \n")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection: \n")
        coll = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Object: \n")
        obj = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and obj is not None and 'info' in lib and 'info' in coll  and 'info' in obj:
            msg = "Creating collection with name: %s with object: %s" % (coll['info'], obj['info'])
            e = handler.create_collection(lib['info'],coll['info'],obj['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "obj":
        list = {}
        print("\t\t\tPlease enter the name of the Object: \n")
        names = par.parser.parse(input("\t\t\t>>>"))
        if names is not None and 'info' in names:
            while True:
                print("\t\t\tPlease enter the value of the key : type \n")
                definition = par.parser.parse(input("\t\t\t>>>"))
                if definition is not None and 'type' in definition:
                    list.update({definition["info"]: definition['type']})
                else:
                    msg = "Not a valid input!! Definition will not be added to object definition!!"
                print("\t\t\tWish to continue?\n")
                u = input("\t\t\t>>>")
                if u == "no":
                    break
                else:
                    continue
            msg = "Creating Object with name: %s with list of attributes: %s" % (names['info'], list)
            e = handler.create_object(names['info'],list)
        else:
            msg = "Not a valid operation!!"
    elif ds == "inst":
        print("\t\t\tPlease enter the name of the Library: \n ")
        lib = par.parser.parse(input("\t\t\t>>>"))
        print("\t\t\tPlease enter the name of the Collection: \n")
        coll = par.parser.parse(input("\t\t\t>>>"))
        if lib is not None and coll is not None and 'info' in lib and  'info' in coll:
            list = []
            obj = handler.get_col_attributes(lib['info'],coll['info'])
            if isinstance(obj, Error):
                e = obj
            else:
                for key in obj:
                    print("\t\t\tPlease enter the value of: \n", key)
                    attr = input("\t\t\t>>>")
                    list.append(attr)
                msg = "Creating instance with in Collection with name: %s with values: %s" % (coll['info'], list)
                e = handler.add_object(lib['info'],coll['info'],list)
        else:
            msg = "Not a valid operation!!!!!!"
    else:
        msg = "Not a valid structure!!!!!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def quit_lib(ds):
    msg = ""
    e = " "
    print("\t\t\tPlease enter the name of the library: \n")
    names = par.parser.parse(input("\t\t\t>>>"))
    if names is not None and 'info' in names:
        msg = "Quiting structure with name: %s" % names['info']
        e = handler.close_library(names['info'])
    else:
        msg = "Not a valid operation!!"
    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def sort():
    msg = ""
    e = " "
    print("\t\t\tPlease enter the name of the Library: \n")
    lib = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the Collection: \n")
    coll = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the attribute to sort by:\n ")
    attri = par.parser.parse(input("\t\t\t>>>"))
    if lib is not None and coll is not None and attri is not None and 'info' in lib and 'info' in coll and 'info' in attri:
        msg = "Sorting Collection with name: %s by attribute: %s" % (coll['info'], attri['info'])
        e = handler.sort(lib['info'],coll['info'],attri['info'])
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def merge():
    msg = " "
    e = " "
    print("\t\t\tPlease enter the name of the first library:\n ")
    lib1 = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the first collection: \n")
    coll1 = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the second library:\n ")
    lib2 = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the second collection: \n")
    coll2 = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the library where the new collection will be placed: \n")
    lib3 = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the new collection:\n ")
    coll3 = par.parser.parse(input("\t\t\t>>>"))
    if lib1 is not None and lib2 is not None and lib3 is not None and coll2 is not None and coll3 is not None and coll1 is not None and 'info' in lib1 and 'info' in lib2 and 'info' in lib3 and 'info' in coll2  and 'info' in coll3  and 'info' in coll1:
            msg = "Merging collection #1: %s with collection #2: %s into new collection with name: %s" % (coll1['info'], coll2['info'], coll3['info'])
            e = handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'],lib3['info'])
    else:
        msg = "Not a valid operation!!"
    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def search():
    msg = ""
    e = " "
    print("\t\t\tPlease enter the name of the Library: \n")
    lib = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the Collection: \n")
    coll = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the name of the attribute to sort by: \n")
    attri = par.parser.parse(input("\t\t\t>>>"))
    print("\t\t\tPlease enter the specific value to search for: \n ")
    value = par.parser.parse(input("\t\t\t>>>"))
    if  lib is not None and coll is not None and attri is not None and value is not None and 'info' in lib and 'info' in coll and 'info' in attri and 'info' in value:
        msg = "Searching collection with name: %s for all entries with value: %s" % (coll['info'], value['info'])
        e = handler.search_in_collection(lib['info'],coll['info'],attri['info'],value['info'])
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def open(ds):
    msg = ""
    e = ""
    if ds == "lib":
        print("\t\t\tPlease enter the name of the library: \n")
        names = par.parser.parse(input("\t\t\t>>>"))
        if names is not None and'info' in names:
            msg = "Opening library with name: %s" % names['info']
            e = handler.openLibrary(names['info'])
        else:
            msg = "Not a valid operation!!"
    else:
        msg = "Not a valid operation!!"
    if isinstance(e, Error):
        msg = e.message()
    print(msg)


if __name__ == '__main__':
    t = Goda()

user_input = {}

os.system('cls')
os.system('color a')
print("\t\t\t\tWELCOME TO GODA     \n")
print('\t\tGENERIC OBJECTIVE DATA ADMINISTRATOR\n')
print('\t\t------------------------------------\n')
print("\t\t\t WE HOPE YOU ENJOY IT!!   \n")

while True:
    print("Please enter desired command:\n")
    user_input = par.parser.parse(input(">>>"))

    if user_input is not None and 'info' not in user_input:

        if user_input['command'] == "help":
            if 'command2' in user_input:
                cmd_help(user_input['command2'])
            else:
                simple_help()
        elif user_input['command'] == "quit":
            if len(user_input) == 1:
                print("\tQuitting Goda \n \tGoodbye!!!")
                time.sleep(3)
                os.system('color f')
                os.system('cls')
                quit()
            else:
                quit_lib(user_input['ds'])
        elif user_input['command'] == "show":
            if 'ds' in user_input:
                show(user_input['ds'])
            elif 'ast' in user_input:
                show(user_input['ast'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "rm":
            if 'ds' in user_input:
                delete(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "crt":
            if 'ds' in user_input:
                create(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "merge":
            if 'ds' in user_input:
                print("{} is not recognized".format(user_input))
            else:
                merge()
        elif user_input['command'] == "search":
            if 'ds' in user_input:
                print("{} is not recognized".format(user_input))
            else:
                search()
        elif user_input['command'] == "sort":
            if 'ds' in user_input:
                print("{} is not recognized".format(user_input))
            else:
                sort()
        elif user_input['command'] == "open":
            if 'ds' in user_input:
                open(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "imp":
            if 'ds' in user_input:
                import_file(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "exp":
            if 'ds' in user_input:
                export(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        elif user_input['command'] == "run":
            if 'ds' in user_input:
                run_cmd(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
        else:
            print("{} is not recognized".format(user_input))
    else:
        print("Please enter a valid command!!!!!")