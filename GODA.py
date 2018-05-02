"""
    MAIN EXECUTION OF GODA
    TO BE DEVELOPED
"""
import textpool
import Handler

def print_help():
    print (textpool.help)

while True:
    user_input = input()
    if user_input == "help":
        print_help()
    elif user_input == "quit":
        exit("puta bida")
    elif user_input == "create_library":
        print("library name: ")
        name = input()
        Handler.createLibrary(name)
    else:
        print("{} is not recognized".format(user_input))
