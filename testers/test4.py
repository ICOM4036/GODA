from Handler import Handler
from Comparators.NumberComparator import NumberComparator

array = [5,8,3,5,8,9,2,0,9,6,545,2,3415,74,5624326,4563]
sorted_array = Handler().quicksort(array, NumberComparator())
print(array)
print(sorted_array)