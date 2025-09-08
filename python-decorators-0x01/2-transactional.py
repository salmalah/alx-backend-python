#!/usr/bin/env python3
import sqlite3
import functools

# Reuse the with_db_connection decorator
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            result = func(conn, *args, **kwargs)
        finally:
            conn.close()
        return result
    return wrapper

# Transactional decorator
def transactional(func):
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()  # commit if function succeeds
            return result
        except Exception as e:
            conn.rollback()  # rollback if an exception occurs
            raise e
    return wrapper

# Update user's email with automatic transaction handling
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

# Example usage
if __name__ == "__main__":
    update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
    print("User email updated successfully!")

