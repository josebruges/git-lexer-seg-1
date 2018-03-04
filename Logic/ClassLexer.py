#Modulo ClassLexer.py
#!/usr/bin/env python

import ply.lex as lex
import re
import codecs
import os
import sys
import time
from Logic.ClassLexer import *
from Logic.ClassTok import *
from Logic.ClassPresentacion import *

#Mis Tokens
reservadas_original = ['BEGIN',         #1
                       'END',           #2
                       'IF',            #3
                       'THEN',          #4
                       'WHILE',         #5
                       'DO',            #6
                       'CALL',          #7
                       'CONST',         #8
                       'VAR',           #9
                       'PROCEDURE',     #10
                       'OUT',           #11
                       'IN',            #12
                       'ELSE']          #13

reservadas = ['INIC_CODE',              #1
              'KILL_CODE',              #2
              'SAY',                    #3
              'MAKE',                   #4
              'SEA',                    #5
              'REALICE',                #6
              'VISIT',                  #7
              'FREEZE',                 #8
              'ZAVAGE',                 #9
              'PROCESS',                #10
              'KBOOM',                  #11
              'KIN',                    #12
              'ELSE']                   #13

tokens = reservadas+['ID','NUMBER','PLUS','MINUS','TIMES','DIVIDE',
		'ODD','ASSIGN','NE','LT','LTE','GT','GTE',
		'LPARENT', 'RPARENT','COMMA','SEMMICOLOM',
		'DOT','UPDATE'
		]

t_ignore = '\t '
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='



#Clase Lexer
class ClassLexer:

    def __init__(self, ruta):
        self.direcctorio = ruta
        self.analizador = ""
        self.cadena = ""

    @classmethod
    def new(cls, ruta):
        return ClassLexer(ruta)

    def abrir_documento(self):

        if os.path.isfile(self.direcctorio) and self.direcctorio.endswith(('.jbc')):
            fp = codecs.open(self.direcctorio, "r", "utf-8")
            self.cadena = fp.read()
            fp.close()
            return True
        else:
            return False

    def analizador_lexer(self):
        self.analizador = lex.lex()
        self.analizador.input(self.cadena)
        while True:
            tok = self.analizador.token()
            if not tok: break
            print("Token valido: ",tok)

#Reconoce e imprime cualquier identificador (tokens)
def t_ID (t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
        #print("Ingreso palabra reservada =", t,"\n")
    return t


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Funcion encargada de reconocer un comentario
# signo (*): define que el tokens debe ser asignado 0 ó N
def t_COMMENT ( t ):
    r'\#.*'
    pass

def t_COMMENTS ( t ):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
    pass

# signo (+): define que el tokens debe ser asignado 1 ó N
def t_NUMBER ( t ):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error ( t ):
    print ("\t* Token tipo: ", t.type,": ", t.value[0], ", Linea: ", t.lineno, ", ", t.lexpos)
    objeto = ClassTok(t.type, t.value[0], t.lineno, t.lexpos)
    obj_present = ClassPresentacion()
    obj_present.hablar("Error en la linea " + str(objeto.lineno))
    t.lexer.skip(1)


