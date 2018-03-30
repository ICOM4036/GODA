from ObjectType import ObjectType
from Collection import Collection

print("===================\n\nTESTING COLLECTIONS\n\n===================")

# Define Object type
objtype = "Student"
attributes = ["ID", "GPA", "NAME", "PROGRAM"]
test_obj_def = ObjectType(objtype, attributes)

# Define Collection
test_col_name = "Roll Book"
test_collection = Collection(test_col_name, test_obj_def)

# Getting Object definition for Collection
print("\n----------------------------------\nGetting Object definition for collection\n")
print (test_collection.get_obj_def())

# Add Objects to Collection
test_collection.add_obj(["802-15-1388", 3.00, "Alex", "ICOM"])
test_collection.add_obj(["802-18-1400", 2.00, "Prepa", "CIPO"])
test_collection.add_obj(["802-10-6088", 4.00, "Changoma", "BIOL"])
test_collection.add_obj(["802-80-2802", 1000, "help", "ICOM"])
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

