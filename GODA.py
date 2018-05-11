import Parser as par
import os
import Handler as handler
import InputManager as ip
import textpool

class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "
        self.ds = " "
        self.usercmd = " "
        self.names = {}


#Work with Alex para el textpool
def simple_help():
    print(textpool.help_txt)


def cmd_help(cmd):
    print(textpool.help_cmd)


def import_file(ds):
    if ds == "lib":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        print("Importing Library from file with name: ", names['info'])
        # ip.imp_new_library(names['info'])
    elif ds == "coll":
        print("Please enter the name of the file: ")
        coll = par.parser.parse(input(">>>"))
        print("Importing Collection from file with name: ", coll['info'])
        # ip.imp_new_collection(coll['info'])
    elif ds == "inst":
        print("Please enter the name of the file: ")
        names = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Importing data from file with name: ", names['info'], " into Collection: ",coll['info'])
        # ip.imp_data(names['info'],coll['info'])
    else:
        print("Not a valid operation!!")


def show(ds):
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Showing structure with name: ", names['info'])
        # handler.Handler.show_library(names['info'])
    elif ds == "coll":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Showing Collection with name: ", coll['info'])
        # handler.Handler.show_collection(lib['info'],coll['info'])
    elif ds == "all":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Showing contents of the Library with name: ", names['info'])
        # handler.Handler.show_library(names['info'])
    else:
        print("Not a valid operation!!")


def delete(ds):
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Deleting Library with name: ", names['info'])
        # handler.Handler.remove_library(names['info'])
    elif ds == "coll":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Deleting Collection with name: ", coll['info'])
        # handler.Handler.remove_collection_from_library(lib['info'],coll['info'])
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the index: ")
        index = par.parser.parse(input(">>>"))
        print("Deleting Instance with index: ", index['info'], " in Collection: ",coll['info'])
        # handler.Handler.remove_object_from_collection(lib['info'],coll['info'],index['info'])
    else:
        print("Not a valid operation!!")


#add loop for the object attributes - dict
#add loop for the attributes - array
def create(ds):
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Creating library with name: ", names['info'])
       # handler.Handler.create_library(names['info'])
    elif ds == "coll":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the Object: ")
        obj = par.parser.parse(input(">>>"))
        print("Creating collection with name: ", coll['info']," with object: ",obj['info'])
        # handler.Handler.create_collection(lib['info'],coll['info'],obj['info'])
    elif ds == "obj":
        print("Please enter the name of the Object: ")
        names = par.parser.parse(input(">>>"))
        print("Creating Object with name: ", names['info'])
        # handler.Handler.create_object(names['info'])
    elif ds == "inst":
        print("Please enter the name of the Object: ")
        names = par.parser.parse(input(">>>"))
        print("Creating instance with name: ", names['info'])
        # handler.Handler.create_library(names['info'])
    else:
        print("Not a valid structure!!!!!!")


def quit_lib(ds):
    print("Please enter the name of the library: ")
    names = par.parser.parse(input(">>>"))
    print("Quiting structure with name: ", names['info'])
    # handler.Handler.close_library(names['info'])


def sort():
    print("Please enter the name of the Library: ")
    lib = par.parser.parse(input(">>>"))
    print("Please enter the name of the Collection: ")
    coll = par.parser.parse(input(">>>"))
    print("Please enter the name of the attribute to sort by: ")
    attri = par.parser.parse(input(">>>"))
    print("Sorting Collection with name: ", coll['info'], " by attribute: ",attri['info'])
    # handler.Handler.sort(lib['info'],coll['info'],attri['info'])


def merge():
    print("Please enter the name of the first library: ")
    lib1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the first collection: ")
    coll1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second library: ")
    lib2 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second collection: ")
    coll2 = par.parser.parse(input(">>>"))
    # print("Please enter the name of the library where the new collection will be placed: ")
    # lib3 = par.parser.parse(input(">>>"))
    print("Please enter the name of the new collection: ")
    coll3 = par.parser.parse(input(">>>"))
    print("Merging collection #1: ",coll1['info']," with collection #2: ",coll2['info']," into new collection with name: ",coll3['info'])
    # handler.Handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'])


def search(ds):
    if ds == "coll":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the attribute to sort by: ")
        attri = par.parser.parse(input(">>>"))
        print("Please enter the specific value to search for: ")
        value = par.parser.parse(input(">>>"))
        print("Searching collection with name: ", coll['info'], " for all entries with value: ",value['info'])
        # handler.Handler.search_in_collection(lib['info'],coll['info'],attri['info'],value['info'])
    else:
        print("Not a valid operation!!!")


def open(ds):
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
        print("Opening library with name: ", names['info'])
       # handler.Handler.openLibrary(names['info'])
    else:
        print("Not a valid operation!!")


if __name__ == '__main__':
    t = Goda()

user_input = {}

print("     Welcome to GODA     \n")
# os.system("GODApic.jpg")
print("     Hope you enjoy it!!   \n")

while True:
    print("Please enter desired command:")
    user_input = par.parser.parse(input(">>>"))

    #There is an error here that not matter what I do it can't be fixed. T_T

    if user_input is not None: #and 'command' in user_input is True and 'info' in user_input is False:

        if user_input['command'] == "help":
            if len(user_input) == 2:
                cmd_help(user_input['ds'])
            else:
                simple_help()
        elif user_input['command'] == "quit":
            if len(user_input) == 1:
                quit("\tQuitting Goda \n \tGoodbye!!!")
            else:
                quit(user_input['ds'])
        elif user_input['command'] == "show":
            show(user_input['ds'])
        elif user_input['command'] == "rm":
            delete(user_input['ds'])
        elif user_input['command'] == "crt":
            create(user_input['ds'])
        elif user_input['command'] == "merge":
            merge()
        elif user_input['command'] == "search":
            search(user_input['ds'])
        elif user_input['command'] == "sort":
            sort()
        elif user_input['command'] == "open":
            open(user_input['ds'])
        elif user_input['command'] == "imp":
            import_file()
        else:
            print("{} is not recognized".format(user_input))
    else:
        print("Please enter a valid command!!!!!")