import Parser as par
import os
import Handler as handler

class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "
        self.ds = " "
        self.usercmd = " "
        self.names = {}


#Work with Alex para el textpool
def simple_help():
    print("This is the Help Option")


def cmd_help(cmd):
    print("This is the command specific help")


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
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Showing structure with name: ", names['info'])
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


def quit(ds):
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
        print("Quiting structure with name: ", names['info'])
       # handler.Handler.close_library(names['info'])
    elif ds == "all":
        exit("\tQuitting Goda \n \tGoodbye!!!")
    else:
        print("Not a valid operation!!")

#Library,collection,attribute_name
def sort(ds):
    if ds == "coll":
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Sorting structure with name: ", names['info'])
    else:
        print("Not a valid operation!!")

#add third library name
def merge():
    print("Please enter the name of the first library: ")
    lib1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the first collection: ")
    coll1 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second library: ")
    lib2 = par.parser.parse(input(">>>"))
    print("Please enter the name of the second collection: ")
    coll2 = par.parser.parse(input(">>>"))
    print("Please enter the name of the new collection: ")
    coll3 = par.parser.parse(input(">>>"))
    print("Merging collection #1: ", coll1['info']," with collection #2: ",coll2['info'], " into new collection with name: ",coll3['info'])
    #handler.Handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'])

#Check the coll part because we need to add a few things
def search(ds):
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
        print("Searching library with name: ", names['info'])
    elif ds == "coll":
        print("Please enter the name of the collection: ")
        names = par.parser.parse(input(">>>"))
        print("Searching collection with name: ", names['info'])
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
            quit(user_input['ds'])
        elif user_input['command'] == "show":
            show(user_input['ds'])
        elif user_input['command'] == "delete":
            delete(user_input['ds'])
        elif user_input['command'] == "create":
            create(user_input['ds'])
        elif user_input['command'] == "merge":
            merge()
        elif user_input['command'] == "search":
            search(user_input['ds'])
        elif user_input['command'] == "sort":
            sort(user_input['ds'])
        elif user_input['command'] == "open":
            open(user_input['ds'])
        else:
            print("{} is not recognized".format(user_input))
    else:
        print("Please enter a valid command!!!!!")