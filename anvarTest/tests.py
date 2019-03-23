import sqlite3
from sqlite3 import Error
from importFiles import *
from create_db import create_db
from datetime import date


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
    for product in cur.fetchall():    
        for order in receive_data():
            if order['name'] == product[1]:
                if if_date(product[0], receive_date()) == False:
                    print("NO!")
                else:
                    print("Yes")
        
    conn.commit()
    conn.close()

#print(if_date(1, receive_date()))
fill_price()