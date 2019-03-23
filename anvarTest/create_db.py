import sqlite3
from sqlite3 import Error
from importFiles import *

name_db = 'db/anv_db'

def create_db():
    try:
        conn = sqlite3.connect(name_db)
    except Error as e:
        print(e)
    cur = conn.cursor()
    sql_product_list =  """
                        CREATE TABLE IF NOT EXISTS products_list(
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL
                        );
                        """
    sql_products_price ="""
                        CREATE TABLE IF NOT EXISTS products_price(
                            id INTEGER,
                            price TEXT NOT NULL,
                            date_incoming DATETIME NOT NULL
                        );
                        """
    sql_total_costs =   """
                        CREATE TABLE IF NOT EXISTS total_costs(
                            id INTEGER PRIMARY KEY,
                            total INTEGER,
                            date_bill DATETIME NOT NULL UNIQUE
                        );
                        """

    cur.execute(sql_product_list)
    cur.execute(sql_products_price)
    cur.execute(sql_total_costs)

    conn.commit()
    conn.close()

create_db()