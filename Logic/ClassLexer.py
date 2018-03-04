import Controller.ply.lex as lex
import re
import codecs
import os
import sys


class Lexer:
    def __init__(self, ruta):
        self.direcctorio = ruta
        self.analizador = lex.lex()
        self.cadena = ""
        # Mis Tokens
        self.tokens = ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                  'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
                  'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM',
                  'DOT', 'UPDATE'
                  ]

        self.reservadas = {
            'begin': 'BEGIN',
            'end': 'END',
            'if': 'IF',
            'then': 'THEN',
            'while': 'WHILE',
            'do': 'DO',
            'call': 'CALL',
            'const': 'CONST',
            'int': 'VAR',
            'procedure': 'PROCEDURE',
            'out': 'OUT',
            'in': 'IN',
            'else': 'ELSE'
        }

        self.tokens = self.tokens + list(self.reservadas.values())

        self.t_ignore = '\t '
        self.t_PLUS = r'\+'
        self.t_MINUS = r'\-'
        self.t_TIMES = r'\*'
        self.t_DIVIDE = r'/'
        self.t_ODD = r'ODD'
        self.t_ASSIGN = r'='
        self.t_NE = r'<>'
        self.t_LT = r'<'
        self.t_LTE = r'<='
        self.t_GT = r'>'
        self.t_GTE = r'>='
        self.t_LPARENT = r'\('
        self.t_RPARENT = r'\)'
        self.t_COMMA = r','
        self.t_SEMMICOLOM = r';'
        self.t_DOT = r'\.'
        self.t_UPDATE = r':='





    def abrir_documento(self):
        if os.path.isfile(self.direcctorio):
            fp = codecs.open(self.direcctorio, "r", "utf-8")
            self.cadena = fp.read()
            fp.close()
            return True
        else:
            return False

    def analizador_lexer(self):
        self.analizador.input(self.cadena)
        while True:
            tok = self.analizador.token()
            if not tok: break
            print(tok.type, tok.value, tok.lineno, tok.lexpos)



    # Reconoce e imprime cualquier identificador (tokens)
    def t_ID(self,t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.upper() in self.reservadas:
            t.value = t.value.upper()
            t.type = t.value

        return t

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Funcion encargada de reconocer un comentario
    # signo (*): define que el tokens debe ser asignado 0 ó N
    def t_COMMENT(t):
        r'\#.*'
        pass

    # signo (+): define que el tokens debe ser asignado 1 ó N
    def t_NUMBER(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_error(t):
        print("caracter ilegal ", t.type, " - ", t.value[0], " - ", t.lineno, " - ", t.lexpos)
        t.lexer.skip(1)