#Modulo main.py
#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import codecs
import os
import sys
import time
from Logic.ClassLexer import *
from Logic.ClassPresentacion import *
import win32com.client

# URL = C:\Users\AngelaPelaez\Dropbox\COMPILADORES\LEXER_V2\Lenguajes\lenguaje2.jbc

#Barra de progreso
os.system("cls")
os.system("COLOR 3A")
present = ClassPresentacion()
present.barra_de_progreso()
present.hablar("bienvenido al lexerr vaikings")


#Abrir fichero
os.system("cls")
my_lexer = ClassLexer(input("\n\n\nIngrese URL: "))
if my_lexer.abrir_documento():
    print("\n\t Fichero encontrado\n\n")
    present.hablar("Fichero encontrado.")

    os.system("Pause")
    os.system("cls")
    print("\n URL:", my_lexer.direcctorio)
    my_lexer.analizador_lexer()
else:
    print("\n\t Error, el fichero no pudo ser encontrado")
    present.hablar("Error, el fichero no pudo ser encontrado")
os.system("Pause")




