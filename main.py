"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) < 2:
    print("Insufficient arguments provided!")
elif sys.argv[1] == "--help":
    print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"     - Add a task to the list.
  remove "task"  - Remove a task from the list.
  view           - Display all tasks.

Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view
""")
elif len(sys.argv) < 3:
    print("Insufficient arguments provided!")
else:
    file_path = sys.argv[1]
    tasks = read_todo_file(file_path)
    i = 2
    valid = True  
    while i < len(sys.argv):
        command = sys.argv[i]
        if command == "add":
            if i + 1 >= len(sys.argv):
                print('Task description required for "add".')
                valid = False
                break
            task = sys.argv[i + 1]
            tasks.append(task)
            print(f'Task "{task}" added.')
            i += 2
        elif command == "remove":
            if i + 1 >= len(sys.argv):
                print('Task description required for "remove".')
                valid = False
                break
            task = sys.argv[i + 1]
            try:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
            except ValueError:
                print(f'Task "{task}" not found.')
            i += 2
        elif command == "view":
            print("Tasks:")
            for task in tasks:
                print(task)
            i += 1
        else:
            print("Command not found!")
            valid = False
            break
    if valid:
        write_todo_file(file_path, tasks)