class LetterComparator:

    def compare(self, string1, string2):
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