import json

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file doesn't exist or is empty

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks):
    """Adds a new task to the to-do list"""
    title = input("Enter task title: ").strip()
    category = input("Enter task category (Work, Personal, Shopping, etc.): ").strip()
    priority = input("Enter task priority (High, Medium, Low): ").strip().capitalize()
    due_date = input("Enter due date (YYYY-MM-DD): ").strip()

    task = {
        "title": title,
        "category": category,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task '{title}' added successfully!")

# Remove a task
def remove_task(tasks):
    """Removes a task by title"""
    title = input("Enter task title to remove: ").strip()
    for task in tasks:
        if task["title"].lower() == title.lower():
            tasks.remove(task)
            save_tasks(tasks)
            print(f"🗑 Task '{title}' removed successfully!")
            return
    print("⚠ Task not found!")

# Edit a task
def edit_task(tasks):
    """Edits an existing task"""
    title = input("Enter task title to edit: ").strip()
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Leave blank to keep current value.")
            new_title = input(f"New title ({task['title']}): ").strip() or task["title"]
            new_category = input(f"New category ({task['category']}): ").strip() or task["category"]
            new_priority = input(f"New priority ({task['priority']}): ").strip().capitalize() or task["priority"]
            new_due_date = input(f"New due date ({task['due_date']}): ").strip() or task["due_date"]

            task.update({
                "title": new_title,
                "category": new_category,
                "priority": new_priority,
                "due_date": new_due_date
            })
            save_tasks(tasks)
            print(f"✏ Task '{new_title}' updated successfully!")
            return
    print("⚠ Task not found!")

# Mark a task as complete
def mark_task_complete(tasks):
    """Marks a task as completed"""
    title = input("Enter task title to mark as complete: ").strip()
    for task in tasks:
        if task["title"].lower() == title.lower():
            task["completed"] = True
            save_tasks(tasks)
            print(f"✅ Task '{title}' marked as complete!")
            return
    print("⚠ Task not found!")

# List all tasks
def list_tasks(tasks, filter_by=None):
    """Lists tasks, with optional filtering"""
    if not tasks:
        print("📭 No tasks found!")
        return

    if filter_by == "incomplete":
        tasks = [task for task in tasks if not task["completed"]]
    elif filter_by == "complete":
        tasks = [task for task in tasks if task["completed"]]
    elif filter_by == "priority":
        tasks = sorted(tasks, key=lambda t: t["priority"], reverse=True)
    elif filter_by == "due_date":
        tasks = sorted(tasks, key=lambda t: t["due_date"])

    print("\n📋 TO-DO LIST 📋")
    for task in tasks:
        status = "✅ Done" if task["completed"] else "❌ Pending"
        print(f"- {task['title']} [{task['priority']}] ({task['category']}) Due: {task['due_date']} → {status}")
    print()

# Main Menu
def main():
    tasks = load_tasks()

    while True:
        print("\n📌 SMART TO-DO LIST MENU 📌")
        print("1️⃣ Add Task")
        print("2️⃣ Remove Task")
        print("3️⃣ Edit Task")
        print("4️⃣ Mark Task as Complete")
        print("5️⃣ List All Tasks")
        print("6️⃣ List Pending Tasks")
        print("7️⃣ List Completed Tasks")
        print("8️⃣ Sort by Priority")
        print("9️⃣ Sort by Due Date")
        print("0️⃣ Exit")

        choice = input("Select an option (0-9): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            remove_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            mark_task_complete(tasks)
        elif choice == "5":
            list_tasks(tasks)
        elif choice == "6":
            list_tasks(tasks, filter_by="incomplete")
        elif choice == "7":
            list_tasks(tasks, filter_by="complete")
        elif choice == "8":
            list_tasks(tasks, filter_by="priority")
        elif choice == "9":
            list_tasks(tasks, filter_by="due_date")
        elif choice == "0":
            print("👋 Exiting. See you next time!")
            break
        else:
            print("⚠ Invalid choice, please try again.")

# Run the to-do list application
if __name__ == "__main__":
    main()
