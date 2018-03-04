import re
import codecs
import os
import sys
import time
from Logic.ClassLexer import *

import win32com.client

class ClassTok(object):

    type = ""
    value = ""
    lineno = ""
    lexpos = ""

    def __init__(self, type, value, lineno, lexpos):
        self.type = type
        self.value = value
        self.lineno = lineno
        self.lexpos = lexpos

    @classmethod
    def new(cls, type, value, lineno, lexpos):
        return ClassTok(type, value, lineno, lexpos)





