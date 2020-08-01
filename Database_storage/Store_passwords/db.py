import psycopg2

DB_NAME = "xnlrlerp"
DB_USER = "xnlrlerp"
DB_PASS = "vgj6fprlZ13EN_-LghLPtSEa5AIMmpL3"
DB_HOST = "dumbo.db.elephantsql.com"
DB_PORT = "5432"



def create():
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("CREATE TABLE  password_storage (id SERIAL PRIMARY KEY, platform TEXT, password TEXT NOT NULL)")
    conn.commit()
    conn.close()


def insert(name, pwd):
    conn = psycopg2.connect(database = DB_NAME, user = DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO password_storage (platform, password) VALUES (%s, %s);", (name, pwd))
    conn.commit()
    conn.close()

def view_all():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM password_storage;")
    list_schemas = cur.fetchall()
    for value in list_schemas:
        print(value[1], value[2])
    conn.commit()
    conn.close()

def view_pass(name):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT password FROM password_storage WHERE platform = %s;", (name,))
    list_schemas = cur.fetchone()
    for password in list_schemas:
        print(password)
    conn.commit()
    conn.close()

def view_platforms():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT platform FROM password_storage;")
    platforms = cur.fetchall()
    for plat in platforms:
        print(plat[0])
    conn.commit()
    conn.close()

def delete_one(name):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM password_storage WHERE platform = %s;", (name,))
    conn.commit()
    conn.close()
