from AbstractDataTypes.ObjectType import ObjectType
from AbstractDataTypes.Collection import Collection


print("===================\n\nTESTING INSTANCES\n\n===================")

ot1 = "Car"
at1 = {"model": "str", "year": "int", "color": "str"}
o1 = ObjectType(ot1, at1)
cn1 = "Garage"
c1 = Collection(cn1, o1)
c1.add_obj(["Tacoma", 2010, "gray"])
c1.add_obj(["Sienna", 2015, "black"])
c1.add_obj(["Yaris", 2020, "red"])
c1.add_obj(["Smart Car", 2018, "blue"])

ot2 = "Person"
at2 = {"name": "str", "age": "int"}
o2 = ObjectType(ot2, at2)
cn2 = "People"
c2 = Collection(cn2, o2)
c2.add_obj(["Willy Wonka", 55])
c2.add_obj(["Pedro", 62])
c2.add_obj(["Bienve", 47])

ot3 = "Something with a list"
at3 = {"name": "str", "stuff": "list"}
o3 = ObjectType(ot3, at3)
cn3 = "Stuff with list"
c3 = Collection(cn3, o3)
c3.add_obj(["Willy Wonka", ["candy", 45, "chocolate", "oompa-loompa"]])
c3.add_obj(["Pedro", ["Data", 4035, "Structures"]])
c3.add_obj(["Bienve", [4015, "Advanced", "Programming", "Computista", "Director"]])
c3.add_obj(["MATE", ["mate"]])

print("\n")
print(c1.get_obj_def_str())
c1.display_col()
print("\n")
print(c2.get_obj_def_str())
c2.display_col()
print("\n")
print(c3.get_obj_def_str())
c3.display_col()
print("\n")


print("===================\n\nTESTING COLLECTIONS\n\n===================")

# Define Object type
objtype = "Student"
attributes = {"ID": "str", "GPA": "float", "NAME": "str", "PROGRAM": "str"}
test_obj_def = ObjectType(objtype, attributes)

# Define Collection
test_col_name = "Roll Book"
test_collection = Collection(test_col_name, test_obj_def)

# Getting Object definition for Collection
print("\n----------------------------------\nGetting Object definition for collection\n")
print (test_collection.get_obj_def_str())

# Add Objects to Collection
print("\n----------------------------------\nAdding objects\n")
test_collection.add_obj(["802-15-1388", 3.00, "Alex", "ICOM"])
test_collection.add_obj(["802-18-1400", 2.00, "Prepa", "CIPO"])
test_collection.add_obj(["802-10-6088", 4.00, "Changoma", "BIOL"])
test_collection.add_obj(["802-80-2802", 10.0, "help", "ICOM"])
test_collection.add_obj(["802-04-0420", 4.20, "Willy", "MAFU"])

# Display Collection
print("\n----------------------------------\nDisplaying Collection\n")
test_collection.display_col()

# Getting list of specific value
print("\n----------------------------------\nGetting list of specific value\n")
print("All IDs:", test_collection.get_all_obj_val("ID"))
print("All GPAs:", test_collection.get_all_obj_val("GPA"))
print("All NAMEs:", test_collection.get_all_obj_val("NAME"))
print("All PROGRAMs:", test_collection.get_all_obj_val("PROGRAM"))

# Getting specific value from specific object
print("\n----------------------------------\nGetting specific value from specific object\n")
print("Index = 4, Value = PROGRAM \n"+ test_collection.get_obj_val(4, "PROGRAM"))

# Removing an object
print("\n----------------------------------\nRemoving an object\nRemoving index = 1\n")
test_collection.remove_obj(1)
test_collection.display_col()

# Changing an Object's value
print("\n----------------------------------\nChanging an Object's value\nIndex = 2, GPA = 3.84\n")
test_collection.set_obj_val(2, "GPA", 3.84)
test_collection.display_col()

print("===================\n\nTESTING COLLECTIONS FOR SPECIAL CASES\nFOR \"SPECIAL\" USERS :)\n\n===================")

# Adding non-compatible Object to collection
print("\n----------------------------------\nAdding non-compatible Object to collection\n")
test_collection.add_obj([8021516,"wewew",654654,54665])
test_collection.add_obj([8021516,555,654654,54665])
test_collection.add_obj(["lasdf"])
test_collection.add_obj(["asdfa", "sdfasdf", "asdfadf", "asdfasdf", "asdfadsfad"])
test_collection.add_obj(["802-04-0420", 4.20, "Willy", 555])

# Removing out of bounds
print("\n----------------------------------\nRemoving out of bounds\n")
test_collection.remove_obj(90)

# Testing case for setting attribute values
print("\n----------------------------------\nTesting case for setting attribute values\n")
# Index out of bounds
test_collection.set_obj_val(11, "ID", "80215168")
# Attribute not compatible with Object type
test_collection.set_obj_val(0, "AGE", "21")
# Attribute value not compatible with attribute data type
test_collection.set_obj_val(1, "GPA", 40)

# Getting values
print("\n----------------------------------\nGetting values\n")
test_collection.get_obj_val(888, "ID")
test_collection.get_obj_val(2, "AGE")
test_collection.get_all_obj_val("Age")


# Prints last Object when Collection is not empty
print("\n----------------------------------\nGetting last Object when collection is not empty and testing bounds\n")
print("\n\n" + test_collection.get_obj(len(test_collection.get_obj_list()) - 1).to_string())
# Out of bounds
print(test_collection.get_obj(len(test_collection.get_obj_list())))
# Out of bounds
print(test_collection.get_obj(len(test_collection.get_obj_list()) + 1))


# Testing empty collections
print("\n----------------------------------\nTesting empty collections\n")
ot4 = "Nothing"
at4 = {"Nothing": "str", "Nothing": "int"}
o4 = ObjectType(ot4, at4)
cn4 = "Empty Collection"
c4 = Collection(cn4, o4)
print(c4.get_obj_def_str())
c4.display_col()

print("\n")
ot5 = "Nothing2"
at5 = {}
o5 = ObjectType(ot5, at5)
cn5 = "Empty Collection2"
c5 = Collection(cn5, o5)
c5.add_obj([])
c5.add_obj([])
c5.add_obj([])
c5.add_obj([])

print(c5.get_obj_def_str())
c5.display_col()
