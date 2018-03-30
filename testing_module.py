from ObjectType import ObjectType
from Collection import Collection

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
print (test_collection.get_obj_def())

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
print("\n\n"+test_collection.get_object(len(test_collection.get_obj_list())-1).to_string())
# Out of bounds
print(test_collection.get_object(len(test_collection.get_obj_list())))
# Out of bounds
print(test_collection.get_object(len(test_collection.get_obj_list())+1))




