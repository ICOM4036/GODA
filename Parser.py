import ply.yacc as yacc
import Lexer
from Lexer import tokens
# P&L

#Check this carefully with the newly added statements
#Make sure that every thing is working correctly

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
                            | INFO COLON TYPE
    '''
    if len(p)== 2:
        p[0] = {"command":p[1]}
    elif len(p)== 3:
        p[0] = {"command": p[1], "ds": p[2]}
    elif len(p) == 4:
        p[0] = {"info": p[1], "type": p[3]}
    else:
        p[0] = {"command":p[1],"command2":p[2]}


def p_statement_parseInfo(p):
    '''
    statement_parseCommand : INFO
    '''
    p[0] = {"info":p[1]}

def p_error(p):
    if not p:
        print("Syntax error in input!!")


parser = yacc.yacc()