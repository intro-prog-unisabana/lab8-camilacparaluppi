"""Laboratorio 8 - CLI del gestor de tareas."""

# TODO: Implementar CLI según README.md
import sys
from todo_manager import read_todo_file
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
    else:
        print("Command not found!")