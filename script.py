# SQL

# What is SQL - a programming language that is used to manage relational 
               # databases and perform operations on the data that they contain.

# Installing and setting up sqlite
# sudo apt install sqlite3

# connect to the db

# Inserting values to the db using SQL queries

# Retriving data value from the db using SQL queries

# Data types in SQL
# NULL - represents "no value
# TEXT - 
# INTEGER -whole numbers
# REAL - old decimal
# BLOB - It is generally used for holding binary data.

import sqlite3

conn = sqlite3.connect('students.db')

# Creates a cursor object (c), which is used to interact with the database.
c = conn.cursor()

# Creating a table
# c.execute(""" CREATE TABLE students(
#           first_name text,
#           last_name text,
#           grade integer
#           )""")

# Inserting values to the table created
c.execute("INSERT INTO students VALUES ('Caleb', 'Bii', 99)")

# Retriving values from the db
c.execute("SELECT * FROM students WHERE last_name='Bii'")
print(c.fetchall())


# Inserting multiple students to the db

#  Define student data (using a dictionary for simplicity)
students = [
    {'first_name': 'Alice', 'last_name': 'Smith', 'grade': 90},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'grade': 85},
    {'first_name': 'Charlie', 'last_name': 'Ngetich', 'grade': 95},
    {'first_name': 'David', 'last_name': 'Lee', 'grade': 88},
    {'first_name': 'Eve', 'last_name': 'Ngetich', 'grade': 92},
]

# Insert multiple students using parameterized queries (prevents SQL injection)
for student in students:
    c.execute("INSERT INTO students VALUES (?, ?, ?)", (student['first_name'], student['last_name'], student['grade']))

# Query the database to fetch all records
c.execute("SELECT * FROM students")
results = c.fetchall()

# Print all records
for record in results:
    print(record)


conn.commit()

conn.close()

# Deleting a Table
c.execute("DROP TABLE students")
