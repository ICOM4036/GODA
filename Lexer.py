import ply.lex as lex

tokens = ["INFO", "DS", "COMMAND","TYPE","COLON"]

reserved = {
    'crt': 'COMMAND',
    'rm': 'COMMAND',
    'help': 'COMMAND',
    'quit': 'COMMAND',
    'sort': 'COMMAND',
    'search': 'COMMAND',
    'show': 'COMMAND' ,
    'merge': 'COMMAND' ,
    'lib': 'DS' ,
    'col': 'DS' ,
    'inst': 'DS',
    'obj': 'DS',
    'open': 'COMMAND',
    'imp': 'COMMAND',
    'all': 'DS',
    'int': 'TYPE',
    'float':'TYPE',
    'str':'TYPE',
    'bool': 'TYPE'
}
# Tokens

t_ignore = '\t '
t_COLON = r':'


def t_CRT(t):
    r'\b crt \b'
    t.type = reserved.get(t.value)
    return t


def t_RM(t):
    r'\b rm \b'
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


def t_LIB(t):
    r'\b lib \b'
    t.type = reserved.get(t.value)
    return t


def t_COL(t):
    r'\b col \b'
    t.type = reserved.get(t.value)
    return t


def t_INST(t):
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


def t_INT(t):
    r'\b int \b'
    t.type = reserved.get(t.value)
    return t


def t_FLOAT(t):
    r'\b float \b'
    t.type = reserved.get(t.value)
    return t


def t_OBJ(t):
    r'\b obj \b'
    t.type = reserved.get(t.value)
    return t


def t_OPEN(t):
    r'\b open \b'
    t.type = reserved.get(t.value)
    return t


def t_IMP(t):
    r'\b imp \b'
    t.type = reserved.get(t.value)
    return t


def t_ALL(t):
    r'\b all \b'
    t.type = reserved.get(t.value)
    return t


def t_INFO(t):
    r'\b [a-zA-Z0-9._]* \b'
    t.type = "INFO"
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()