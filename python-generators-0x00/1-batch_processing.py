#!/usr/bin/python3
import mysql.connector

def stream_users_in_batches(batch_size):
    """Generator that yields users from the database in batches"""
    try:
        connection = mysql.connector.connect(
            host='localhost',   # change if needed
            user='root',
            password='',        # your MySQL password
            database='ALX_prodev'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM user_data;")

        batch = []
        for row in cursor:  # only one loop here
            batch.append(row)
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:  # yield remaining rows
            yield batch

        cursor.close()
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def batch_processing(batch_size):
    """Generator that yields users older than 25"""
    for batch in stream_users_in_batches(batch_size):
        for user in batch:
            if user['age'] > 25:
                yield user  
    return  

