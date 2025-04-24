#a list to store tasks- each task will be a dictionary
tasks = []
#function to print the options user can choose from
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Exit")

#function to ask user to type a task and add to list
def add_task():
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    input("Please press Enter to return to menu.")

def view_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    else: 
        for i, task in enumerate(tasks):
            status = "✓" if task["done"] else "✗"
            print(f"{i+1}. [{status}] {task['task']}")

#function to let user pick a task number to mark
def mark_complete():
    view_tasks()
    if tasks:
        try:
            num = int(input("Enter task number to mark as complete: ")) - 1
            if 0 <= num < len(tasks):
                tasks[num]["done"] = True
            else:
                print("Invalid task number.")
        except ValueError: 
            print("Please enter a valid number.")

#main loop 
while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
        input("Please press Enter to return to menu.")
    elif choice == '3':
        mark_complete()
        input("Please press Enter to return to menu.")
    elif choice == '4':
        print("Goodbye")
        break
    else:
        print("Invalid choice.")
        