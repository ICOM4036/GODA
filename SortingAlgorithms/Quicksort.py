"""

"""
class Quicksort:

    def sort(self, array, comp, index):
        less = []
        equal = []
        greater = []

        if len(array) > 1:
            pivot = array[0]
            for x in array:
                if comp.compare(x.get_value(index), pivot.get_value(index)) < 0:
                    less.append(x)
                elif comp.compare(x.get_value(index), pivot.get_value(index)) > 0:
                    greater.append(x)
                else:
                    equal.append(x)
            return self.sort(less, comp, index) + equal + self.sort(greater, comp, index)
        else:
            return array