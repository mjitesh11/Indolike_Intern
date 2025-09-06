# Advanced To-Do List App (CLI) with File Storage, Status, Due Date, Priority

import datetime

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    try:
        with open(TASKS_FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    task, status, due_date, priority = [p.strip() for p in parts]
                    tasks.append({
                        "task": task,
                        "status": status,
                        "due_date": due_date,
                        "priority": priority
                    })
    except FileNotFoundError:
        pass
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for t in tasks:
            f.write(f"{t['task']} | {t['status']} | {t['due_date']} | {t['priority']}\n")

def show_menu():
    print("\n==== Advanced To-Do List Menu ====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            status_symbol = "✅" if t["status"] == "Done" else "⏳"
            print(f"{i}. {t['task']} [{status_symbol} {t['status']}] "
                  f"(Due: {t['due_date']}, Priority: {t['priority']})")

def add_task(tasks):
    task = input("Enter a new task: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    # Validate due date
    try:
        datetime.datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("⚠️ Invalid date format. Setting as 'No Due Date'")
        due_date = "No Due Date"

    if priority not in ["High", "Medium", "Low"]:
        priority = "Low"

    tasks.append({"task": task, "status": "Pending", "due_date": due_date, "priority": priority})
    save_tasks(tasks)
    print("✅ Task added!")

def update_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter updated task: ")
            new_due_date = input("Enter new due date (YYYY-MM-DD): ")
            new_priority = input("Enter new priority (High/Medium/Low): ").capitalize()

            try:
                datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
            except ValueError:
                new_due_date = tasks[task_num - 1]["due_date"]

            if new_priority not in ["High", "Medium", "Low"]:
                new_priority = tasks[task_num - 1]["priority"]

            tasks[task_num - 1].update({
                "task": new_task,
                "due_date": new_due_date,
                "priority": new_priority
            })
            save_tasks(tasks)
            print("✏️ Task updated!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"🗑️ Deleted: {removed['task']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to mark as Done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["status"] = "Done"
            save_tasks(tasks)
            print(f"🎉 Task marked as Done: {tasks[task_num - 1]['task']}")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            mark_done(tasks)
        elif choice == "6":
            print("👋 Exiting To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

if __name__ == "__main__":
    main()
