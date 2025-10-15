import sqlite3
##connect to sqlite
connection = sqlite3.connect("student.db")
##create a cursor object to insert record,create table ,retrieve
cursor = connection.cursor()
##create a table
table_info = """CREATE TABLE IF NOT EXISTS student(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)
##insert record
cursor.execute("INSERT INTO student VALUES('Krish','Data Science','A',90)")
cursor.execute("INSERT INTO student VALUES('Sudhanshu','Data Science','B',100)")
cursor.execute("INSERT INTO student VALUES('Darius','Data Science','A',86)")
cursor.execute("INSERT INTO student VALUES('Vikas','DEVOPS','A',50)")
cursor.execute("INSERT INTO student VALUES('Dipesh','DEVOPS','A',35)")

#Display all the records
print("The inserted records are:")
data = cursor.execute("SELECT * FROM student")
for row in data:
    print(row)
#close connection
connection.commit()
connection.close()