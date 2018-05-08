"""
    MAIN EXECUTION OF GODA
    TO BE DEVELOPED
"""
import textpool
import Handler


class Goda:
    def __init__(self):
        self.name = "Main"
        self.cmd = " "
        self.ds = " "
        self.usercmd = " "


if __name__ == '__main__':
    t = Goda()


def print_help():
    print (textpool.help)


user_input = {}

while True:

    print("Enter desired command:")
    user_input = input(">>>")

    if user_input == "help" :
        print("I am merely testing this out")
    elif user_input == "quit":
        exit("Quitting GODA")
    elif user_input == "show library":
        print("library name: ")
        name = input()
        print("Deleting library with name: ",name)
    elif user_input == "delete library":
        print("library name: ")
        name = input()
        print("Deleting library with name: ",name)
    elif user_input == "create library":
        print("library name: ")
        name = input()
        print("Creating library with name: ", name)
    else:
        print("{} is not recognized".format(user_input))
