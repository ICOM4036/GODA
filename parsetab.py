
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMAND DS INFO\n    statement : statement_parseCommand\n    \n    statement_parseCommand : COMMAND DS\n                            | INFO\n    '
    
_lr_action_items = {'COMMAND':([0,],[3,]),'INFO':([0,],[4,]),'$end':([1,2,4,5,],[0,-1,-3,-2,]),'DS':([3,],[5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'statement_parseCommand':([0,],[2,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> statement_parseCommand','statement',1,'p_statement','Parser.py',11),
  ('statement_parseCommand -> COMMAND DS','statement_parseCommand',2,'p_statement_parseCommand','Parser.py',20),
  ('statement_parseCommand -> INFO','statement_parseCommand',1,'p_statement_parseCommand','Parser.py',21),
]