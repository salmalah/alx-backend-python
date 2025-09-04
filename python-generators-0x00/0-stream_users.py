#!/usr/bin/python3
import mysql.connector

def stream_users():
    """Generator that yields rows from user_data one by one as dictionaries"""
    try:
        connection = mysql.connector.connect(
            host='localhost',   # replace if needed
            user='root',
            password='',        # replace with your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)  # fetch rows as dicts
        cursor.execute("SELECT * FROM user_data;")
        for row in cursor:  # only one loop
            yield row

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
