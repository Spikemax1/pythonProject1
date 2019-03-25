import sqlite3
from sqlite3 import Error
from importFiles import *
from create_db import create_db
from datetime import date
import os
import codecs


def import_from_alltext():

    path = u'' + 'import_files/alltext'

    with codecs.open(path, "r", "utf-8") as file:
        str = file.read().strip()
    arr = str.split("Гипермаркет №1")
    new_arr = []
    num = 1
    for x in arr:
        if x == "":
            continue
        else:
            new_path = 'import_files/text'+ num.__str__()
            with codecs.open(new_path, "w", "utf-8") as somefile:
                somearr = x.split("\n")
                for a in range(3):
                    small_arr = somearr[-1].split(" ")
                    if "Итого:" in small_arr:
                        continue
                    else:
                        somearr.pop()
                x = "\n".join(somearr)
                somefile.write(x)
            num+= 1

        print(receive_date(new_path))

import_from_alltext()