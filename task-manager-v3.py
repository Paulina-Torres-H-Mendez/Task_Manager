import json # we use JSON files to keep track of the lists as they are easy to use and easy to handle
from datetime import datetime  # Used for date validation

# creates a file to store tasks
TASKS_FILE = "tasks.json"

#                                           Functions:

# Load tasks from file if there is any:
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file doesn't exist or is empty

# Saves tasks to the file:
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Function to validate priority inputs:
def validate_priority(priority):
    valid_priorities = ["Low", "Medium", "High"]
    if priority not in valid_priorities:
        print("⚠ Invalid priority! Must be 'Low', 'Medium', or 'High'. Task creation canceled.")
        return False
    return True


# Function to validate due date input:
def validate_due_date(due_date):
    try:
        due_date_obj = datetime.strptime(due_date, "%Y-%m-%d")  # Convert string to date object
        today = datetime.today()

        if due_date_obj < today:
            print("⚠ Invalid date! You cannot add a task with a past due date. Task creation canceled.")
            return False
        return True
    except ValueError:
        print("⚠ Invalid date format! Please use YYYY-MM-DD. Task creation canceled.")
        return False

# Adds a new task:
def add_task(tasks):
    """Adds a new task to the to-do list"""
    title = input("Enter task title: ").strip()
    category = input("Enter task category (Work, Personal, Shopping, etc.): ").strip()

    priority = input("Enter task priority (High, Medium, Low): ").strip().capitalize()
    if not validate_priority(priority):
        return  # Cancel task addition if priority is invalid

    due_date = input("Enter due date (YYYY-MM-DD): ").strip()
    if not validate_due_date(due_date):
        return  # Cancel task addition if due date is invalid

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


# Removes a task:
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


# Removes all completed tasks:
def remove_completed_tasks(tasks):
    """Removes all completed tasks"""
    initial_count = len(tasks)
    tasks[:] = [task for task in tasks if not task["completed"]]  # Keep only uncompleted tasks
    if len(tasks) < initial_count:
        save_tasks(tasks)
        print("🗑 All completed tasks removed successfully!")
    else:
        print("⚠ No completed tasks to remove!")


# Edits a task:
def edit_task(tasks):
    """Edits an existing task"""
    title = input("Enter task title to edit: ").strip()
    for task in tasks:
        if task["title"].lower() == title.lower():
            print("Leave blank to keep current value.")
            new_title = input(f"New title ({task['title']}): ").strip() or task["title"]
            new_category = input(f"New category ({task['category']}): ").strip() or task["category"]

            new_priority = input(f"New priority ({task['priority']}): ").strip().capitalize() or task["priority"]
            if new_priority and not validate_priority(new_priority):
                return  # Cancel update if new priority is invalid

            new_due_date = input(f"New due date ({task['due_date']}): ").strip() or task["due_date"]
            if new_due_date and not validate_due_date(new_due_date):
                return  # Cancel update if new date is invalid

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


# Marks a task as complete:
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


# Lists all tasks:
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





#                                              Main Menu:
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
        print("🔟 Remove All Completed Tasks")
        print("0️⃣ Exit")

        choice = input("Select an option (0-🔟): ").strip()

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
        elif choice == "10":
            remove_completed_tasks(tasks)
        elif choice == "0":
            print("👋 Exiting. See you next time!")
            break
        else:
            print("⚠ Invalid choice, please try again.")


# Run the to-do list application
if __name__ == "__main__":
    main()
