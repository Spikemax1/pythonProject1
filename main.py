import sqlite3
from sqlite3 import Error

sql_create_projcet_table = """  CREATE TABLE IF NOT EXISTS projects (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                begin_date text,
                                end_date text
                            ); """
sql_create_tasks_table = """    CREATE TABLE IF NOT EXISTS tasks (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                priority integer,
                                status_id integer NOT NULL,
                                project_id integer NOT NULL,
                                begin_date text NOT NULL,
                                end_date text NOT NULL,
                                FOREIGN KEY(project_id) REFERENCES projects (id)
                            ); """

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_project(conn, project):
    sql = """   INSERT INTO projects(name, begin_date, end_date) 
                VALUES (?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid

def create_task(conn, tasks):
    sql = """   INSERT INTO tasks(name, priority, status_id, project_id, begin_date,
                end_date) VALUES (?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, tasks)
    return cur.lastrowid

#project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
#project_id = create_project(create_connection('test_db'), project)

#task_1 = ('Analyze the requirements of the app', 1, 1, project_id, '2015-01-01', '2015-01-02')
#task_2 = ('Confirm with user about the top requirements', 1, 1, project_id, '2015-01-03', '2015-01-05')

#create_task(create_connection('test_db'),task_1)
#create_task(create_connection('test_db'),task_2)

conn = create_connection('test_db')
c = conn.cursor()
c.execute("""SELECT * FROM projects """)
print(c.fetchone())