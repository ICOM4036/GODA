import Parser as par
from Handler import Handler
import InputManager as ip
import textpool
from Exceptions import *

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
    if ds == "lib":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        print("Importing Library from file with name: ", names['info'])
        ip.imp_new_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the file: ")
        coll = par.parser.parse(input(">>>"))
        print("Importing Collection from file with name: ", coll['info'])
        ip.imp_new_collection(coll['info'])
    elif ds == "inst":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Importing data from file with name: ", names['info'], " into Collection: ",coll['info'])
        ip.imp_data(names['info'],coll['info'])
    else:
        print("Not a valid operation!!")


def show(ds):
    msg = ""
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        msg = "Showing structure with name: " + names['info']
        e = handler.show_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        msg = "Showing Collection with name: " + coll['info']
        e = handler.show_collection(lib['info'], coll['info'])
    elif ds == "all":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        msg = "Showing contents of the Library with name: " + names['info']
        e = handler.show_library(names['info'])
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def delete(ds):
    msg = ""
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        msg = "Deleting Library with name: " + names['info']
        e = handler.remove_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        msg = "Deleting Collection with name: " + coll['info']
        e = handler.remove_collection_from_library(lib['info'],coll['info'])
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the index: ")
        index = par.parser.parse(input(">>>"))
        msg = "Deleting Instance with index: " + index['info'] + " in Collection: " + coll['info']
        e = handler.remove_object_from_collection(lib['info'],coll['info'],index['info'])
    else:
        msg = "Not a valid operation!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def create(ds):
    msg = ""
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        msg = "Creating library with name: " + names['info']
        e = handler.create_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the Object: ")
        obj = par.parser.parse(input(">>>"))
        msg = "Creating collection with name: " + coll['info'] + " with object: " + obj['info']
        e = handler.create_collection(lib['info'],coll['info'],obj['info'])
    elif ds == "obj":
        list = {}
        print("Please enter the name of the Object: ")
        names = par.parser.parse(input(">>>"))
        while True:
            print("Please enter the value of the key : type ")
            definition = par.parser.parse(input(">>>"))
            if definition is not None:
                list.update({definition["info"]: definition['type']})
            else:
                print("Not a valid input!! Definition will not be added to object definition!!")
            print("Wish to continue?")
            u = input(">>>")
            if u == "no":
                break
            else:
                continue
        msg = "Creating Object with name: " + names['info'] + " with list of attributes: " + list
        e = handler.create_object(names['info'],list)
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        list = []
        obj = handler.get_col_attributes(lib['info'],coll['info'])
        if isinstance(obj, Error):
            e = obj
            pass
        for key in obj:
            print("Please enter the value of: ", key)
            attr = input(">>>")
            list.append(attr)
        msg = "Creating instance with in Collection with name: " + coll['info'] + " with values: " + list
        e = handler.add_object(lib['info'],coll['info'],list)
    else:
        msg = "Not a valid structure!!!!!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def quit_lib(ds):
    msg = ""
    print("Please enter the name of the library: ")
    names = par.parser.parse(input(">>>"))
    msg = "Quiting structure with name: " + names['info']
    e = handler.close_library(names['info'])

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def sort():
    msg = ""
    print("Please enter the name of the Library: ")
    lib = par.parser.parse(input(">>>"))
    print("Please enter the name of the Collection: ")
    coll = par.parser.parse(input(">>>"))
    print("Please enter the name of the attribute to sort by: ")
    attri = par.parser.parse(input(">>>"))
    msg = "Sorting Collection with name: " + coll['info'] + " by attribute: " + attri['info']
    e = handler.sort(lib['info'],coll['info'],attri['info'])

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def merge():
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
    msg = "Merging collection #1: " + coll1['info'] + " with collection #2: " + coll2['info'] + " into new collection with name: " + coll3['info']
    e = handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'],lib3['info'])

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def search(ds):
    msg = ""
    if ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the attribute to sort by: ")
        attri = par.parser.parse(input(">>>"))
        print("Please enter the specific value to search for: ")
        value = par.parser.parse(input(">>>"))
        msg = "Searching collection with name: " + coll['info'] + " for all entries with value: " + value['info']
        e = handler.search_in_collection(lib['info'],coll['info'],attri['info'],value['info'])
    else:
        msg = "Not a valid operation!!!"

    if isinstance(e, Error):
        msg = e.message()
    print(msg)


def open(ds):
    msg = ""
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
        msg = "Opening library with name: ", names['info']
        e = handler.openLibrary(names['info'])
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
                quit(user_input['ds'])
        elif user_input['command'] == "show":
            if 'ds' in user_input:
                show(user_input['ds'])
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