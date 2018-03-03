#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import codecs
import os
import sys
import time

progress_bar =""
i = 0;
limit = 11
ascii_progress = 178
ascii_no_progress = 176

for index in range(0, 11):
    time.sleep(0.2)
    progress_bar = "| "
    for i in range(0, index):
        progress_bar += " ═ "
    limit-=1;
    for j in range(0, limit):
        progress_bar += " - "

    progress_bar += " | " + str(index*10) + "%"
    os.system("cls")

    print("\n\n\n\tLEXER VIKINGS ")
    print("\t..CARGANDO.. ")
    print("\t" , progress_bar)