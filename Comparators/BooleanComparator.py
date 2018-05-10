class BooleanComparator:

    def compare(self, bool1, bool2):
        if bool1 == True and bool2 == False:
            return 1
        elif bool2 == True and bool2 == True:
            return -1
        else:
            return 0