import Parser as par
from Handler import Handler
import InputManager as ip
import textpool

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
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Showing structure with name: ", names['info'])
        handler.show_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Showing Collection with name: ", coll['info'])
        handler.show_collection(lib['info'],coll['info'])
    elif ds == "all":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Showing contents of the Library with name: ", names['info'])
        handler.show_library(names['info'])
    else:
        print("Not a valid operation!!")


def delete(ds):
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Deleting Library with name: ", names['info'])
        handler.remove_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Deleting Collection with name: ", coll['info'])
        handler.remove_collection_from_library(lib['info'],coll['info'])
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the index: ")
        index = par.parser.parse(input(">>>"))
        print("Deleting Instance with index: ", index['info'], " in Collection: ",coll['info'])
        handler.remove_object_from_collection(lib['info'],coll['info'],index['info'])
    else:
        print("Not a valid operation!!")


def create(ds):
    if ds == "lib":
        print("Please enter the name of the Library: ")
        names = par.parser.parse(input(">>>"))
        print("Creating library with name: ", names['info'])
        handler.create_library(names['info'])
    elif ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the Object: ")
        obj = par.parser.parse(input(">>>"))
        print("Creating collection with name: ", coll['info']," with object: ",obj['info'])
        handler.create_collection(lib['info'],coll['info'],obj['info'])
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
        print("Creating Object with name: ", names['info']," with list of attributes: ",list)
        handler.create_object(names['info'],list)
    elif ds == "inst":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        list = []
        obj = handler.get_col_attributes(lib['info'],coll['info'])
        for key in obj:
            print("Please enter the value of: ", key)
            attr = input(">>>")
            list.append(attr)
        print("Creating instance with in Collection with name: ", coll['info'], " with values: ",list)
        handler.add_object(lib['info'],coll['info'],list)
    else:
        print("Not a valid structure!!!!!!")


def quit_lib(ds):
    print("Please enter the name of the library: ")
    names = par.parser.parse(input(">>>"))
    print("Quiting structure with name: ", names['info'])
    handler.close_library(names['info'])


def sort():
    print("Please enter the name of the Library: ")
    lib = par.parser.parse(input(">>>"))
    print("Please enter the name of the Collection: ")
    coll = par.parser.parse(input(">>>"))
    print("Please enter the name of the attribute to sort by: ")
    attri = par.parser.parse(input(">>>"))
    print("Sorting Collection with name: ", coll['info'], " by attribute: ",attri['info'])
    handler.sort(lib['info'],coll['info'],attri['info'])


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
    print("Merging collection #1: ",coll1['info']," with collection #2: ",coll2['info']," into new collection with name: ",coll3['info'])
    handler.merge(lib1['info'],coll1['info'],lib2['info'],coll2['info'],coll3['info'],lib3['info'])


def search(ds):
    if ds == "col":
        print("Please enter the name of the Library: ")
        lib = par.parser.parse(input(">>>"))
        print("Please enter the name of the Collection: ")
        coll = par.parser.parse(input(">>>"))
        print("Please enter the name of the attribute to sort by: ")
        attri = par.parser.parse(input(">>>"))
        print("Please enter the specific value to search for: ")
        value = par.parser.parse(input(">>>"))
        print("Searching collection with name: ", coll['info'], " for all entries with value: ",value['info'])
        handler.search_in_collection(lib['info'],coll['info'],attri['info'],value['info'])
    else:
        print("Not a valid operation!!!")


def open(ds):
    if ds == "lib":
        print("Please enter the name of the library: ")
        names = par.parser.parse(input(">>>"))
        print("Opening library with name: ", names['info'])
        handler.openLibrary(names['info'])
    else:
        print("Not a valid operation!!")


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