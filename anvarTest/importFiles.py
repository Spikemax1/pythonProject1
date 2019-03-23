import codecs
import os
import datetime

def text_extract():
    path = u''+'import_files/text'
    with codecs.open(path, "r", "utf-8") as file:
        str = file.read().strip()  
    new_str = ''
    for x in str:
        if(x == ','):
            x = '.'
        new_str += x
    arr = new_str.split("\n")  
    return arr
     

def receive_date():
    arr = text_extract()
    date = arr[0].split(' ')    
    buy_time = date[-1].split(":")
    #buy_time = datetime.time(int(buy_time[0]), int(buy_time[1]))
    buy_date = date[-3].strip()
    arr = buy_date.split('.')
    #arr.reverse()
    #buy_date = datetime.date(int(arr[0]), int(arr[1]), int(arr[2]))
    
    day = "{}/{}/{} {}:{}".format(int(arr[0]), int(arr[1]), int(arr[2]), int(buy_time[0]), int(buy_time[1]))
    
    return datetime.datetime.strptime(day, "%d/%m/%Y %H:%M")

def receive_bill():
    arr = text_extract()
    str = arr[-1].split(':')[-1]
    bill = str[0:-3].strip()
    return int(bill) 

def receive_data():
    arr = text_extract()
    data = arr[1:-1]
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
    

