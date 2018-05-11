class NumberComparator:

    def compare(self, elem1, elem2):
        if elem1 is None and elem2 is None:
            return 0
        if elem1 > elem2 or elem2 is None:
            return 1
        elif elem1 < elem2 or elem1 is None:
            return -1
        else:
            return 0