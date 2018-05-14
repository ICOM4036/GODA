import Parser as par
from Handler import Handler
import InputManager as ip
import textpool
from Exceptions import *
import ImpCmd as ic

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
    print(textpool.help_cmd.get(cmd))


def import_file(ds):
    msg = " "
    e = " "
    if ds == "lib":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Importing Library from file with name: "% names['info']
            e = ip.imp_new_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Importing Collection from file with name: " % names['info']
            e = ip.imp_new_collection(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "inst":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        if names is not None and coll is not None and 'info' in names and 'info' in coll:
            msg = "Importing data from file with name: " % names['info']% " into Collection: "%coll['info']
            e = ip.imp_data(names['info'],coll['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "cmd":
        print("Please enter the keyword: ")
        names = par.parser.parse(input(">>>"))
        print("Please enter the name of the Python file from which to import command: ")
        file = par.parser.parse(input(">>>"))
        if names is not None and file is not None and 'info' in names and 'info' in file:
            msg = "Importing Command from file with name: " % file['info'] % " with keyword: "%names['info']
            e = ic.run_cmd(names['info'],file['info'])
        else:
            msg = "Not a valid operation!!"
    else:
        print("Not a valid operation!!")

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def show(ds):
    msg = ""
    e = " "
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Showing structure with name: %s" % names['info']
            e = handler.show_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        if lib is not None and coll is not None and 'info' in lib and 'info' in coll:
            msg = "Showing Collection with name: %s" % coll['info']
            e = handler.show_collection(lib['info'], coll['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "all":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Showing contents of the Library with name: %s" % names['info']
            e = handler.show_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "liba":
        msg = "Showing contents of all open Libraries"
        #e = handler.show_library(names['info'])
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def delete(ds):
    msg = ""
    e = " "
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Deleting Library with name: %s" % names['info']
            e = handler.remove_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        if lib is not None and coll is not None and 'info' in lib and 'info' in coll :
            msg = "Deleting Collection with name: %s" % coll['info']
            e = handler.remove_collection_from_library(lib['info'],coll['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the index: ")
        index = par.parser.parse(input(">>>"))
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
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            msg = "Creating library with name: %s" % names['info']
            e = handler.create_library(names['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the Object: ")
        obj = par.parser.parse(input(">>>"))
        if lib is not None and coll is not None and obj is not None and 'info' in lib and 'info' in coll  and 'info' in obj:
            msg = "Creating collection with name: %s with object: %s" % (coll['info'], obj['info'])
            e = handler.create_collection(lib['info'],coll['info'],obj['info'])
        else:
            msg = "Not a valid operation!!"
    elif ds == "obj":
        list = {}
        print("Please enter the name of the Object: ")
        names = par.parser.parse(input(">>>"))
        if names is not None and 'info' in names:
            while True:
                print("Please enter the value of the key : type ")
                definition = par.parser.parse(input(">>>"))
                if definition is not None and 'type' in definition:
                    list.update({definition["info"]: definition['type']})
                else:
                    print("Not a valid input!! Definition will not be added to object definition!!")
                print("Wish to continue?")
                u = input(">>>")
                if u == "no":
                    break
                else:
                    continue
            msg = "Creating Object with name: %s with list of attributes: %s" % (names['info'], list)
            e = handler.create_object(names['info'],list)
        else:
            msg = "Not a valid operation!!"
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        if lib is not None and coll is not None and 'info' in lib and  'info' in coll:
            list = []
            obj = handler.get_col_attributes(lib['info'],coll['info'])
            if isinstance(obj, Error):
                e = obj
            else:
                for key in obj:
                    print("Please enter the value of: ", key)
                    attr = input(">>>")
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
    print("Please enter the name of the library: ")
    names = par.parser.parse(input(">>>"))
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
    print("Please enter the name of the Library: ")
    lib = par.parser.parse(input(">>>"))
    print("Please enter the name of the Collection: ")
    coll = par.parser.parse(input(">>>"))
    print("Please enter the name of the attribute to sort by: ")
    attri = par.parser.parse(input(">>>"))
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
    print("Please enter the name of the first library: ")
    lib1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the first collection: ")
    coll1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second library: ")
    lib2 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second collection: ")
    coll2 = par.parser.parse(input(">>>"))
    print("Please enter the name of the library where the new collection will be placed: ")
    lib3 = par.parser.parse(input(">>>"))
    print("Please enter the name of the new collection: ")
    coll3 = par.parser.parse(input(">>>"))
    if lib1 is not None and lib2 is not None and lib3 is not None and coll2 is not None and coll3 is not None and coll1 is not None and 'info' in lib1 and 'info' in lib2 and 'info' in lib3 and 'info' in coll2  and 'info' in coll3  and 'info' in coll1:
            msg = "Merging collection #1: %s with collection #2: %s into new collection with name: %s" % (coll1['info'], coll2['info'], coll3['info'])
            e = handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'],lib3['info'])
    else:
        msg = "Not a valid operation!!"
    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def search(ds):
    msg = ""
    e = " "
    if ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the attribute to sort by: ")
        attri = par.parser.parse(input(">>>"))
        print("Please enter the specific value to search for: ")
        value = par.parser.parse(input(">>>"))
        if  lib is not None and coll is not None and attri is not None and value is not None and 'info' in lib and 'info' in coll and 'info' in attri and 'info' in value:
            msg = "Searching collection with name: %s for all entries with value: %s" % (coll['info'], value['info'])
            e = handler.search_in_collection(lib['info'],coll['info'],attri['info'],value['info'])
        else:
            msg = "Not a valid operation!!"
    else:
        msg = "Not a valid operation!!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def open(ds):
    msg = ""
    e = ""
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
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

print("     Welcome to GODA     \n")
print("     Hope you enjoy it!!   \n")

while True:
    print("Please enter desired command:")
    user_input = par.parser.parse(input(">>>"))

    if user_input is not None and 'info' not in user_input:

        if user_input['command'] == "help":
            if 'command2' in user_input:
                cmd_help(user_input['command2'])
            else:
                simple_help()
        elif user_input['command'] == "quit":
            if len(user_input) == 1:
                quit("\tQuitting Goda \n \tGoodbye!!!")
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
                search(user_input['ds'])
            else:
                print("{} is not recognized".format(user_input))
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
        else:
            print("{} is not recognized".format(user_input))
    else:
        print("Please enter a valid command!!!!!")