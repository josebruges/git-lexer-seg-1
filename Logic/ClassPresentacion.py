import re
import codecs
import os
import sys
import time
from Logic.ClassLexer import *
import win32com.client

class ClassPresentacion:

    #Caracteres para la barra de progreso
    caracter_inicio = "| "
    caracter_fin = " | "
    caracter_progress = " ═ "
    caracter_no_progress = " - "


    def barra_de_progreso(self):
        os.system("cls")
        progress_bar = ""
        limit = 11

        for index in range(0, 11):
            time.sleep(0.2)
            progress_bar = self.caracter_inicio
            for i in range(0, index):
                progress_bar += self.caracter_progress
            limit -= 1;
            for j in range(0, limit):
                progress_bar += self.caracter_no_progress

            progress_bar += self.caracter_fin + str(index * 10) + "%"
            os.system("cls")

            print("\n\n\n\tLEXER VIKINGS ")
            print("\t..CARGANDO.. ")
            print("\t", progress_bar)

    def hablar (self, mensaje):
        speaker = win32com.client.Dispatch("SAPI.SpVoice")
        speaker.Speak(mensaje)