import mysql.connector

config = {
    'host' : 'localhost',
    'user' : 'root',
    'password' : '8979826321luffy',
    'database' : 'test'
}
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)