from DataTypes.ObjectType import ObjectType
from DataTypes.Collection import Collection
from Handler import Handler

# Creating collection with an object that has boolean attributes
ot3 = "Something with bool"
at3 = {"name": "str", "dead": "bool"}
o3 = ObjectType(ot3, at3)
cn3 = "Stuff with list"

handler = Handler()

handler.create_library('Testing something with bool')
handler.create_object(ot3, at3)
handler.create_collection('Testing something with bool', cn3, ot3)
handler.add_object('Testing something with bool', cn3, ["Willy Wonka", False])
handler.add_object('Testing something with bool', cn3, ["Hawking", True])
handler.add_object('Testing something with bool', cn3, ["Pedro", False])
handler.add_object('Testing something with bool', cn3, ["Bienve", None])
handler.add_object('Testing something with bool', cn3, ["Changoma", True])

handler.show_collection('Testing something with bool', cn3)

handler.sort('Testing something with bool', "Stuff with list", 'dead')

handler.remove_library('Testing something with bool')

