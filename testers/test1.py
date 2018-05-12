from ADT.Library import Library
from ADT.ObjectType import ObjectType
from ADT.Collection import Collection

print("===================\n\nTESTING LIBRARY\n\n===================")

# Creating Library
print('\n**********************************'
      '\nCreating Library "University"'
      '\nCreating Collection "Roll Book 1" in "University'
      '\nCreating Collection "Roll book 2" in "University"'
      '\nCreating Collection "Faculty" in "University"\n')
lib0 = Library("University")
# Creating Collection "Roll Book 1" inside Library
lib0.create_collection("Roll Book 1", "Student", {"ID": "str", "GPA": "float", "NAME": "str", "PROGRAM": "str"})
# Creating Collection "Roll Book 2" inside Library
lib0.create_collection("Roll Book 2", "Student", {"ID": "str", "GPA": "float", "NAME": "str", "PROGRAM": "str"})
# Creating Collection "Faculty" inside Library
lib0.create_collection("Faculty", "Professor", {"NAME": "str", "PROGRAM": "str", "COURSES": "int"})

# Adding Students to Roll Book 1
print('\n**********************************\nAdding Students to "Roll Book 1"\n')
c1 = lib0.get_collection("Roll Book 1")
c1.add_obj(["802-15-1388", 3.00, "Alex", "ICOM"])
c1.add_obj(["802-18-1400", 2.00, "Prepa", "CIPO"])
c1.add_obj([None, None, None, None])
c1.add_obj(["802-10-6088", 4.00, "Changoma", "BIOL"])
c1.add_obj(["802-80-2802", 10.0, "help", "ICOM"])
c1.add_obj(["802-04-0420", 4.20, "Willy", "MAFU"])
c1.display_col()

# Adding Professors to Faculty
print('\n**********************************\nAdding Professors to "Faculty"\n')
c3 = lib0.get_collection("Faculty")
c3.add_obj(["Wilson", "ICOM", 2])
c3.add_obj(["Bienvenido", "CIIC", 3])
c3.add_obj(["Pedro", "ICOM", 2])
c3.add_obj(["Amir", "CIIC", 1])
c3.display_col()


# Adding a collection (Not creating!)
print('\n**********************************\nAdding a Collection (Not creating!)\n')
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

# Displaying Library
print('\n**********************************\nDisplaying Library "University" info\n')
lib0.display_lib()
print('\n**********************************\nDisplaying Library "University"\n')
lib0.display_all_lib()

# Removing Collection "Roll Book 2"
print('\n**********************************\nRemoving Collection "Roll Book 2"\n')
lib0.remove_collection("Roll Book 2")
print('\n**********************************\nDisplaying Library "University" info\n')
lib0.display_lib()
print('\n**********************************\nDisplaying Library "University"\n')
lib0.display_all_lib()

# Removing Collection "Faculty"
print('\n**********************************\nRemoving Collection "Faculty"\n')
lib0.remove_collection("Faculty")
print('\n**********************************\nDisplaying Library "University" info\n')
lib0.display_lib()
print('\n**********************************\nDisplaying Library "University"\n')
lib0.display_all_lib()

# Removing Collection "Roll Book 1"
print('\n**********************************\nRemoving Collection "Roll Book 1"\n')
lib0.remove_collection("Roll Book 1")
print('\n**********************************\nDisplaying Library "University" info\n')
lib0.display_lib()
print('\n**********************************\nDisplaying Library "University"\n')
lib0.display_all_lib()

# Removing Collection "Garage"
print('\n**********************************\nRemoving Collection "Garage"\n')
lib0.remove_collection("Garage")
print('\n**********************************\nDisplaying Library "University" info\n')
lib0.display_lib()
print('\n**********************************\nDisplaying Library "University"\n')
lib0.display_all_lib()