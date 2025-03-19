import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file (if it exists)
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    description = input("Enter task description: ")
    task = {"id": len(tasks) + 1, "description": description, "done": False}
    tasks.append(task)
    print(f"Task '{description}' added!")

# View all tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")
        for task in tasks:
            status = "✔" if task["done"] else "✘"
            print(f"{task['id']}. {task['description']} [{status}]")

# Mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to mark complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
                print(f"Task '{task['description']}' marked as complete!")
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_id = int(input("Enter task ID to delete: "))
        for i, task in enumerate(tasks):
            if task["id"] == task_id:
                deleted_task = tasks.pop(i)
                print(f"Task '{deleted_task['description']}' deleted!")
                # Reassign IDs to maintain sequence
                for j, t in enumerate(tasks, 1):
                    t["id"] = j
                return
        print("Task ID not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Main program loop
def main():
    tasks = load_tasks()
    
    while True:
        print("\n=== To-Do List App ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        save_tasks(tasks)  # Save after every action

if __name__ == "__main__":
    main()