class Quicksort:

    def sort(self, array, comp, index):
        """
        Sorts the elements in the array
        :param array: ObjType[] - array to be sorted, where the elements are ObjectTypes
        :param comp: Comparator - comparator to be used to compare elements
        :param index: int - index, in the array of the object values, of the attribute used to sort
        :return: ObjType[] - array of the ObjectTypes sorted
        """
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