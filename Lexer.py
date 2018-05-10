import ply.lex as lex

#the int, and float definitions as str

tokens = ["INFO", "DS", "COMMAND","TYPE","COLON"]

reserved = {
    'create': 'COMMAND',
    'delete': 'COMMAND',
    'help': 'COMMAND',
    'quit': 'COMMAND',
    'sort': 'COMMAND',
    'search': 'COMMAND',
    'show': 'COMMAND' ,
    'merge': 'COMMAND' ,
    'lib': 'DS' ,
    'coll': 'DS' ,
    'inst': 'DS',
    'obj': 'DS',
    'open': 'COMMAND',
    'import': 'COMMAND',
    'all': 'DS',
    'int': 'TYPE',
    'float':'TYPE',
    'str':'TYPE',
    'bool': 'TYPE'
}
# Tokens

t_ignore = '\t '
t_COLON = r':'


def t_CREATE(t):
    r'\b create \b'
    t.type = reserved.get(t.value)
    return t


def t_DELETE(t):
    r'\b delete \b'
    t.type = reserved.get(t.value)
    return t


def t_QUIT(t):
    r'\b quit \b'
    t.type = reserved.get(t.value)
    return t


def t_HELP(t):
    r'\b help \b'
    t.type = reserved.get(t.value)
    return t


def t_SORT(t):
    r'\b sort \b'
    t.type = reserved.get(t.value)
    return t


def t_EXIT(t):
    r'\b exit \b'
    t.type = reserved.get(t.value)
    return t


def t_SEARCH(t):
    r'\b search \b'
    t.type = reserved.get(t.value)
    return t


def t_SHOW(t):
    r'\b show \b'
    t.type = reserved.get(t.value)
    return t


def t_MERGE(t):
    r'\b merge \b'
    t.type = reserved.get(t.value)
    return t


def t_LIBRARY(t):
    r'\b lib \b'
    t.type = reserved.get(t.value)
    return t


def t_COLLECTION(t):
    r'\b coll \b'
    t.type = reserved.get(t.value)
    return t


def t_INSTANCE(t):
    r'\b inst \b'
    t.type = reserved.get(t.value)
    return t


def t_BOOL(t):
    r'\b bool \b'
    t.type = reserved.get(t.value)
    return t


def t_STR(t):
    r'\b str \b'
    t.type = reserved.get(t.value)
    return t


def t_OBJECT(t):
    r'\b obj \b'
    t.type = reserved.get(t.value)
    return t


def t_OPEN(t):
    r'\b open \b'
    t.type = reserved.get(t.value)
    return t


def t_ALL(t):
    r'\b all \b'
    t.type = reserved.get(t.value)
    return t


def t_INFO(t):
    r'\b [a-zA-Z0-9._^%$\#!~@]* \b'
    t.type = "INFO"
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()