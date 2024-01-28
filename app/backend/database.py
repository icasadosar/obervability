
import mysql.connector
import os

MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DB = os.getenv("MYSQL_DB")

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

def initialize_db():
    conn = connect()
    cursor = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS items (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255)
    )
    """
    cursor.execute(query)
    conn.close()

def create_item(name):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO items VALUES (name) VALUES (%s)"
    values = (name)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def read_item(id):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT name FROM items WHERE 1=1"
    if id:
        query = query + " AND id = '%s'"
    values = (id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid, cursor.lastrowname

def update_item(id, name):
    if not isinstance(id, int):
        raise "'id' must be integer."
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE items SET name=%s WHERE id = '%s'"
    values = (name, id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.lastrowid

def delete_item(id):
    if not id:
        raise "'id' cannot be empty."
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM items WHERE id = '%s'"
    values = (id)
    cursor.execute(query, values)
    conn.commit()
    conn.close()
    return cursor.rowcount