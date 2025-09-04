#!/usr/bin/python3
import mysql.connector
import csv
import uuid

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # replace with your MySQL password
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(connection):
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev;")
    cursor.close()

def connect_to_prodev():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # replace with your MySQL password
            database='ALX_prodev'
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS user_data (
               user_id CHAR(36) PRIMARY KEY,
               name VARCHAR(255) NOT NULL,
               email VARCHAR(255) NOT NULL,
               age DECIMAL NOT NULL,
               INDEX idx_user_id(user_id)
           );"""
    )
    cursor.close()
    print("Table user_data created successfully")

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cursor.execute(
                """INSERT INTO user_data (user_id, name, email, age)
                   VALUES (%s, %s, %s, %s)
                   ON DUPLICATE KEY UPDATE name=VALUES(name), email=VALUES(email), age=VALUES(age);""",
                (str(uuid.uuid4()), row['name'], row['email'], row['age'])
            )
    connection.commit()
    cursor.close()
    print("Data inserted successfully")
