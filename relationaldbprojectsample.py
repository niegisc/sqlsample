import sqlite3

def menu():
  print("Sports Club")
  print("(1) List all tables")
  print("(2) Show table records")
  print("(3) Insert record(s)")
  print("(4) Update record(s)")
  print("(5) Delete record(s)")
  print("(6) Courses not more than $x")
  print("(0) Quit")

def list_tables():
  cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
  records = cursor.fetchall()
  for record in records:
    print(record[0])

def show_records():
  list_tables()
  table = input("Choose table: ")
  query = "SELECT * FROM " + table + ";"
  cursor.execute(query)
  records = cursor.fetchall()
  for record in records:
    print(record)

def insert_record():
  list_tables()
  table = input("Choose table: ")
  if table == "Course":
    course_code = input("Enter course code: ")
    description = input("Enter description: ")
    fee = float(input("Enter fee: "))
  query = "INSERT INTO " + table + "(CourseCode, Description, Fee) VALUES(?, ?, ?);"
  cursor.execute(query, (course_code, description, fee))
  connection.commit()
  # show records to confirm insert
  query = "SELECT * FROM " + table + ";"
  cursor.execute(query)
  records = cursor.fetchall()
  for record in records:
    print(record)

def update_record():
  list_tables()
  table = input("Choose table: ")
  if table == "Course":
    course_code = input("Enter course code: ")
    fee = float(input("Enter new fee: "))
  query = "UPDATE " + table + " SET Fee = ? WHERE CourseCode = ?;"
  cursor.execute(query, (fee, course_code))
  connection.commit()
  # show records to confirm update
  query = "SELECT * FROM " + table + ";"
  cursor.execute(query)
  records = cursor.fetchall()
  for record in records:
    print(record)

def delete_record():
  list_tables()
  table = input("Choose table: ")
  if table == "Course":
    course_code = input("Enter course code: ")
  query = "DELETE FROM " + table + " WHERE CourseCode = ?;"
  cursor.execute(query, (course_code, ))
  connection.commit()
  # show records to confirm delete
  query = "SELECT * FROM " + table + ";"
  cursor.execute(query)
  records = cursor.fetchall()
  for record in records:
    print(record)

def courses_lte_x():
  x = input("Enter max fee: ") 
  query = "SELECT * FROM Course WHERE Fee <= " + x + " ORDER BY Fee, Description;"
  cursor.execute(query)
  records = cursor.fetchall()
  for record in records:
    print(record)
  print(len(records))

# main
# create database connection
connection = sqlite3.connect("sports_club.db")

# create cursor
cursor = connection.cursor()

option = ''
while option != '0':
  menu()
  option = input("Enter option: ")
  if option == '1':
    list_tables()
  elif option == '2':
    show_records()
  elif option == '3':
    insert_record()
  elif option == '4':
    update_record()
  elif option == '5':
    delete_record()
  elif option == '6':
    courses_lte_x()
  elif option != '0':
    print("Valid options are 0 to 5")
  else:
    print("Bye")
  print()

# destroy database connection (and cursor)
connection.close()
