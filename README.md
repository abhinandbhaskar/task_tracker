# Task Tracker CLI
Project URL: https://roadmap.sh/projects/task-tracker
A simple Command Line Interface (CLI) application to manage daily tasks using Python and JSON storage.

## Features

- Add tasks
- List tasks
- Update tasks
- Delete tasks
- Mark tasks as done
- Mark tasks as in progress
- List completed tasks
- List todo tasks
- Store tasks in JSON file

## Technologies Used

- Python
- JSON
- File Handling

## Project Structure

task_tracker/
│
├── task_cli.py
├── tasks.json
└── README.md

## Commands

### Add Task

```bash
python task_cli.py add "Study Python"
List Tasks
python task_cli.py list
Update Task
python task_cli.py update 1 "Learn Django"
Delete Task
python task_cli.py delete 1
Mark Task as Done
python task_cli.py mark_done 1
Mark Task as In Progress
python task_cli.py mark_in_progress 1
List Done Tasks
python task_cli.py list_done
List Todo Tasks
python task_cli.py list_todo
Task Properties

Each task contains:

id
description
status
createdAt
updatedAt
Author

Abhinand Bhaskar