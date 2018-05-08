import Parser as par
import os
import textpool


class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "
        self.ds = " "
        self.usercmd = " "
        self.names = {}

    def help(self):
        print("This is the Help Option")

    def exit(self):
        exit("Quitting Structure")

    def show(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Showing structure with name: ", names['info'])

    def delete(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Deleting structure with name: ", names['info'])

    def create(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Creating structure with name: ", names['info'])

    def quit(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Quiting structure with name: ", names['info'])

    def sort(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Sorting structure with name: ", names['info'])

    def merge(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Merging structure with name: ", names['info'])

    def search(self):
        print("Please enter the name of the structure: ")
        names = par.parser.parse(input(">>>"))
        print("Searching structure with name: ", names['info'])

    def open(self):
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
            t.help()
        elif user_input['command'] == "quit":
            t.quit()
        elif user_input['command'] == "show":
            t.show()
        elif user_input['command'] == "delete":
            t.delete()
        elif user_input['command'] == "create":
            t.create()
        elif user_input['command'] == "exit":
            t.exit()
        elif user_input['command'] == "merge":
            t.merge()
        elif user_input['command'] == "search":
            t.search()
        elif user_input['command'] == "sort":
            t.sort()
        elif user_input['command'] == "open":
            t.open()
        else:
            print("{} is not recognized".format(user_input))

    else:
        print("Please enter a command!!!!!")