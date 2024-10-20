import pg8000

# Database connection
conn = pg8000.connect(database="postgres", user="postgres", password="123", host="localhost", port="5432")
cur = conn.cursor()

# Get input from the user
name = input("Please enter your name: ")
age = input("Please enter your age: ")
address = input("Please enter your address: ")

# Correct query and execution
query = '''INSERT INTO students (name, age, address) VALUES (%s, %s, %s);'''
try:
    cur.execute(query, (name, age, address))
    conn.commit()  # Commit the transaction
    print("Data inserted successfully!")
except pg8000.ProgrammingError as e:
    print("Error: ", e)
finally:
    cur.close()
    conn.close()
