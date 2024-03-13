import sqlite3

conn=sqlite3.connect("student.db")

table="""CREATE TABLE STUDENTS( USN VARCHAR(25),NAME VARCHAR(50), SECTION VARCHAR(25), MARKS INT);"""

conn.execute(table)

conn.execute('''INSERT INTO STUDENTS VALUES ('CSE020','ARIYA MALHOTRA','B',92)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE036','DAVID RAI','C',97)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE060','GEETA MADUMOHAN','A',98)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE070','JYOTHI S','A',95)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE093','LAKSH R MATHUR','A',98)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE112','MOHAN MRIDYA','C',89)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE138','PRAVEEN SINGH','B',47)''')
conn.execute('''INSERT INTO STUDENTS VALUES ('CSE165','SUHAS ROY','B',76)''')

cursor=conn.cursor()

sql1=cursor.execute("""Select * FROM STUDENTS;""")

for row in sql1:
  print(row)

conn.commit()
conn.close
