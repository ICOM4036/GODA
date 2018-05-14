class LetterComparator:

    def compare(self, string1, string2):
        # string1 and string2 are null
        if string1 is None and string2 is None:
            return 0
        # string1 is null
        elif string1 is None:
            return -1
        # string2 is null
        elif string2 is None:
            return 1
        # Compare character by character
        for idx in range(min(len(string1), len(string2))):
            # Get the "value" of the character
            ordinal1, ordinal2 = ord(string1[idx]), ord(string2[idx])
            # If the "value" is identical check the next characters
            if ordinal1 == ordinal2:
                continue
            elif ordinal1 < ordinal2:
                return -1
            else:
                return 1
        # We're out of characters and all were equal
        return 0