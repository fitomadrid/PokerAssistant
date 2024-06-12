import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DATABASE_PATH = os.getenv("DATABASE_PATH", "poker_assistant.db")

CREATE_HANDS_TABLE = """CREATE TABLE IF NOT EXISTS hands (
                            id INTEGER PRIMARY KEY,
                            hand TEXT NOT NULL,
                            result TEXT NOT NULL
                        );"""

def connect_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        print("Connection to the database is successful.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    try:
        cursor = conn.cursor()
        cursor.execute(CREATE_HANDS_TABLE)
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

def insert_hand(conn, hand, result):
    try:
        sql = '''INSERT INTO hands(hand, result) VALUES(?,?)'''
        cur = conn.cursor()
        cur.execute(sql, (hand, result))
        conn.commit()
        print("Hand data inserted successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting hand data: {e}")

def fetch_hands(conn):
    try:
        sql = '''SELECT * FROM hands'''
        cur = conn.cursor()
        cur.execute(sql)
        
        rows = cur.fetchall()
        
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(f"Error fetching hands data: {e}")

if __name__ == "__main__":
    conn = connect_implugin_hand(conn, "5H 5C 6S 7S KD", "Pair of Fives")
    fetch_hands(conn)
    
    if conn:
        conn.close()