import sqlite3
from sqlite3 import Error

try:
    conn = sqlite3.connect('anv_db')
except Error as e:
    print(e)

cur = conn.cursor()
#cur.execute("DROP TABLE products_list")
#cur.execute("DROP TABLE products_price")
sql_products =   """
        SELECT * FROM products_list;
        """
sql_products_price =   """
        SELECT * FROM products_price;
        """
cur.execute(sql_products)

for x in cur.fetchall():
    print(x, end="\n")

cur.execute(sql_products_price )

for x in cur.fetchall():
    print(x, end="\n")

#sql = """
#        INSERT INTO products_list(name) VALUES(?);
#    """
#elem = ("Test 1", )
#cur.execute(sql, elem)
#conn.commit()

conn.close()


