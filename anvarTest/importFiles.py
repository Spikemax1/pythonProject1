# -*- coding: utf8 -*-

import codecs
import os
import datetime

def text_imp():
    path = u''+'import_files/text'
    with codecs.open(path, "r", "utf-8") as file:
        str = file.read()  
    arr = str.split("\n")  
    return arr  

def receive_date():
    arr = text_imp()
    date = arr[0].split(' ')
    date = date[-3].strip()
    arr = date.split('.')
    arr.reverse()
    date = datetime.date(int(arr[0]), int(arr[1]), int(arr[2]))
    return date

def receive_bill():
    arr = text_imp()
    bill = arr[-2].split(':')[-1]
    return bill.strip()

def receive_data():
    arr = text_imp()
    data = arr[1:-2]
    newData = []
    for x in data:
        arr = x.split(" ")
        xcount = float(arr[-1])
        xprice = float(arr[-2])
        xname = arr[0: -2]        

        xname = " ".join(xname)
        add_dict = {'name': xname, 'price': round(xprice / xcount)}
        newData.append(add_dict)
    return newData
    

