# import sys

# command = sys.argv[1] if len(sys.argv) > 1 else None
# description = sys.argv[2] if len(sys.argv) > 2 else None

# print(f"Command: {command}")
# print(f"Description: {description}")

import os
import sys
import json
from datetime import datetime

if not os.path.exists("tasks.json"):
    with open("tasks.json", "w") as file:
        json.dump([], file)

command = sys.argv[1] if len(sys.argv) > 1 else None

def task_add():

    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    description = sys.argv[2]
    new_task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }
    tasks.append(new_task)

    with open("tasks.json","w") as file:
        json.dump(tasks, file , indent=4)
    print(f"Task added successfully (ID : {new_task['id']})")

def task_list():
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
    print("Task List:", tasks)

def task_delete():
    with open("tasks.json","r") as file:
        tasks = json.load(file)

        tasks_id = int(sys.argv[2])

        updated_tasks = []
        for task in tasks:
            if task["id"] != tasks_id:
                updated_tasks.append(task)

        with open("tasks.json","w") as file:
            json.dump(updated_tasks, file , indent=4)

    print(f"Task with ID {tasks_id} deleted successfully")

def task_update():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        task_id = int(sys.argv[2])
        description = sys.argv[3]
        for task in tasks:
            if task["id"] == task_id:
                task["description"] = description
                task["updatedAt"] = str(datetime.now())
                break
        with open("tasks.json","w") as file:
            json.dump(tasks, file, indent=4)

def mark_done():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        task_id = int(sys.argv[2])
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                task["updatedAt"] = str(datetime.now())
                break

    with open("tasks.json","w") as file:
        json.dump(tasks, file , indent=4)

def mark_in_progress():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        task_id = int(sys.argv[2])
        for task in tasks:
            if task["id"] == task_id:
                task["status"] = "in_progress"
                task["updatedAt"] = str(datetime.now())
                break
    with open("tasks.json","w") as file:
        json.dump(tasks, file , indent=4)

def list_done():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        tasks_list_done=[]
        for task in tasks:
            if task["status"] == "done":
                tasks_list_done.append(task)
        print("List of Done Tasks:", tasks_list_done)

def list_todo():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        tasks_list_todo=[]
        for task in tasks:
            if task["status"] == "todo":
                tasks_list_todo.append(task)
        print("List of To-Do Tasks:", tasks_list_todo)
def list_in_progress():
    with open("tasks.json","r") as file:
        tasks = json.load(file)
        tasks_list_in_progress=[]
        for task in tasks:
            if task["status"] == "in_progress":
                tasks_list_in_progress.append(task)
        print("List of In-Progress Tasks:", tasks_list_in_progress)

if command == "add":
    task_add()
elif command == "list":
    task_list()
elif command == "update":
    task_update()
elif command == "delete":
    task_delete()
elif command == "mark_done":
    mark_done()
elif command == "mark_in_progress":
    mark_in_progress()
elif command == "list_done":
    list_done()
elif command == "list_todo":
    list_todo()
else:
    print("Invalid Command Please add valid command")
