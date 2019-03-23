import sqlite3
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
    
def fill_products():
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor() 
    sql =   """
            INSERT INTO products_list(name) VALUES(?);
            """
    for x in receive_data():       
        ans = if_name(x['name']) 
        product = (x['name'],)    
        if ans == False:            
            cur.execute(sql, product)
    conn.commit()
    conn.close()

def fill_price():
    try:
        conn = sqlite3.connect('db/anv_db')
    except Error as e:
        print(e)
    cur = conn.cursor()
    sql =   """
            INSERT INTO products_price(id, price, date_incoming) VALUES(?,?,?);
            """  
    cur.execute("""SELECT * FROM products_list;""") 
    bill_data = receive_data()
    for product in cur.fetchall():    
        for order in bill_data:
            if order['name'] == product[1]:
                if if_date(product[0], receive_date()) == False:
                    cur.execute(sql, (product[0], order['price'], receive_date()))
        
    conn.commit()
    conn.close()

    
fill_products()
fill_price()

    
