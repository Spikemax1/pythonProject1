import sqlite3
import os
from sqlite3 import Error
from importFiles import *
from create_db import create_db
from datetime import date

create_db()

def if_name(my_name):   
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()  
    ans = False
    sql =   """
            SELECT name FROM products_list;
            """
    elem = (my_name,)
    cur.execute(sql)
    for x in cur.fetchall():
        if elem == x:
            ans = True
            break
    conn.close()
    return ans    
    
def if_date(my_id, my_date):   
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()  
    ans = False
    sql =   """
            SELECT id, date_incoming FROM products_price;
            """
    cur.execute(sql)
    for x in cur.fetchall():
        a = str(x[1])
        newDay = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
        if my_id == x[0] and my_date == newDay:
            ans = True
            break

    conn.close()
    return ans     
    
def fill_products(path):
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor() 
    sql =   """
            INSERT INTO products_list(name) VALUES(?);
            """
    for x in receive_data(path):       
        ans = if_name(x['name']) 
        product = (x['name'],)    
        if ans == False:            
            cur.execute(sql, product)
    conn.commit()
    conn.close()

def fill_price(path):
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()
    sql =   """
            INSERT INTO products_price(id, price, date_incoming) VALUES(?,?,?);
            """  
    cur.execute("""SELECT * FROM products_list;""") 
    bill_data = receive_data(path)
    for product in cur.fetchall():    
        for order in bill_data:
            if order['name'] == product[1]:
                if if_date(product[0], receive_date(path)) == False:
                    cur.execute(sql, (product[0], order['price'], receive_date(path)))
        
    conn.commit()
    conn.close()

def if_bill(my_bill, my_date):
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()
    sql =   """
            SELECT * FROM total_costs;
            """
    ans = False
    cur.execute(sql)
    for x in cur.fetchall():
        a = str(x[2])
        newDay = datetime.datetime.strptime(a, "%Y-%m-%d %H:%M:%S")
        if x[1] == my_bill and newDay == my_date:
            ans = True
            break
    conn.close()
    return ans

def insert_bill(path):
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()
    my_date = receive_date(path)
    my_bill = receive_bill(path)

    sql =   """
            INSERT INTO total_costs(total, date_bill) VALUES(?, ?);
            """
    if if_bill(my_bill, my_date) == False:
        cur.execute(sql, (my_bill, my_date,))
    
    conn.commit()
    conn.close()





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
        fill_products(new_path)
        insert_bill(new_path)
        fill_price(new_path)
    for x in range(num):
        myfile = 'import_files/text'+ x.__str__()
        if os.path.isfile(myfile):
            os.remove(myfile)
import_from_alltext()



    
