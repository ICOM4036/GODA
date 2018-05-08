import Parser as par
import os
import textpool
import Handler as handler

class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "#user_input['command']
        self.ds = " " #user_input['ds']
        self.usercmd = " "#user_input['info']
        self.names = {}

def help():
    print("This is the Help Option")

def exit():
    exit("Quitting Structure")

def show(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Showing structure with name: ", names['info'])
    handler.Handler.show_library(names['info'])

def delete(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Deleting structure with name: ", names['info'])
    handler.Handler.remove_library(names['info'])

def create(ds):
    if ds == "lib":
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Creating structure with name: ", names['info'])
        handler.Handler.create_library(names['info'])
    elif ds == "coll":
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Creating structure with name: ", names['info'])
        handler.Handler.create_library(names['info'])
    elif ds == "obj":
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Creating structure with name: ", names['info'])
        handler.Handler.create_library(names['info'])
    else:
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Creating structure with name: ", names['info'])
        handler.Handler.create_library(names['info'])


def quit(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Quiting structure with name: ", names['info'])

def sort(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Sorting structure with name: ", names['info'])

def merge(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Merging structure with name: ", names['info'])

def search(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Searching structure with name: ", names['info'])

def open(ds):
    print("Please enter the name of the structure: ")
    names = par.parser.parse(input(">>>"))
    print("Opening structure with name: ", names['info'])


if __name__ == '__main__':
    t = Goda()

user_input = {}

while True:
    print("     Welcome to GODA     \n")
    # os.system("GODApic.jpg")
    print("     Hope you enjoy it!!   \n")
    print("Please enter desired command:")
    user_input = par.parser.parse(input(">>>"))

    if user_input is not None:

        if user_input['command'] == "help":
            help()
        elif user_input['command'] == "quit":
            quit(user_input['ds'])
        elif user_input['command'] == "show":
            show(user_input['ds'])
        elif user_input['command'] == "delete":
            delete(user_input['ds'])
        elif user_input['command'] == "create":
            create(user_input['ds'])
        elif user_input['command'] == "exit":
            exit()
        elif user_input['command'] == "merge":
            merge(user_input['ds'])
        elif user_input['command'] == "search":
            search(user_input['ds'])
        elif user_input['command'] == "sort":
            sort(user_input['ds'])
        elif user_input['command'] == "open":
            open(user_input['ds'])
        else:
            print("{} is not recognized".format(user_input))

    else:
        print("Please enter a command!!!!!")