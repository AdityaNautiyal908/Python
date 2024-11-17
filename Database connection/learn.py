import mysql.connector as myConn
from mysql.connector import Error

def create_connection():
    try:
        connection = myConn.connect(
            host = "localhost",
            user = "root",
            password = "8979826321luffy"
        )
        if connection.is_connected():
            print("Successfully connected")
            return connection
    
    except Error as e:
        print(f"Error : {e}")
        return None
        
def show_database(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    database = cursor.fetchall()

    if database:
        print()
        print("All Databases")
        for i, val in enumerate(database,start = 1):
            print(f"{i}.{val[0]}")
    else:
        print("No Database found")
            
def create_database(connection):
    db_name = input("Enter the name of database : ").strip()

    if db_name:
        try:
            cursor = connection.cursor()
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"{db_name} created successfully")
        except Error as e:
            print(f"Error : {e}")
    else:
        print("Please enter a valid database name")
        
def drop_database(connection):
    db_name = input("Enter the database name you want to drop : ").strip()

    if db_name:
        try:
            cursor = connection.cursor()
            cursor.execute(f"Drop database {db_name}")
            print(f"{db_name} dropped successfully")
        except Error as e:
            print(f"Error : {e}")
    else:
        print("Please enter a valid database name")

def use_database(connection):
    db_name = input("Enter the database you want to work on : ").strip()

    if db_name:
        try:
            cursor = connection.cursor()
            cursor.execute(f"USE {db_name}")
            print(f"\nYou are now working on {db_name} database")
        except Error as e:
            print(f"Error : {e}")
    else:
        print("Database not in the system. Please try again")
    
def main_menu():
    connection = create_connection()
    if not connection:
        return
    while True:
        print("\nMAIN MENU")
        print(""" 
            1. Show Database
            2. Create Database
            3. Drop Database
            4. Use Database
            5. Exit
""")

        choice = input("Enter your choice (1/2/3/4/5) : ").strip()

        if choice == '1':
            show_database(connection)
        
        elif choice == '2':
            create_database(connection)

        elif choice == '3':
            drop_database(connection)
        
        elif choice == '4':
            use_database(connection)
        
        elif choice == '5':
            print("Exiting program")
            connection.close()
            break
        else:
            print("Invalid input please, Try again")


if __name__ == "__main__":
    main_menu()

