from Handler import Handler

handler = Handler()

handler.create_library('PersonalidadesDeHelp')
handler.create_object('help', {'name':'str', 'nivel':'int'})

handler.openLibrary('PersonalidadesDeHelp')

handler.create_collection('PersonalidadesDeHelp', 'help1', 'help')
handler.create_collection('PersonalidadesDeHelp', 'help2', 'help')

handler.add_object('PersonalidadesDeHelp', 'help1', ['el que no sabe lo que dice', 6])
handler.add_object('PersonalidadesDeHelp', 'help1', ['el que habla mucho', 2])

handler.add_object('PersonalidadesDeHelp', 'help2', ['el que no te deja estudiar', 8])
handler.add_object('PersonalidadesDeHelp', 'help2', ['la housemate', 10])


#handler.openLibrary('PersonalidadesDeHelp')
print("Testing show library\n")
handler.show_library('PersonalidadesDeHelp')
print("\nTesting show collection\n")
handler.show_collection('PersonalidadesDeHelp', 'help1')
print("\n")
handler.show_collection('PersonalidadesDeHelp', 'help2')

print("\n\nTesting merge\n")
handler.merge('PersonalidadesDeHelp', 'help1', 'PersonalidadesDeHelp', 'help2', 'help3', 'PersonalidadesDeHelp')
handler.show_collection('PersonalidadesDeHelp', 'help3')

print("\n\nTesting sort by int\n")
handler.sort('PersonalidadesDeHelp', 'help3', 'nivel')
print("\nTesting sort by strings\n")
handler.sort('PersonalidadesDeHelp', 'help3', 'name')

# handler.remove_collection_from_library('PersonalidadesDeHelp', 'help1')
# handler.remove_collection_from_library('PersonalidadesDeHelp', 'help2')

print("\n\nTesting remove 'help1' and 'help2'\n")
handler.show_library('PersonalidadesDeHelp')

print("\n\nTesting delete object at index 1\n")
handler.remove_object_from_collection('PersonalidadesDeHelp', 'help3', 1)
handler.show_collection("PersonalidadesDeHelp", 'help3')

print("\n\nTesting search objects with 'nivel' = 10\n")
handler.search_in_collection('PersonalidadesDeHelp', 'help3', 'nivel', 10)

#handler.remove_library('PersonalidadesDeHelp')