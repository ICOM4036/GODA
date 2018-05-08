import ply.yacc as yacc
import Lexer
from Lexer import tokens
# P&L

def p_statement(p):
    '''
    statement : statement_parseCommand
    '''
    print(p)
    p[0] = p[1]
    pass


def p_statement_parseCommand(p):
    '''
    statement_parseCommand : COMMAND DS
                            | INFO
    '''
    if len(p)== 2:
        p[0] = {"info":p[1]}
    elif len(p)== 3:
        p[0] = {"command": p[1], "ds": p[2]}
    else:
        print("Syntax error in input!!")


def p_error(p):
    if not p:
        print("Syntax error in input!!")


parser = yacc.yacc()