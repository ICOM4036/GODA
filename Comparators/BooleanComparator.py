class BooleanComparator:

    def compare(self, bool1, bool2):
        if bool1 == True and bool2 == False or None:
            return -1
        elif bool2 == True and bool1 == False or None:
            return 1
        # Both booleans have the same value
        else:
            return 0