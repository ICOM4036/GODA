from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from Handler import Handler

# Creating collection with an object that has boolean attributes
ot3 = "Something with bool"
at3 = {"name": "str", "dead": "bool"}
o3 = ObjectType(ot3, at3)
cn3 = "Stuff with list"
c3 = Collection(cn3, o3)
c3.add_obj(["Willy Wonka", False])
c3.add_obj(["Pedro", False])
c3.add_obj(["Bienve", False])
c3.add_obj(["Hawking", True])
c3.add_obj(["Changoma", True])

# Display Collection
print("\n")
print(c3.get_obj_def_str())
c3.display_col()

handler = Handler()

handler.create_library('Testing something with bool')
handler.create_collection('Testing something with bool', "Stuff with list", o3)
handler.add_object('Testing something with bool', "Stuff with list", ["Willy Wonka", False])
handler.add_object('Testing something with bool', "Stuff with list", ["Pedro", False])
handler.add_object('Testing something with bool', "Stuff with list", ["Bienve", False])
handler.add_object('Testing something with bool', "Stuff with list", ["Hawking", True])
handler.add_object('Testing something with bool', "Stuff with list", ["Changoma", True])

handler.sort('Testing something with bool', "Stuff with list", 'dead')


