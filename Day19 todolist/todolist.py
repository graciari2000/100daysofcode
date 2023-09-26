# To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display the to-do list
def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the to-do list.")

# Function to mark a task as complete
def complete_task(index):
    if 1 <= index <= len(tasks):
        completed_task = tasks.pop(index - 1)
        print(f"Task '{completed_task}' marked as complete.")
    else:
        print("Invalid task index.")

# Function to delete a task
def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

# Main loop for the to-do list application
while True:
    print("\nOptions:")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. Delete a task")
    print("4. View to-do list")
    print("5. Quit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '2':
        display_tasks()
        index = int(input("Enter the task number to mark as complete: "))
        complete_task(index)
    elif choice == '3':
        display_tasks()
        index = int(input("Enter the task number to delete: "))
        delete_task(index)
    elif choice == '4':
        display_tasks()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")