from Handler import Handler
from DataTypes.Library import Library
from DataTypes.Collection import Collection
from DataTypes.ObjectType import ObjectType
from Comparators.NumberComparator import NumberComparator
from SortingAlgorithms import Quicksort

array = [5,8,3,5,8,9,2,0,9,6,545,2,3415,74,5624326,4563]
sorted_array = Quicksort.sort(array, NumberComparator())
print(array)
print(sorted_array)

# student_obj = ObjectType('Student', {'name':'str', 'gpa':'float', 'year':'int'})
# col1 = Collection('PLStudents', student_obj)
# col2 = Collection('DBStudents', student_obj)
#
# col1.add_obj(['Juana', 4.00, 3])
# col1.add_obj(['Chua', 2.00, 10])
# col2.add_obj(['Pedro Rivera', 3.34, 20])
# col2.add_obj(['Orlando', 3.85, 2])
#
# Handler().merge(col1, col2, 'col3')
#
# lib = Library('lib')
# lib.add_collection(col1)
# lib.add_collection(col2)
# Handler().show_library(lib)
# Handler().show_collection(col1)
# Handler().show_collection(col2)

# dict = {'A': 1, 'B': 2, 'C': 3}
# dict2 = {'A': 4, 'B': 5, 'C': 6}

