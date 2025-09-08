#!/usr/bin/env python3
import time
import sqlite3
import functools

# Simple in-memory cache
query_cache = {}

# Reuse with_db_connection from previous tasks
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

# Cache decorator
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query string
        query = kwargs.get("query") if "query" in kwargs else args[1] if len(args) > 1 else None
        if query is None:
            return func(*args, **kwargs)

        # Return cached result if available
        if query in query_cache:
            print("Returning cached result")
            return query_cache[query]

        # Execute and cache the result
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

# Fetch users with caching
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


if __name__ == "__main__":
    # First call will cache the result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(users)

    # Second call will use the cached result
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(users_again)

