import mysql.connector as myConn
import os
from dotenv import load_dotenv
from collections import deque

load_dotenv()
transaction_queue = deque()

def db_connect():
    password = os.getenv("DB_PASSWORD")
    connection = myConn.connect(
        user = "root",
        host = "localhost",
        password = password,
        database = "library"
    )
    
    return connection

def add_user(username,password,user_type="user"):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (username,password,user_type) VALUES (%s,%s,%s)",(username,password,user_type))
    connection.commit()
    cursor.close()
    connection.close()

def authenticate_user(username,password):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s",(username,password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def add_book(title,author,genre):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO books (title,author,genre,status) VALUES (%s,%s,%s ,'available') ",(title,author,genre))
    connection.commit()
    cursor.close()
    connection.close()

def borrow_book(user_id,book_id):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET status = 'borrowed',borrower_id = %s WHERE book_id = %s AND status = 'available'",(user_id,book_id))
    connection.commit()
    cursor.close()
    connection.close()

def return_book(book_id):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("UPDATE books SET status = 'available',borrower_id = NULL WHERE book_id = %s AND status = 'borrowed'",(book_id))
    connection.commit()
    cursor.close()
    connection.close()

def create_transaction(user_id,book_id,action):
    connection = db_connect()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO transactions (user_id,book_id,action,date) VALUES (%s,%s,%s,NOW())",(user_id,book_id,action))
    connection.commit()
    cursor.close()
    connection.close()
    
    transaction_queue.append((user_id,book_id,action))

class BookNode:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.left = None
        self.right = None

class BookSearchTree:
    def __init__(self):
        self.root = None

    def insert(self, book_id, title, author):
        self.root = self._insert(self.root, book_id, title, author)

    def _insert(self, root, book_id, title, author):
        if root is None:
            return BookNode(book_id, title, author)
        if title < root.title:
            root.left = self._insert(root.left, book_id, title, author)
        else:
            root.right = self._insert(root.right, book_id, title, author)
        return root

    def search(self, title):
        return self._search(self.root, title)

    def _search(self, root, title):
        if root is None or root.title == title:
            return root
        if title < root.title:
            return self._search(root.left, title)
        return self._search(root.right, title)

# Create book tree and insert books
book_tree = BookSearchTree()
book_tree.insert(1, "The Great Gatsby", "F. Scott Fitzgerald")
book_tree.insert(2, "1984", "George Orwell")
book_tree.insert(3, "Moby Dick", "Herman Melville")

# Search for a book by title
book = book_tree.search("1984")
if book:
    print(f"Found Book: {book.title} by {book.author}")
else:
    print("Book not found.")

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("1. Add User")
        print("2. Add Book")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. View Books")
        print("6. Search Books")
        print("7. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            add_user(username, password)
            print("User added successfully!")
        
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter author: ")
            genre = input("Enter genre: ")
            add_book(title, author, genre)
            print("Book added successfully!")
        
        elif choice == "3":
            # Handle user_id input validation
            while True:
                try:
                    user_id = int(input("Enter user ID: "))
                    break  # exit the loop if the input is valid
                except ValueError:
                    print("Invalid input. Please enter a valid integer for user ID.")
            
            book_id = int(input("Enter book ID: "))
            borrow_book(user_id, book_id)
            create_transaction(user_id, book_id, 'borrow')
            print("Book borrowed successfully!")
        
        elif choice == "4":
            # Handle book_id input validation
            while True:
                try:
                    book_id = int(input("Enter book ID: "))
                    break  # exit the loop if the input is valid
                except ValueError:
                    print("Invalid input. Please enter a valid integer for book ID.")
            
            return_book(book_id)
            create_transaction(user_id, book_id, 'return')
            print("Book returned successfully!")
        
        elif choice == "5":
            connection = db_connect()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(f"ID: {book[0]} | Title: {book[1]} | Author: {book[2]} | Status: {book[4]}")
            cursor.close()
            connection.close()
        
        elif choice == "6":
            title = input("Enter book title to search: ")
            book = book_tree.search(title)
            if book:
                print(f"Found: {book.title} by {book.author}")
            else:
                print("Book not found.")
        
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

