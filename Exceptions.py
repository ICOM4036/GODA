class Error(Exception):
    pass


class LibraryNotOpenedError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s is not opened." % self.expression


class LibraryOpenedError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s is already opened." % self.expression


class LibraryDoesNotExistError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s does not exist." % self.expression


class CollectionDoesNotExistError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Collection %s does not exist." % self.expression


class ObjectDoesNotExistError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Collection %s does not exist." % self.expression


class AttributeDoesNotExistError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Attribute %s does not exist." % self.expression


class ObjectExistsError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "An object with the name %s already exists." % self.expression


class LibraryExistsError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "A library with the name %s already exists." % self.expression


class CollectionExistsError(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "A collection with the name %s already exists." % self.expression


class CollectionsNotCompatibleError(Error):

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def message(self):
        return "Collections %s and %s are not compatible." % (self.expression1, self.expression2)


class ObjectIndexOutOfBound(Error):

    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "An object with index %s does not exist." % self.expression