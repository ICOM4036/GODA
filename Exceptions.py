class Error(Exception):
    pass


class LibraryNotOpenedError(Error):
    """
    Error when a command is tried to use with a library that is not opened.
    Receives the name of the library.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s is not opened." % self.expression


class LibraryOpenedError(Error):
    """
    Error when a library is tried to be opened but it is already opened.
    Receives the name of the library.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s is already opened." % self.expression


class LibraryDoesNotExistError(Error):
    """
    Error when a command is called with a library does not exist.
    Receives the name of the library.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Library %s does not exist." % self.expression


class CollectionDoesNotExistError(Error):
    """
    Error when a command is called with a collection that does not exist.
    Receives the name of the collection.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Collection %s does not exist." % self.expression


class ObjectDoesNotExistError(Error):
    """
    Error when a command is called with an object that does not exist.
    Receives the name of the object.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Object %s does not exist." % self.expression


class AttributeDoesNotExistError(Error):
    """
    Error when a command is called with an attribute that does not exist.
    Receives the name of the attribute.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "Attribute %s does not exist." % self.expression


class ObjectExistsError(Error):
    """
    Error when an object is tried to be created but an object with that name already exists.
    Receives the name of the object.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "An object with the name %s already exists." % self.expression


class LibraryExistsError(Error):
    """
    Error when a library is tried to be created but an library with that name already exists.
    Receives the name of the library.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "A library with the name %s already exists." % self.expression


class CollectionExistsError(Error):
    """
    Error when a collection is tried to be created but a collection with that name already exists.
    Receives the name of the collection.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "A collection with the name %s already exists." % self.expression


class CollectionsNotCompatibleError(Error):
    """
    Error when two collections are being compared but are not compatible.
    Receives the name of both collections.
    """
    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def message(self):
        return "Collections %s and %s are not compatible." % (self.expression1, self.expression2)


class ObjectNotCompatibleError(Error):
    """
    Error when an onject is tried to be added to a collection and attribute types are not compatible with collection.
    """
    def __init__(self):
        pass

    def message(self):
        return "Object is not compatible with collection."


class ObjectIndexOutOfBound(Error):
    """
    Error when an object is tried to be accessed with an index out of bounds.
    Receives the index number.
    """
    def __init__(self, expression):
        self.expression = expression

    def message(self):
        return "An object with index %s does not exist." % self.expression