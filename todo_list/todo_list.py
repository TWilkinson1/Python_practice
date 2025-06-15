todo_list = []
filename = "todo_list.txt"

def load_tasks():
    try:
        with open(filename, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []
    
def save_tasks():
    with open(filename, 'w') as file:
        for task in todo_list:
            file.write(task + '\n')

def show_choices():
    print("Todo List Application")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Clear all tasks")
    print("5. Exit")

    while True:
            try:
                choice = int(input("Enter your choice (1-5): "))
                if choice in [1, 2, 3, 4, 5]:
                    return choice
                else:
                     print("Invalid choice. Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

todo_list = load_tasks()

while True:
            choice = show_choices()
            if choice == 1:
                task = input("Enter the task to add: ")
                todo_list.append(task)
                print(f"Task '{task}' added.")
                save_tasks()
                continue
            elif choice == 2:
                if todo_list:
                    print("Current tasks:")
                    for i, task in enumerate(todo_list, start=1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks in the list.")
                    save_tasks()
                continue
            elif choice == 3:
                task_to_remove = input("Enter the task to remove: ")
                if task_to_remove in todo_list:
                    todo_list.remove(task_to_remove)
                    print(f"Task '{task_to_remove}' removed.")
                else:
                    print(f"Task '{task_to_remove}' not found in the list.")
                save_tasks()
            elif choice == 4:
                todo_list.clear()
                print("All tasks cleared.")
                save_tasks()
                continue
            elif choice == 5:
                print("Exiting the Todo List Application. Goodbye!")
                break
    