import OutputManager2
from DataTypes.Collection import Collection
from DataTypes.ObjectType import ObjectType

obj = ObjectType('prueba', {'esto':'es', 'un':'crical'})
col = Collection('prueba', obj)
OutputManager2.create_collection("C:/Users/irixa/PycharmProjects/GODA/Libraries/Stuff", col)
OutputManager2.delete_collection("C:/Users/irixa/PycharmProjects/GODA/Libraries/Stuff", 'prueba')