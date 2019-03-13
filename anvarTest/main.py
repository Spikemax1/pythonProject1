import sqlite3
from sqlite3 import Error
from importFiles import *

def import_into_db():
    try:
        conn = sqlite3.connect("db/anv_db")
        print(sqlite3.version)
    except Error as e:
        print(e)
        exit()

    cur = conn.cursor()
    sql_create_projcet_table = """  CREATE TABLE IF NOT EXISTS products (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                count text,
                                price text,
                                date text
                            ); """
    cur.execute(sql_create_projcet_table)

    cur.execute("""
                    INSERT INTO products(name,count,price, date) VALUES('one', '123', '3', '2018.02.19')
            """)
    
    conn.commit()
    conn.close()

import_into_db()
    

