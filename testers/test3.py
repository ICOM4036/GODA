from InputManager import *

print("===================\n\nTESTING INPUT MANAGER\n\n===================")

# Importing a collection from "Libraries\University\RollBook1.txt"
print('\n**********************************\nImporting a Collection from "',
      r"Libraries\University\RollBook1.txt", '"\n')
c = imp_new_collection(r"Libraries\University\RollBook1.txt")
c.display_col()

# Importing a collection from a file that does not exist "Libraries\University\llBook1.txt"
print('\n**********************************\nImporting a Collection from a file that does not exist"',
      r"Libraries\University\llBook1.txt", '\n')
e = imp_new_collection(r"Libraries\University\llBook1.txt")

# Importing and entire library from "Libraries\University\University.txt"
print('\n**********************************\nImporting an entire Library from"',
      r"Libraries\University\University.txt", '\n')
lib = imp_new_library(r"Libraries\University\University.txt")
lib.display_lib()
lib.display_all_lib()

# Updating a Collection within the imported Library
print('\n**********************************\nUpdating a Collection within the imported Library\n')
faculty = lib.get_collection("Faculty")
faculty.add_obj(["Ramon", "INEL 4205"])
faculty.add_obj(["Nilsa", "MATE 3031"])
faculty.display_col()
print('\n**********************************\nRemoving Nilsa\n')
faculty.remove_obj(6)
faculty.display_col()

# Removing a Collection from imported Library
print('\n**********************************\nRemoving a Collection from imported Library\n')
lib.remove_collection("RollBook3")
lib.display_lib()

###############################################################################
#                                                     # THIS WILL NOT BE USED #
# # Removing a Collection from imported Library
# print('\n**********************************\nImporting raw col\n')
# '''
# CSV FORMAT FOR RAW COLLECTION INPUT:
#
# objtype
# ATTR0:type,ATTR1:type, . . , ATTRn:type
# DATA00,DATA10, . . ,DATAn0
# DATA01, DATA11, . . DATAn1
# .
# DATA0m, DATA1m, . . ,DATAnm
# '''
#
# c = imp_raw_collection(r"rawtesting\rawcol.csv")
# c.display_col()
