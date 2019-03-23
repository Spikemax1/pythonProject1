import sqlite3
from sqlite3 import Error
from importFiles import *
from create_db import create_db
from datetime import date
import os
import codecs


path = u''+'import_files/text2'
with codecs.open(path, "r", "utf-8") as file:
    str = file.read().strip()  
arr = str.split("\n")
new_arr = []
for a in arr:
    r = a.split(' ')
    if 'бонусов:' in r:
        continue
    else:
        new_arr.append(r)
arr = '\n'.join(new_arr)
print(arr)
