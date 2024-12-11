from db import create_table, add_task, view_tasks, mark_completed, delete_task
from task import Task

def menu():
    print("""
    -------------------------
    1. Add Task
    2. View Tasks
    3. Mark Task as Completed
    4. Delete Task
    5. Exit
    -------------------------
    """)

def main():
    # Ensure the database table is created at the start
    create_table()

    while True:
        menu()
        choice = input("Choose an option: ").strip()

        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                task = Task(description)
                add_task(task)  # Add task to database
                print(f"Task '{description}' has been added.")
            else:
                print("Task description cannot be empty.")

        elif choice == '2':
            tasks = view_tasks()
            if tasks:
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("No tasks available.")

        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_completed(task_id)
            print(f"Task {task_id} has been marked as completed.")

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
            print(f"Task {task_id} has been deleted.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
