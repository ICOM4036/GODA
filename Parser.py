import ply.yacc as yacc
import Lexer
from Lexer import tokens
from Lexer import reserved
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
                            | COMMAND
                            | COMMAND COMMAND
                            | INFO TYPE
                            | INFO
                            | COMMAS INFO COMMAS
                            | INFO INFO
    '''
    if len(p)== 2:
        if 'COMMAND' == reserved.get(p[1]):
            p[0] = {"command":p[1]}
        else:
            p[0] = {"info": p[1]}
    elif len(p)== 3:
        if 'DS' == reserved.get(p[2]):
            p[0] = {"command": p[1], "ds": p[2]}
        elif 'TYPE' == reserved.get(p[2]):
            p[0] = {"info": p[1], "type":p[2]}
        elif 'COMMAND' == reserved.get(p[2]):
            p[0] = {"command": p[1], "command2": p[2]}
        else:
           p[0] = {"info": p[1]+" "+p[2]}
    else:
        p[0] = {"info":p[2]}



def p_error(p):
    if not p:
        print("Syntax error in input!!")


parser = yacc.yacc()