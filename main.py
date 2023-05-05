from enum import Enum
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["todolist"]
collection = db["tasks"]


class MenuOptions(Enum):
    CREATE = "create"
    READ = "read"
    UPDATE = "update"
    DELETE = "delete"
    EXIT = "exit"


def create_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status: ")
    task = {"title": title, "description": description, "status": status}
    result = collection.insert_one(task)
    print("Task created with id:", result.inserted_id)


def read_tasks():
    tasks = list(collection.find())
    for task in tasks:
        print(task)


def update_task():
    task_id = input("Enter task id: ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    status = input("Enter task status: ")
    new_values = {"$set": {"title": title, "description": description, "status": status}}
    collection.update_one({"_id": task_id}, new_values)
    print("Task updated successfully.")


def delete_task():
    task_id = input("Enter task id: ")
    collection.delete_one({"_id": task_id})
    print("Task deleted successfully.")


def main_menu():
    while True:
        print("Main Menu")
        print("1. Create task")
        print("2. Read tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = MenuOptions(choice)
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == MenuOptions.CREATE:
            create_task()
        elif choice == MenuOptions.READ:
            read_tasks()
        elif choice == MenuOptions.UPDATE:
            update_task()
        elif choice == MenuOptions.DELETE:
            delete_task()
        elif choice == MenuOptions.EXIT:
            print("Exiting program...")
            break


if __name__ == "__main__":
    main_menu()
