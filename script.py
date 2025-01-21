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
from students import Student

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


# from student import Student



# creating students objects
std_one = Student('Paul', 'Ngetich', 87)

std_two = Student('Joy', 'Kirui', 57)

# Creating functions to run queries

def insert_std(std):
    with conn:
        c.execute("INSERT INTO students VALUES('{}', '{}', '{}')".format(std.first_name, std.last_name,std.grade))

def get_std_name(first_name, last_name):
    c.execute("SELECT * FROM students WHERE first_name = ? AND last_name = ?", (first_name, last_name))
    return c.fetchall()

def update_grade(std, grade):
    with conn:
        c.execute("UPDATE students SET grade = ? WHERE first_name = ? AND last_name = ?", 
                  (grade, std.first_name, std.last_name))
        
def remove_std(std):
    with conn:
        c.execute("DELETE FROM students WHERE first_name = ? AND last_name = ?", 
                  (std.first_name, std.last_name))


# calling the functions
insert_std(std_one) 

student_results = get_std_name('Damaris',"Kerubo")
print(student_results)

# update_grade(std_one)
update_grade(std_one, 95)

# Remove a student from the database
# to_be_deleted = Student("Paul", "Ngetich", 87)
# remove_std(to_be_deleted)


conn.commit()
conn.close()