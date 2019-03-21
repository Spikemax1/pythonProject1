# -*- coding: utf8 -*-
import sqlite3
from sqlite3 import Error
from importFiles import *
from datetime import date
import datetime

def receive_name(name, db_name):
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
        return False
    cur = conn.cursor()
    search_name = (name,)
    answer = False
    sql =   """
            SELECT name FROM list_products;
            """
    cur.execute(sql)
    for x in cur.fetchall():
        if x == search_name:
            answer = True
            break

    conn.close()
    return answer

def date_if_exists(db_name, my_id, my_date):
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
        return False
    cur = conn.cursor()
    search = (my_id, my_date,)
    answer = False
    sql =   """
            SELECT id,date FROM products_price;
            """
    try:
        cur.execute(sql) 
    except:
        return False       
    
    for x in cur.fetchall():
        if x[0] == my_id and str(x[1]) == str(my_date):
            answer = True
            break
    conn.close()
    return answer


def import_into_db(db_name):
    try:
        conn = sqlite3.connect(db_name)
        print(sqlite3.version)
    except Error as e:
        print(e)
        exit()

    cur = conn.cursor()
    sql_create_project_table = """ 
                                CREATE TABLE IF NOT EXISTS list_products (
                                id integer PRIMARY KEY AUTOINCREMENT,
                                name text UNIQUE NOT NULL
                            ); 

                            """
    
    cur.execute(sql_create_project_table)
    
    sql =   """
            INSERT INTO list_products(name) VALUES(?)
            """

    for x in receive_data():       
        ans = receive_name(x['name'], "db/anv_db") 

        #Запомнить это! 

        product = (x['name'],)    
        if ans == False:            
            cur.execute(sql, product)
        
        
    conn.commit()
    conn.close()

def add_price(db_name, ins_id, ins_price):
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
        exit()


    cur = conn.cursor()
    my_date = receive_date()
    sql_create_project = """
                                    CREATE TABLE IF NOT EXISTS products_price(
                                    id integer,
                                    price integer,
                                    date text
                                );
                                """
    cur.execute(sql_create_project)

    sql_ins =   """
                INSERT INTO products_price(id, price, date) VALUES(?,?,?)
                """
    conn.execute(sql_ins, (ins_id, ins_price, my_date))
    conn.commit()
    conn.close()

def fill_price_list(db_name):
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
        exit()
    cur = conn.cursor()
    sql =   """
            SELECT id,name FROM list_products; 
            """    
    cur.execute(sql)
    bill_data = receive_data()

    for x in cur.fetchall():
        for j in bill_data:
            if x[1] == j['name']:   
                ans = date_if_exists(db_name, x[0], receive_date()) 
                if ans == False:
                    add_price(db_name, x[0], int(j['price']))   
    
import_into_db("db/anv_db")
fill_price_list("db/anv_db")


#import_into_db("db/anv_db")
    

