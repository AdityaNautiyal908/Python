import mysql.connector as MyConn

mydb = MyConn.connect(host = "localhost", user="root" , password="8979826321luffy", database = "OnePiece")

db_cursor = mydb.cursor()

db_cursor.execute("select * from emp")

db_select = db_cursor.fetchall()

for i in db_select:
    print(i)


