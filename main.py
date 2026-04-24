"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file, write_todo_file
if len(sys.argv) < 3:
    print("Insufficient arguments provided!")
else:
    file_path = sys.argv[1]
    command = sys.argv[2]
    if command == "view":
        tasks = read_todo_file(file_path)
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif command == "add":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "add".')
        task = sys.argv[3]
        tasks = read_todo_file(file_path)
        tasks.append(task)
        write_todo_file(file_path, tasks)
        print(f'Task "{task}" added.')
    elif command == "remove":
        if len(sys.argv) < 4:
            raise IndexError('Task description required for "remove".')
        task = sys.argv[3]
        tasks = read_todo_file(file_path)
        try:
            tasks.remove(task)
            write_todo_file(file_path, tasks)
            print(f'Task "{task}" removed.')
        except ValueError:
            print(f'Task "{task}" not found.')
    else:
        raise ValueError("Command not found!")