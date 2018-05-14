class BooleanComparator:

    def compare(self, bool1, bool2):
        if bool2 == False or None and bool1 == True:
            return -1
        elif bool1 == False or None and bool2 == True:
            return 1
        # Both booleans have the same value
        else:
            return 0