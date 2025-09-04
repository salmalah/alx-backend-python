#!/usr/bin/python3
seed = __import__('seed')

def stream_user_ages():
    """Generator that yields user ages one by one"""
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT age FROM user_data;")
    
    for row in cursor:  # first loop
        yield row['age']
    
    cursor.close()
    connection.close()


def compute_average_age():
    """Compute the average age using the generator"""
    total = 0
    count = 0
    
    for age in stream_user_ages():  # second loop
        total += age
        count += 1
    
    if count == 0:
        return 0
    return total / count


if __name__ == "__main__":
    average_age = compute_average_age()
    print(f"Average age of users: {average_age}")
