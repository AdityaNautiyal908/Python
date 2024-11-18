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
                    pass
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
    tasks.append(task)

    print(f"Task '{task}' has been added")

def view_Tasks():
    print("Your task do to")
    for i,task in enumerate(tasks,start=1):
        print(f"{i}. {task}")

main_menu()

