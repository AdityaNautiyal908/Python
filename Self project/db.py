import sqlite3
from task import Task

# Connect to the SQLite database (or create it if it doesn't exist)
def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn


# Create the tasks table if it doesn't exist
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        description TEXT,
                        completed BOOLEAN)''')
    conn.commit()
    conn.close()

# Add a new task to the database
def add_task(task):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (task.description, task.completed))
    conn.commit()
    conn.close()

# View all tasks from the database
def view_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    tasks = [Task(row[1], row[2]) for row in rows]  # Create Task objects from the database rows
    conn.close()
    return tasks

# Mark a task as completed
def mark_completed(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET completed = ? WHERE id = ?", (True, task_id))
    conn.commit()
    conn.close()

# Delete a task from the database
def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
