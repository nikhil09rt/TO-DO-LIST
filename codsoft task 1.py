#TASK 1 :- TO DO LIST

class TodoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task, description):
        self.tasks[task] = description
        print(f"Task '{task}' added.")

    def update_task(self, task, new_description):
        if task in self.tasks:
            self.tasks[task] = new_description
            print(f"Task '{task}' updated.")
        else:
            print(f"Task '{task}' not found.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks:")
            for task, description in self.tasks.items():
                print(f" - {task}: {description}")
        else:
            print("No tasks in the list.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. View Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task name: ")
            description = input("Enter task description: ")
            todo_list.add_task(task, description)
        elif choice == '2':
            task = input("Enter task name to update: ")
            new_description = input("Enter new task description: ")
            todo_list.update_task(task, new_description)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
