import os

def text_imp():
    with open('import_files/text', "r") as file:
        str = file.read()    
    arr = str.split("\n")  
    return arr  

def receive_date():
    arr = text_imp()
    date = arr[0].split(' ')
    date = date[-3]
    return date.strip()

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
        xcount = arr[-1]
        xprice = arr[-2]
        xname = arr[0: -2]
        xname = " ".join(xname)
        add_dict = {'name': xname, 'count': xcount, 'price': xprice}
        newData.append(add_dict)
    return newData
    


