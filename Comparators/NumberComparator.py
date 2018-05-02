class NumberComparator:

    def compare(self, elem1, elem2):
        if elem1 > elem2:
            return 1
        elif elem1 < elem2:
            return -1
        else:
            return 0