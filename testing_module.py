import Object

otype = "Student"
attributes = ["ID", "GPA", "name"]
# Creting an Object
s = Object.Object(otype, attributes)


vals = ["802-15-1388", 3.00, "Alex"]
# Setting values for the attributes of object s
s.set_values(vals)

# Testing Object module
print("---------------------------------\nObject type: ", s.get_type())
print ("---------------------------------\nList of defined attributes: ", s.get_attributes())
print ("---------------------------------\nGetting specific values:")
for a in s.get_attributes():
    print(a, "=", s.get_val(a))


print("---------------------------------\nList of values: ", s.get_val_list())

print("---------------------------------\nList of attributes and list of values values printed respectively")
attr = s.get_attributes()
attrval = s.get_val_list()
for b in range(0, len(attr)):
    print(attr[b], attrval[b])









