"""

"""

def sort(array, comp, index):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if comp.compare(x[index], pivot[index]) < 0:
                less.append(x)
            elif comp.compare(x[index], pivot[index]) > 0:
                greater.append(x)
            else:
                equal.append(x)
        return self.quicksort(less, comp, index) + equal + self.quicksort(greater, comp, index)
    else:
        return array