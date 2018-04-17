import InputManager
import OutputManager
from Collection import Collection
from Library import Library
from ObjectType import ObjectType

print("===================\n\nTESTING OUTPUT MANAGER\n\n===================")

# Importing library from project files
print('\n**********************************\nImporting library from project files\n')
lib = InputManager.imp_new_library(r"Libraries\University\University.txt")
lib.display_lib()

# Saving Library in project files
print('\n**********************************\nSaving Library in project files\n')
OutputManager.save_library(lib)

# Exporting Library to Desktop (replace my directory with your to test for yourself)
print('\n**********************************\nExporting Library to Desktop (replace my directory with your own to test)\n')
OutputManager.export_library(lib, r'C:/Users/cintr/Desktop/Libraries')

# Creating a Library
print('\n**********************************''\nCreating Library "Stuff" (same Library "University", renames "Stuff" from "test1.py")')
lib0 = Library("Stuff")
# Creating Collention "Roll Book 1" inside Library
lib0.create_collection("Roll Book 1", "Student", {"ID": "str", "GPA": "float", "NAME": "str", "PROGRAM": "str"})
# Creating Collention "Roll Book 2" inside Library
lib0.create_collection("Roll Book 2", "Student", {"ID": "str", "GPA": "float", "NAME": "str", "PROGRAM": "str"})
# Creating Collention "Faculty" inside Library
lib0.create_collection("Faculty", "Professor", {"NAME": "str", "PROGRAM": "str", "COURSES": "int"})

# Adding Students to Roll Book 1
c1 = lib0.get_collection("Roll Book 1")
c1.add_obj(["802-15-1388", 3.00, "Alex", "ICOM"])
c1.add_obj(["802-18-1400", 2.00, "Prepa", "CIPO"])
c1.add_obj(["802-10-6088", 4.00, "Changoma", "BIOL"])
c1.add_obj(["802-80-2802", 10.0, "help", "ICOM"])
c1.add_obj(["802-04-0420", 4.20, "Willy", "MAFU"])

# Adding Professors to Faculty
c3 = lib0.get_collection("Faculty")
c3.add_obj(["Wilson", "ICOM", 2])
c3.add_obj(["Bienvenido", "CIIC", 3])
c3.add_obj(["Pedro", "ICOM", 2])
c3.add_obj(["Amir", "CIIC", 1])

# Adding a collection (Not creating!)
ot1 = "Car"
at1 = {"model": "str", "year": "int", "color": "str"}
o1 = ObjectType(ot1, at1)
cn1 = "Garage"
c1 = Collection(cn1, o1)
c1.add_obj(["Tacoma", 2010, "gray"])
c1.add_obj(["Sienna", 2015, "black"])
c1.add_obj(["Yaris", 2020, "red"])
c1.add_obj(["Smart Car", 2018, "blue"])

lib0.add_collection(c1)

# Exporting Library to Desktop (replace my directory with your to test for yourself)
print('\n**********************************\nExporting Library to Desktop (replace my directory with your own to test)\n')
OutputManager.export_library(lib0, 'C:/Users/cintr/Desktop/Libraries')

# Importing Library from Desktop (replace my directory with your to test for yourself)
print('\n**********************************\nExporting Library from Desktop (replace my directory with your own to test)\n')
lib1 = InputManager.imp_new_library(r'C:\Users\cintr\Desktop\Libraries\Stuff\Stuff.txt')
lib1.display_lib()
lib1.display_all_lib()

# Saving Library "Stuff" in project files
print('\n**********************************\nSaving Library "Stuff" in project files\n')
OutputManager.save_library(lib1)

# Exporting Collection to Desktop (replace my directory with your own to test)
print('\n**********************************\nExporting Collection to Desktop (replace my directory with your own to test)\n')
OutputManager.export_collection(c1, 'C:/Users/cintr/Desktop/Collection')
