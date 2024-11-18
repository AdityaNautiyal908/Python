def menu():
    print("""
        1. Add Task
        2. View Tasks
        3. Mark Task are Completed
        4. Delete Task
        5. Exit
""")

def main_menu():
    while True:
        try:
            menu()
            choice = input("Enter your choice : ")
            if choice.isdigit():
                choice = int(choice)
                if choice == 1:
                    add_Task()
                elif choice == 2:
                    view_Tasks()
                elif choice == 3:
                    mark_test()
                elif choice == 4:
                    pass
                elif choice == 5:
                    print("Exiting program")
                    break
                else:
                    print("Invalid choice! Please choose a number between 1 and 5.")
            
            else:
                print("Please enter a valid number.")
            
        except Exception as e:
            print(f"Error : {e}")
            
tasks = []
def add_Task():
    task = input("Enter a new task: ")
    task = {'task_name' : task, 'completed' : False}
    tasks.append(task)

    print(f"Task '{task}' has been added")

def view_Tasks():
    print("Your tasks:")
    if not tasks:
        print("No tasks added.")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task['completed'] else "Not Completed"
        print(f"{i}. {task['task_name']} - {status}")

def mark_test():
    view_Tasks()
    task_number = input("Enter the task number to mark as completed : ")

    if task_number.isdigit():
        task_number = int(task_number) - 1

        if 0 <= task_number < len(tasks):
            task = tasks[task_number]
            if task['completed']:
                print("The task is already completed")
            else:
                task['completed'] = True
                print(f"Task '{task['task_name']}' has been marked as completed")
        else:
            print("Invalid task number.")
    else:
        print("Please enter a valid task number.")

main_menu()

