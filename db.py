import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()

DB_PATH = os.getenv("DATABASE_PATH", "poker_assistant.db")

SQL_CREATE_HANDS_TABLE = """CREATE TABLE IF NOT EXISTS hands (
                            id INTEGER PRIMARY KEY,
                            hand TEXT NOT NULL,
                            outcome TEXT NOT NULL
                        );"""

def db_connect():
    try:
        connection = sqlite3.connect(DB_PATH)
        print("Connection to the database is successful.")
        return connection
    except sqlite3.Error as error:
        print(f"Error connecting to database: {error}")
        return None

def create_hands_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute(SQL_CREATE_HANDS_TABLE)
        print("Hands table created successfully.")
    except sqlite3.Error as error:
        print(f"Error creating hands table: {error}")

def insert_hand_record(connection, poker_hand, outcome):
    try:
        insert_query = '''INSERT INTO hands(hand, outcome) VALUES(?,?)'''
        cursor = connection.cursor()
        cursor.execute(insert_query, (poker_hand, outcome))
        connection.commit()
        print("Poker hand data inserted successfully.")
    except sqlite3.Error as error:
        print(f"Error inserting poker hand data: {error}")

def retrieve_hand_records(connection):
    try:
        select_query = '''SELECT * FROM hands'''
        cursor = connection.cursor()
        cursor.execute(select_query)
        
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f"Error fetching poker hands data: {error}")

if __name__ == "__main__":
    connection = db_connect()
    
    if connection:  # Ensure connection was successful before proceeding
        create_hands_table(connection)
        insert_hand_record(connection, "5H 5C 6S 7S KD", "Pair of Fives")
        retrieve_hand_records(connection)

        connection.close()