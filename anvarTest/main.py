# -*- coding: utf8 -*-
import sqlite3
from sqlite3 import Error
from importFiles import *
from datetime import date

def receive_name(name, db_name):
    try:
        conn = sqlite3.connect(db_name)
    except Error as e:
        print(e)
        exit()
    cur = conn.cursor()
    search_name = (name,)
    answer = False
    sql =   """
            SELECT name FROM products;
            """
    cur.execute(sql)
    for x in cur.fetchall():
        if x == search_name:
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

        #Запомнит это! 

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
                                    id integer PRIMARY KEY NOT NULL,
                                    price INTEGER,
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

def 


add_price("db/anv_db", 2, 123)
#import_into_db("db/anv_db")
    

